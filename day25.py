#Day 25 tomorrow — Hallucination Detection
from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
api_key =  os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

hallucination_test_prompt = """What did Andrej Karpathy say in his 2019 paper about transformer context windows exceeding 1 million tokens?"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens = 400,
    messages=[
        {
            "role": "user",
            "content": hallucination_test_prompt
        }
    ]
)
#print (response.content[0])
print (response.content[0].text)
