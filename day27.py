#Day 27: RAGAS, Evaluating a RAG Pipeline

from dotenv import load_dotenv
import os
import anthropic
import chromadb
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
anthropic_client = anthropic.Anthropic(api_key=api_key)

# ---------- PART 1: your Day 22 RAG pipeline ----------
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="testcases")
collection.add(
    documents=["Test case 1: Verify login functionality with valid credentials.",
               "Test case 2: Verify login functionality with invalid credentials.",
               "Test case 3: Verify password reset functionality.",
               "Test case 4: Verify account lockout after multiple failed login attempts.",
               "Test case 5: Verify login page UI elements and responsiveness."],
    ids=["TC01", "TC02", "TC03", "TC04", "TC05"]
)

user_question = "What happens if someone enters the wrong password?"
results = collection.query(query_texts=[user_question], n_results=2)
retrieved_docs = results["documents"][0]
context = "\n".join(retrieved_docs)

prompt = f"""Context:
{context}
Question: {user_question}
Answer based on the context provided. If the answer is not present in the context, say "I don't know"."""

response = anthropic_client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=400,
    messages=[{"role": "user", "content": prompt}]
)
answer = response.content[0].text

# ---------- PART 2: RAGAS grades the RAG output ----------
judge_client = anthropic.AsyncAnthropic(api_key=api_key)
judge_llm = llm_factory("claude-sonnet-4-5", provider="anthropic", client=judge_client)
judge_llm.model_args.pop("top_p", None)
faithfulness = Faithfulness(llm=judge_llm)

result = faithfulness.score(
    user_input=user_question,
    response=answer,
    retrieved_contexts=retrieved_docs
)

print("ANSWER:", answer)
print("FAITHFULNESS:", result.value)