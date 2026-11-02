from dotenv import load_dotenv
import os
import anthropic

load_dotenv()  # reads your .env file and loads its contents

api_key = os.getenv("ANTHROPIC_API_KEY")  # pulls out just that one value by name
client = anthropic.Anthropic(api_key=api_key) 

response = client.messages.create( #the actual API call
    model="claude-sonnet-4-5",
    max_tokens=20,
    messages=[
        {"role": "user", "content": "What is the difference between a bug and a defect in QA?"}
    ]
)

print(response.content[0].text)
print(response.usage)
