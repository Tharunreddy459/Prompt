import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up client with API key from .env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Take review input from user
review = input("Enter the English paragraph to translate into Spanish: ")

# Define the prompt messages
messages = [
    {"role": "system", "content": "You are a professional technical translator fluent in English and Spanish."},
    {"role": "user", "content": f"Translate the following technical paragraph to Spanish:\n\n{review}"}
]

# Send request using latest OpenAI client
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=messages,
    temperature=0
)

# Display result
print("\n🌐 Translated Paragraph (Spanish):\n")
print(response.choices[0].message.content.strip())
