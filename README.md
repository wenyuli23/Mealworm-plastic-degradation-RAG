# Mealworm-RAG

A repository for exploring and comparing different Retrieval-Augmented Generation (RAG) approaches for scientific literature about mealworms and related organisms. Paper: *_Leveraging Knowledge Graph–Based Retrieval Augmented Generation to Accelerate Insights on Mealworm Larvae and Plastic Degradation._*

## Overview

This repository contains code and data of applying two RAG systems to scientific literature on mealworms and related biodegradation text. It allows for comparing different approaches of knowledge-graph-based information retrieval and question answering.

## Repository Structure

- **`data/`**: Contains source materials for RAG processing
  - Scientific papers in PDF format
  - Abstract text files for mealworm vs waxworm comparison
  - Query spreadsheets
  - Converted markdown files

- **`graphrag/`**: Configuration of Microsoft's GraphRAG
  - GraphRAG configuration with following analysis
  - Supports both global and local search methods
  - README with detailed guidelines

- **`lightrag/`**: Configuration of LightRAG
  - Lightweight RAG Configuration with OpenAI API integration
  - Configurable models and embedding settings
  - Multiple query modes

- **`answers/`**: Output directory for query responses

- **`knowledge graphs/`**: Output directory for generated knowledge graphs from the two RAGs

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
   - Select your preferred model (GPT-4o-mini, deepseek-chat, etc.)
   - Set your embedding model and parameters
   - Configure API endpoints and keys

2. Run queries using the lightrag_api_mw.py script

## License

This repository implements existing RAG technologies (GraphRAG from Microsoft and LightRAG) for research purposes. Please refer to their respective licenses for usage terms.
