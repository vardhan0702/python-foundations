from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=150,
    system="",
    temperature=1,
    messages= [
        {"role": "user", "content": "Suggest one creative edge case for testing a file upload feature."}
    ]
)
print(response.content[0].text)