import openai
import os
from dotenv import load_dotenv

load_dotenv()


print("hello")
# Set up client with API key from .env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Take review input from user
review = input("Enter your request to generate Python code for finding pairs that sum to a target: ")

# Define the prompt messages
messages = [
    {"role": "system", "content": "You are a Python expert who writes optimized and readable code."},
    {"role": "user", "content": f"Write Python code for the following task:\n\n{review}"}
]

# Send request using latest OpenAI client
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=messages,
    temperature=0
)

# Display result
print("\n💡 Generated Python Code:\n")
print(response.choices[0].message.content.strip())
