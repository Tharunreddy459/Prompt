import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up client with API key from .env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Take review input from user
review = input("Enter a review to classify its sentiment: ")

# Define the prompt messages
messages = [
    {"role": "system", "content": "You classify restaurant review sentiment as Positive, Negative, or Neutral."},
    {"role": "user", "content": f"Classify the sentiment of this review:\n\n{review}"}
]

# Send request using latest OpenAI client
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if available
    messages=messages,
    temperature=0
)

# Display result
print("\n🧠 Sentiment:", response.choices[0].message.content.strip())
