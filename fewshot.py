from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    system="You are a QA engineer writing bug reports in this exact format: Title | Severity | Steps to Reproduce",
    messages= [
        {"role": "user", "content": "Example: Login button unresponsive | High | 1. Open login page 2. Click login 3. Nothing happens"},
        {"role": "assistant", "content": "Understood. I will follow this exact format."},
        {"role": "user", "content": "Now write a bug report for: search results page shows blank when no results found"}
    ]
)
print(response.content)
print("-------------------------------------------------------------")
print(response.content[0].text)