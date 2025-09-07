from pathlib import Path
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_core.documents import Document

def load_documents(md_folder: Path) -> List[Document]:
    """Load .txt and .md files into LangChain Documents."""
    # Load .txt
    txt_loader = DirectoryLoader(
        path=str(md_folder),
        glob="**/*.txt",
        loader_cls=TextLoader,  # plain text
    )
    docs_txt = txt_loader.load()

    # Load .md (UnstructuredMarkdownLoader supports 'single' or 'elements' modes)
    md_loader = DirectoryLoader(
        path=str(md_folder),
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        loader_kwargs={"mode": "single"},  # keep each file as one Document
    )
    docs_md = md_loader.load()

    return docs_txt + docs_md
