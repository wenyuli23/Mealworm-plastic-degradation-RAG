from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import pandas as pd
import torch

#tokenizer = AutoTokenizer.from_pretrained("BioMistral/BioMistral-7B-SLERP")
#model = AutoModelForQuestionAnswering.from_pretrained("BioMistral/BioMistral-7B-SLERP")

def answer_question(df, type):
    answers = []
    for query in df['Query']:
        if not pd.isna(query):
            print(query)
            messages = [
                {"role": "user", "content": query},
            ]
            pipe = pipeline("text-generation", model="BioMistral/BioMistral-7B-SLERP", device=0, max_new_tokens=200)
            output = pipe(messages)
            generated_text = output[0]['generated_text']
            answers.append(generated_text)
    df['answer'] = answers
    df.to_excel(f'./answers/{type} output.xlsx', index=False)

for type in ["Text", "TF", "Numerical", "Exp Design"]:
    df = pd.read_excel('Query.xlsx', sheet_name=type, header=0)
    answer_question(df, type)