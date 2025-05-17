# -*- coding: utf-8 -*-
import os
from typing import List, Tuple, Optional, Dict
import cv2
import pymupdf
import torch.multiprocessing as tmp
import numpy as np
from PIL import Image
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info
from rapid_layout import RapidLayout, VisLayout
from tqdm import tqdm
import torch

# Setup environment and directories
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
output_dir = 'output-md'
os.makedirs(output_dir, exist_ok=True)

# Initialize models and processors
layout_engine = RapidLayout(conf_thres=0.5, model_type="yolov8n_layout_paper")

min_pixels = 256*28*28
max_pixels = 1280*28*28
processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct",
                                          min_pixels=min_pixels,
                                          max_pixels=max_pixels)
model = AutoModelForImageTextToText.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct", 
                                                   torch_dtype="auto", 
                                                   device_map="auto")

DEFAULT_PROMPT = """Use Markdown syntax to convert the text recognized from the image into Markdown format output. You must adhere to the following:
0. The contents of the inputs include scientific papers about plastic degradation via mealworm.
1. Each picture is a page of the corresponding paper pdf. For each graph, if any, in the picture, describe its content and meaning in words and include them in the fianl output.
2. Output must be in the same language as the recognized text in the image. For example, if the fields are in English, the output must also be in English.
3. Do not explain or output irrelevant text. Directly output the content from the image. For instance, it is strictly prohibited to output something like 'The following is the Markdown text I generated based on the image content:' Instead, you should directly output the Markdown.
4. Do not enclose the content in markdown tags. Use $$ $$ for block equations and $ $ for inline equations. Ignore long horizontal lines and page numbers.
Again, do not explain or output irrelevant text. Directly output the content from the image.
"""
DEFAULT_RECT_PROMPT = """Some areas in the image are highlighted with colored rectangular boxes and labeled with names (%s). If the highlighted area is a table or image, insert it into the output using the ![]() format. Otherwise, directly output the text content."""
DEFAULT_ROLE_PROMPT = """You are a PDF document parser, and you should use Markdown and LaTeX syntax to output the content from the image."""

def _parse_pdf_to_images(pdf_path: str, output_dir: str = './output') -> List[Tuple[str, List[str]]]:
    """Convert PDF pages to images and detect figures/tables."""
    image_infos = []
    pdf_document = pymupdf.open(pdf_path)
    
    for page_index, page in enumerate(pdf_document):
        rect_images = []
        
        # Get high-resolution pixmap
        pix = page.get_pixmap(matrix=pymupdf.Matrix(4, 4))
        pix = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        
        # Detect layout elements
        boxes, scores, class_names, _ = layout_engine(pix)
        
        # Extract figures and tables
        for index, (class_name, box) in enumerate(zip(class_names, boxes)):
            if class_name in ('figure', 'table'):
                name = f'{page_index}_{index}.png'
                sub_pix = pix.crop(box)
                sub_pix.save(os.path.join(output_dir, name))
                rect_images.append(name)

        # Prepare visualization
        boxes_ = []
        scores_ = []
        class_names_ = []
        for i, (class_name, box, score) in enumerate(zip(class_names, boxes, scores)):
            if class_name in ('figure', 'table'):
                boxes_.append(box)
                scores_.append(score)
                class_names_.append(f'{page_index}_{i}.png')

        # Save page image with annotations
        page_image = os.path.join(output_dir, f'{page_index}.png')
        pix_array = np.array(pix)
        pix_bgr = cv2.cvtColor(pix_array, cv2.COLOR_RGB2BGR)
        annotated_img = VisLayout.draw_detections(pix_bgr, boxes_, scores_, class_names_)
        if annotated_img is not None:
            cv2.imwrite(page_image, annotated_img)
            
        image_infos.append((page_image, rect_images))
        
    pdf_document.close()
    return image_infos

