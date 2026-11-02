from dotenv import load_dotenv
import os
import anthropic
import requests

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")  # Ensure the API key is loaded from the environment variables
client = anthropic.Anthropic(api_key=api_key)

question = "What should I check when testing a login page?"
# Claude's answer
claude_response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=400,
    messages=[{"role": "user", "content": question}]
)

print("=== CLAUDE ===")
print(claude_response.content[0].text)

# Ollama's answer (phi3:mini running locally)
ollama_response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": question,
        "stream": False
    }
)
print("\n=== OLLAMA (phi3:mini) ===")
print(ollama_response.json()["response"])