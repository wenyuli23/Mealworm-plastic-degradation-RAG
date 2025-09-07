import argparse
from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
from tqdm import tqdm

from src.config import DOTENV_PATH, VSTORE_DIR, CHAT_MODEL, EMBEDDING_MODEL, TOP_K
from src.prompts import RAG_PROMPT


def format_docs(docs):
    from langchain_core.documents import Document
    return "\n\n---\n\n".join(
        f"[{i+1}] {d.metadata.get('source','')}:\n{d.page_content}"
        for i, d in enumerate(docs)
    )

def get_llm(model_name: str, temperature: float = 0.2):
    """Get the appropriate LLM based on the model name."""
    model_name_lower = model_name.lower()
    
    # Llama models via Ollama
    if 'llama' in model_name_lower:
        return ChatOllama(model=model_name, temperature=temperature)
    
    # DeepSeek models via OpenAI-compatible API
    elif 'deepseek' in model_name_lower:
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            base_url="https://api.deepseek.com/v1",
            api_key=os.getenv("DEEPSEEK_API_KEY")
        )
    
    # Qwen models via OpenAI-compatible API
    elif 'qwen' in model_name_lower:
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
            api_key=os.getenv("QWEN_API_KEY")
        )
    
    # OpenAI models (including GPT-4, GPT-3.5, etc.)
    elif 'gpt' in model_name_lower:
        return ChatOpenAI(model=model_name, temperature=temperature)
    
    # Default: raise an error for unknown model types
    else:
        raise ValueError(f"Unknown model type: '{model_name}'")

def build_chain():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vstore = FAISS.load_local(str(VSTORE_DIR), embeddings, allow_dangerous_deserialization=True)
    retriever = vstore.as_retriever(search_kwargs={"k": TOP_K})
    llm = get_llm(CHAT_MODEL, temperature=0.2)

    chain = (
        {"input": RunnablePassthrough(), "context": retriever | format_docs}
        | RAG_PROMPT
        | llm
    )
    return chain


def run_cli_mode(chain):
    while True:
        q = input("\nAsk a question (or 'exit'): ").strip()
        if not q or q.lower() == "exit":
            break
        resp = chain.invoke(q)
        print("\n" + resp.content)


def run_excel_mode(chain, excel_path: Path, sheet: str, question_col: str, out_path: Path):
    # Read questions
    df = pd.read_excel(excel_path, sheet_name=sheet)
    if question_col not in df.columns:
        raise ValueError(f"Column '{question_col}' not found. Available: {list(df.columns)}")
    questions = df[question_col].astype(str).fillna("").tolist()

    # Process questions with progress bar
    outputs = []
    for question in tqdm(questions, desc="Processing queries"):
        response = chain.invoke(question)
        outputs.append(response.content)

    # Write results
    out_df = pd.DataFrame({question_col: questions, "answer": outputs})
    out_df.to_excel(f"{sheet}_{out_path}", index=False)
    print(f"Wrote {len(out_df)} rows to {sheet}_{out_path}.")


def main():
    print("CHAT_MODEL:", os.getenv("CHAT_MODEL"))
    load_dotenv(DOTENV_PATH, override=True)

    parser = argparse.ArgumentParser(description="Query RAG index from CLI or Excel.")
    parser.add_argument("--excel", type=Path, help="Path to input Excel file (optional).")
    parser.add_argument("--sheet", default=0, help="Sheet name or index (default=0).")
    parser.add_argument("--question-col", default="question", help="Column with user questions (default='question').")
    parser.add_argument("--out", type=Path, default=f"{CHAT_MODEL}_answers.xlsx", help="Output Excel path (default=answers.xlsx).")
    args = parser.parse_args()  # argparse is the standard way to add CLI options :contentReference[oaicite:4]{index=4}

    chain = build_chain()

    if args.excel:
        run_excel_mode(chain, args.excel, args.sheet, args.question_col, args.out)
    else:
        run_cli_mode(chain)


if __name__ == "__main__":
    main()
