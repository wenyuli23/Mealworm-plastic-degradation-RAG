import os
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc
import numpy as np
import asyncio
import nest_asyncio
import pandas as pd
from dotenv import load_dotenv

# Apply nest_asyncio to solve event loop issues
nest_asyncio.apply()

load_dotenv()

# Configure working directory
MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
DEFAULT_RAG_DIR = f"./outputs/{MODEL}"
os.makedirs(DEFAULT_RAG_DIR, exist_ok=True)

# Configure working directory and models
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_MAX_TOKEN_SIZE = int(os.getenv("EMBEDDING_MAX_TOKEN_SIZE", 8192))
EMBEDDING_URL = os.getenv("EMBEDDING_URL", "https://api.openai.com/v1/")
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", "")

# Configure API endpoints
MODEL_URL = os.getenv("MODEL_URL", "https://api.openai.com/v1/")

# Configure API keys
API_KEY = os.getenv("API_KEY", "")

# Print configuration for debugging
print(f"Configuration loaded from environment variables:")
print(f"WORKING_DIR: {DEFAULT_RAG_DIR}")
print(f"LLM_MODEL: {LLM_MODEL}")
print(f"EMBEDDING_MODEL: {EMBEDDING_MODEL}")
print(f"EMBEDDING_MAX_TOKEN_SIZE: {EMBEDDING_MAX_TOKEN_SIZE}")
print(f"EMBEDDING_URL: {EMBEDDING_URL}")
print(f"BASE_URL: {MODEL_URL}")
print(f"API keys loaded: MODEL: {bool(API_KEY)}, EMBED: {bool(EMBEDDING_API_KEY)}")
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)


# LLM model function
async def llm_model_func(
    prompt, system_prompt=None, history_messages=[], keyword_extraction=False, **kwargs
) -> str:
    return await openai_complete_if_cache(
        model=MODEL,
        prompt=prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        base_url=MODEL_URL,
        api_key=API_KEY,
        temperature=1,
        top_p=0.8,
        **kwargs,
    )


# Embedding function


async def embedding_func(texts: list[str]) -> np.ndarray:
    return await openai_embed(
        texts=texts,
        model=EMBEDDING_MODEL,
        base_url=EMBEDDING_URL,
        api_key=EMBEDDING_API_KEY,
    )


async def get_embedding_dim():
    test_text = ["This is a test sentence."]
    embedding = await embedding_func(test_text)
    embedding_dim = embedding.shape[1]
    print(f"{embedding_dim=}")
    return embedding_dim


# Initialize RAG instance
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=llm_model_func,
    embedding_func=EmbeddingFunc(
        embedding_dim=asyncio.run(get_embedding_dim()),
        max_token_size=EMBEDDING_MAX_TOKEN_SIZE,
        func=embedding_func,
    )
)

""" folder_path = "../data/md/"
md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
for filename in md_files:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        rag.insert(f.read()) """
""" 
def get_answer(df, type, mode):
    answers = []
    for query in df['Query']:
        if not pd.isna(query):
            print(query)
            answer = rag.query(query, param=QueryParam(mode=mode))
            answers.append(answer)

    df[mode] = answers

for type in ["Text", "TF", "Numerical", "Exp Design"]:
    df = pd.read_excel('../data/Query.xlsx', sheet_name=type, header=0)
    for mode in ["naive", "local", "global", "hybrid"]:
        get_answer(df, type, mode)
    df.to_excel(f'./answers/{MODEL}/{MODEL} {type} output.xlsx', index=False)
    print(f'Answers written to {MODEL} {type} output.xlsx')"""

print(
    rag.query("What specific enzyme derived from Klebsiella sp. EMBL-1 can degrade PVC film?", param=QueryParam(mode="hybrid")),
    rag.query("Can the catalase-peroxidase derived from Klebsiella sp. EMBL-1 deconstruct or oxidize PVC film with enough dose?", param=QueryParam(mode="hybrid"))
)