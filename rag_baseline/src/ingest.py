import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from src.config import DATA_DIR, VSTORE_DIR, DOTENV_PATH, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP
from src.loaders import load_documents

def main():
    load_dotenv(DOTENV_PATH, override=True)

    # 1) Load raw docs
    docs = load_documents(DATA_DIR)

    # 2) Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)

    # 3) Embed and build FAISS
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vstore = FAISS.from_documents(chunks, embeddings)

    # 4) Persist FAISS index
    VSTORE_DIR.mkdir(parents=True, exist_ok=True)
    vstore.save_local(str(VSTORE_DIR))
    print(f"Indexed {len(chunks)} chunks; saved to {VSTORE_DIR}")

if __name__ == "__main__":
    main()
