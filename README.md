# Leveraging Knowledge Graph–Based Retrieval Augmented Generation to Accelerate Insights on Mealworm Larvae and Plastic Degradation

A repository for exploring and comparing different Retrieval-Augmented Generation (RAG) approaches for scientific literature about mealworms and related organisms. Paper: *_Leveraging Knowledge Graph–Based Retrieval Augmented Generation to Accelerate Insights on Mealworm Larvae and Plastic Degradation._*

## Overview

This repository contains code and data for applying different RAG systems and specialized tools to scientific literature on mealworms and related biodegradation text. It allows for comparing different approaches of RAG-based information retrieval and question answering.

## Repository Structure

- **`data/`**: Contains source materials for RAG processing
  - Abstract text files for mealworm vs waxworm comparison
  - Query spreadsheets

- **`graphrag/`**: Configuration of Microsoft's GraphRAG
  - GraphRAG configuration with following analysis
  - Supports both global and local search methods
  - README with detailed guidelines

- **`lightrag/`**: Configuration of LightRAG
  - Lightweight RAG Configuration with OpenAI API integration
  - Configurable models and embedding settings
  - Multiple query modes

- **`rag_baseline/`**: Traditional vector-based RAG system using LangChain and FAISS for comparison

- **`ft_bio.py`**: Fine-tuned biological language model evaluation script with BioMistral-7B-SLERP

- **`pdfconvertor_new.py`**: Advanced PDF-to-Markdown conversion pipeline
  - Converts scientific PDFs to structured markdown using Qwen2.5-VL-7B vision model
  - Includes layout detection for figures and tables
  - Optimized for scientific literature processing

- **`answers/`**: Output directory for query responses

- **`knowledge graphs/`**: Generated knowledge graphs from different RAG systems

## Getting Started

### GraphRAG Setup ([Source](https://microsoft.github.io/graphrag/get_started/))

1. Install the GraphRAG package:
   ```
   pip install graphrag
   ```

2. Initialize your workspace:
   ```
   graphrag init --root ./your_workspace
   ```

3. Configure settings in the `.env` and `settings.yaml` files with your API keys and model preferences.

4. Build the graph index:
   ```
   graphrag index --root ./your_workspace
   ```

5. Query the graph using global or local search methods:
   ```
   graphrag query --root ./your_workspace --method local --query "Your question here"
   ```

See the GraphRAG README for detailed instructions.

### LightRAG Setup

1. Configure your model and API settings in [`lightrag/config.env`](lightrag/config.env)
   - Select your preferred model (GPT-5, qwen, etc.)
   - Set your embedding model and parameters
   - Configure API endpoints and keys

2. Run queries using the lightrag_api_mw.py script

## License

This repository implements existing RAG technologies (GraphRAG from Microsoft and LightRAG) for research purposes. Please refer to their respective licenses for usage terms.
