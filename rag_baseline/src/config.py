import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Folders
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT.parent / "data" / "md"
VSTORE_DIR = ROOT / "vectorstore"
DOTENV_PATH = ROOT / '.env'

# Models (env override allowed)
load_dotenv(find_dotenv(), override=True)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")

# Chunking
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
TOP_K = 4   
