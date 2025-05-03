import openai
import os
from dotenv import load_dotenv

# Load the environment file where your API key is stored
load_dotenv()

# Create the OpenAI client using your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask the user to paste a news article
article = input("Please paste the news article you want to summarize:\n\n")


# Prompt 1: Simple and basic request to summarize
prompt1 = f"{article}\n\nPlease write a summary of this article."

# Prompt 2: Clear request with a rule to write only 3 sentences
prompt2 = f"Read this article and write a short summary in exactly 3 sentences. Include the main idea and important points:\n\n{article}"

# Prompt 3: Ask the model to act like a news expert and include tone and key points
prompt3 = f"You are a news expert. Read the article and write a summary that includes the main events, the feeling or tone of the article, and what it means:\n\n{article}"

# List of all prompts
prompts = [prompt1, prompt2, prompt3]

# List to save the answers from the model
outputs = []

# Use while loop to ask GPT for each prompt
i = 0
while i < len(prompts):
    prompt = prompts[i]
    messages = [
        {"role": "system", "content": "You are a helpful assistant that writes news summaries."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    # Save the answer to the list
    outputs.append(response.choices[0].message.content.strip())
    i += 1

# Print all the answers one by one
print("\n=== Prompt 1 Output ===")
print(outputs[0])
print("\n=== Prompt 2 Output ===")
print(outputs[1])
print("\n=== Prompt 3 Output ===")
print(outputs[2])

#refer readme.md for output

'''
article
In recent years, climate change has led to a noticeable rise in dangerously high temperatures across the globe. 
These extreme heat conditions are putting more people—especially older adults—at serious risk. 
Health experts are warning that rising temperatures are now directly affecting public health, 
including causing more heat-related illnesses and deaths.A new report emphasizes the urgent need for governments to take action by stopping the growth of fossil fuel use 
and investing more in renewable energy. While some steps have been taken, especially in countries like the U.S., 
the overall threat from climate change continues to grow.Without strong and immediate action, future generations could face more severe health and environmental problems.

'''