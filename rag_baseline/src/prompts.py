from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You must answer strictly from the provided context. "
     "If the answer is not in the context, say \"I don't know.\""),
    ("human", "Question: {input}\n\nContext:\n{context}")
])
