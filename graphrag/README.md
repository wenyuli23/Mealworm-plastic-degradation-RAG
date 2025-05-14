# GraphRAG Documentation ([Source](https://microsoft.github.io/graphrag/))

## 1. Requirements and Installation

Before you begin, ensure you have:
- Python version: 3.10 to 3.12
- Required packages: GraphRAG, CLI tools, and an LLM API key (e.g., OpenAI)

Installation:
```
pip install graphrag
```

GraphRAG includes a command-line interface (CLI) for a no-code start. (For more details, refer to the Microsoft GraphRAG "Getting Started" documentation.)

---

## 2. Preparing Your Data and Workspace

GraphRAG uses a configuration setup that creates a workspace with environment variables and settings. Initialize your workspace by running:

```
graphrag init --root ./ragtest
```

This command creates two important files:
- `.env`: Contains your API key (e.g., `GRAPHRAG_API_KEY=<your_api_key>`).
- `settings.yaml`: Holds pipeline settings which you can adjust as needed.

---

## 3. Prompt Tuning

GraphRAG features a built‐in prompt tuning module designed to improve the precision of entity extraction and query generation. Users have two options for fine-tuning:

### a. Manual Prompt Tuning
You can directly edit the prompt templates in the configuration file or through the CLI. This approach allows you to inject domain-specific language, adjust response formatting, and experiment with different phrasings. Simply modify the prompt sections in your settings file (typically found in `settings.yaml`) to better align with your data and objectives.

### b. Automatic Prompt Tuning
Alternatively, you can enable automatic prompt tuning. This feature iteratively refines the prompts based on performance feedback from the LLM outputs. The system runs several test iterations—comparing outputs against predefined quality metrics—to suggest an optimal prompt configuration without manual intervention. To activate this, adjust the `prompt_tuning` settings in your configuration (see example below).

```
python -m graphrag prompt-tune --root /path/to/project --config /path/to/settings.yaml --no-entity-types
```

After generation, put the prompts and generated entity types in the appropriate place indicated in `settings.yaml`.

---

## 4. Configure settings.yaml

### a. Configure LLMs
- **OpenAI Mode**: Update your `.env` file with your OpenAI API key.
- **Azure OpenAI**: If you use Azure's service, modify `settings.yaml` to include your Azure endpoint, deployment name, and API version.

### b. To use OpenAI, Groq, etc. with openai format url call
If you intend to use cloud-based LLM services such as OpenAI, Groq, or Deepseek, your settings file should be set up with an API call format. An example configuration might look like this:

```yaml
llm:
  type: openai_chat   # Replace with the corresponding type
  api_base: "https://api.openai.com/v1"   # Replace with the corresponding url
  api_key: "<your_api_key>"  # Replace with your actual API key
  model: "gpt-4"
```

### c. To use custom models that run locally
For local deployments where you want to run models on your hardware, you can configure GraphRAG to use custom local models such as those served by Ollama or LMStudio. In this case, your settings might look like:

```yaml
llm:
  type: openai_chat
  api_base: "http://localhost:1234/v1/"   # Replace with your local host url
  model: "gemma-3-27b-it-GGUF"  # Replace with your model name
embeddings:
  llm:
    model: "nomic-embed-text-v1.5-GGUF"
    api_base: "http://localhost:1234/v1/"   # Replace with your local host url
```

For a detailed explanation for each of the parameters in settings, please refer to the official page for GraphRAG: https://microsoft.github.io/graphrag/config/overview/ and https://microsoft.github.io/graphrag/cli/.

---

## 5. Building the Graph Index

GraphRAG first "indexes" your text by splitting it into chunks, extracting entities and relationships, and then building a knowledge graph.

Execute the following command:

```
graphrag index --root ./ragtest
```

During this process:
- Your text is split into manageable "chunks."
- Entities (such as names, organizations, or key concepts) and their relationships are extracted.
- The pipeline outputs a set of parquet files (or another storage format) under `./ragtest/output`.

This indexing step uses an LLM (like GPT-4 or OpenAI's models) to extract and structure your document data into a knowledge graph.

---

## 6. Querying Your Graph

Once the indexing is complete, you can query your graph to retrieve information. GraphRAG supports two query modes:

### a. Global Search
Global Search helps answer broad questions by leveraging community summaries from the entire dataset. For example:

```
graphrag query \
  --root ./ragtest \
  --method global \
  --query "What are the top themes in this story?"
```

This command:
- Searches across your entire knowledge graph.
- Uses community summaries to generate a synthesized answer.

### b. Local Search
Local Search is ideal for pinpointing specific details within a certain context (for instance, asking about a particular character or entity):

```
graphrag query \
  --root ./ragtest \
  --method local \
  --query "Who is Scrooge and what are his main relationships?"
```

This mode "fans out" from a specified entity to fetch detailed information, allowing for a more focused query response.

In addition, GraphRAG supports filters (e.g., by date or entity type) during the query process.