from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    system="You are a strict senior QA engineer. Answer in exactly 3 bullet points, no more, no less.",
    messages = [
        {"role": "user", "content": "What should I check when testing a login page?"}
    ]
)
print(response.content[0].text)