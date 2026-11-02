from dotenv import load_dotenv
import os
import anthropic
import chromadb

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")  # Ensure the API key is loaded from the environment variables
anthropic_client = anthropic.Anthropic(api_key=api_key)

user_question = "What happens if someone enters the wrong password?"



client = chromadb.Client()
collection = client.create_collection(name ="testcases")

collection.add(
    documents=["Test case 1: Verify login functionality with valid credentials.",
               "Test case 2: Verify login functionality with invalid credentials.",
               "Test case 3: Verify password reset functionality.",
               "Test case 4: Verify account lockout after multiple failed login attempts.",
               "Test case 5: Verify login page UI elements and responsiveness."
               ],
    ids=["TC01", "TC02", "TC03", "TC04", "TC05"]
)

results = collection.query(query_texts=[user_question], n_results=2)
retrieved_docs = results["documents"][0]

context = "\n".join(retrieved_docs)  # Combine the retrieved documents into a single context string

prompt = f"""Context :
{context}
question : {user_question}
answer the question based on the context provided. If the answer is not present in the context, say "I don't know".
"""
response = anthropic_client.messages.create(
    model="claude-sonnet-4-5", 
    max_tokens=400,
    messages=[{"role": "user", "content": prompt}]
)

print("=== RAG LLM Response ===")
print(response.content[0].text)