import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)  # Create a client instance

# Define the review
review = input("Enter the input: ")

# Define the prompt
# messages = [
#     {"role": "system", "content": "You classify restaurant review sentiment as Positive, Negative, or Neutral."},
#     {"role": "user", "content": f'Classify the sentiment of this review:\n\n"{review}"\n\nSentiment:'}
# ]

# messages = [
#     {"role": "system", "content": "You identify the language of the given text."},
#     {"role": "user", "content": f'Detect the language of this sentence:\n\n"{review}"\n\nLanguage:'}
# ]

messages = [
    {"role": "system", "content": "You correct grammar and spelling in English text."},
    {"role": "user", "content": f'Correct the following text:\n\n"{review}"\n\nCorrected:'}
]

# Call the GPT-4o model
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0 #0-20, 0 is the most deterministic and 2 is the most creative
)

# Extract and print the result
# print(response)
sentiment = response.choices[0].message.content.strip()
print(f"Corrected response : {sentiment}")
