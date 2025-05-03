import openai
import os
from dotenv import load_dotenv

# Load the environment file that contains the API key
load_dotenv()

# Create the OpenAI client using your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask the user to paste a resume
resume = input("Please paste the resume text you want to check:\n\n")

# Prompt 1: Role-based prompt asking as a hiring manager
role_prompt = [
    {"role": "system", "content": "You are a hiring manager reviewing a job applicant's resume."},
    {"role": "user", "content": f"Please read and evaluate the following resume. Give feedback on the strengths, weaknesses, and if the resume is a good match for a data analytics role:\n\n{resume}"}
]

# Prompt 2: Simple general prompt with no role
generic_prompt = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Give your thoughts on this resume:\n\n{resume}"}
]

# Get response for the role-based prompt
response1 = client.chat.completions.create(
    model="gpt-4o",
    messages=role_prompt,
    temperature=0
)
output1 = response1.choices[0].message.content.strip()

# Get response for the generic prompt
response2 = client.chat.completions.create(
    model="gpt-4o",
    messages=generic_prompt,
    temperature=0
)
output2 = response2.choices[0].message.content.strip()

# Print both outputs for comparison
print("\n=== Role-Based Prompt Output ===")
print(output1)

print("\n=== Generic Prompt Output ===")
print(output2)

# refer readme.md for report analysis
#example resume used
'''
Name: Priya Sharma  
Email: priya.sharma@example.com  
Phone: +19876543210  

Objective:  
To obtain a challenging position in data analytics where I can apply my statistical, technical, and analytical skills to solve real-world problems.

Skills:  
- Data Analysis using Python and R  
- SQL, Excel, and Power BI  
- Machine Learning Basics  
- Data Visualization and Reporting  
- Strong problem-solving and communication skills  

Experience:  
Data Analyst Intern, Infosys Ltd (Jan 2023 – Jun 2023)  
- Analyzed client data to identify trends and presented weekly reports to the analytics team  
- Built dashboards using Power BI to track KPIs  

Education:  
B.Sc. in Statistics, Delhi University, 2022  

Certifications:  
- Google Data Analytics Professional Certificate  
- Python for Data Science Coursera

'''