def _process_page(index: int, image_info: Tuple[str, List[str]], 
                 prompt: str, rect_prompt: str, role_prompt: str) -> Tuple[int, str]:
    """Process a single page and convert it to markdown."""
    page_image, rect_images = image_info
    
    # Build prompt
    local_prompt = role_prompt + prompt
    if rect_images:
        local_prompt += rect_prompt % ', '.join(rect_images)
    
    # Create message for the model
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": page_image},
            {"type": "text", "text": local_prompt}
        ]
    }]
    
    # Process input
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    ).to("cuda")
    
    # Generate output
    generated_ids = model.generate(**inputs, max_new_tokens=2000)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, 
        skip_special_tokens=True, 
        clean_up_tokenization_spaces=False
    )
    
    # Clean up markdown formatting if needed
    content = output_text[0]
    if '```markdown' in content:
        content = content.replace('```markdown\n', '')
        last_backticks_pos = content.rfind('```')
        if last_backticks_pos != -1:
            content = content[:last_backticks_pos] + content[last_backticks_pos + 3:]
            
    return index, content

def _gpt_parse_images(
        image_infos: List[Tuple[str, List[str]]],
        prompt_dict: Optional[Dict] = None,
        output_dir: str = './',
        gpt_worker: int = 1,
        file_name: str = "output",
        **_
) -> str:
    """Parse images to markdown content."""    # Get prompts
    prompt = prompt_dict.get('prompt', DEFAULT_PROMPT) if isinstance(prompt_dict, dict) else DEFAULT_PROMPT
    rect_prompt = prompt_dict.get('rect_prompt', DEFAULT_RECT_PROMPT) if isinstance(prompt_dict, dict) else DEFAULT_RECT_PROMPT
    role_prompt = prompt_dict.get('role_prompt', DEFAULT_ROLE_PROMPT) if isinstance(prompt_dict, dict) else DEFAULT_ROLE_PROMPT

    # Process pages in parallel with multiprocessing
    contents = [None] * len(image_infos)

    tasks = [(index, image_info, prompt, rect_prompt, role_prompt) 
             for index, image_info in enumerate(image_infos)]
    num_workers = min(gpt_worker, torch.cuda.device_count() or 1)
    ctx = tmp.get_context('spawn')  # ensures each child initializes CUDA safely
    with ctx.Pool(processes=num_workers) as pool:
        results = pool.starmap(_process_page, tasks)
        
        for index, content in results:
            contents[index] = content

    # Save combined markdown
    output_text = '\n\n'.join(contents)
    output_path = os.path.join(output_dir, f'{file_name}.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

    return output_text

def parse_pdf(
        pdf_path: str,
        output_dir: str = './',
        prompt: Optional[Dict] = None,
        verbose: bool = False,
        gpt_worker: int = 1,
        file_name: str = "output",
        **kwargs
) -> Tuple[str, List[str]]:
    """Parse a PDF file to a markdown file."""
    os.makedirs(output_dir, exist_ok=True)

    # Extract images from PDF
    image_infos = _parse_pdf_to_images(pdf_path, output_dir=output_dir)
    
    # Process images to markdown
    content = _gpt_parse_images(
        image_infos=image_infos,
        output_dir=output_dir,
        prompt_dict=prompt,
        gpt_worker=gpt_worker,
        file_name=file_name,
        **kwargs
    )

    # Clean up temporary files if not in verbose mode
    all_rect_images = []
    if not verbose:
        for page_image, rect_images in image_infos:
            if os.path.exists(page_image):
                os.remove(page_image)
            all_rect_images.extend(rect_images)
            
    return content, all_rect_images

# Main execution
if __name__ == "__main__":
    # Find all PDF files
    tmp.set_start_method("spawn", force=True)
    pdf_paths = []
    for root, _, files in os.walk('./all-files'):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_paths.append(os.path.join(root, file))

    # Process each PDF
    for path in tqdm(pdf_paths, desc="Processing PDFs"):
        file_name = path.replace('.', '', 1).replace('/', '')
        parse_pdf(
            pdf_path=path,
            output_dir=output_dir,
            verbose=True,
            gpt_worker=1,
            file_name=file_name
        )
