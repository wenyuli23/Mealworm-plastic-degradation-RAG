# Baseline Vector-only RAG (LangChain + FAISS)

A traditional vector-based RAG system using LangChain and FAISS for RAG comparison on mealworm plastic degradation.

## Features

- **Multiple LLM Support**: OpenAI GPT models, Qwen, DeepSeek, and Llama via Ollama
- **Vector Retrieval**: FAISS-based semantic search with configurable top-k results
- **Batch Processing**: Excel-based query processing for systematic evaluation
- **Flexible Configuration**: Environment-based model and parameter configuration

## Quick Start

1. **Install dependencies**:
   python >= 3.10
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env to set API keys (OPENAI_API_KEY, QWEN_API_KEY, DEEPSEEK_API_KEY)
   ```

3. **Build vector index**:
   ```bash
   python -m src.ingest
   ```

4. **Query interactively**:
   ```bash
   python -m src.query
   ```

5. **Batch process from Excel**:
   ```bash
   python -m src.query --excel Final_query_set.xlsx --sheet "open-ended" --question-col "question"
   ```

## Configuration

Key parameters in `src/config.py`:
- `CHUNK_SIZE`: 1200 tokens per document chunk
- `CHUNK_OVERLAP`: 200 tokens overlap between chunks
- `TOP_K`: 4 retrieved documents per query
- Models configurable via environment variables
