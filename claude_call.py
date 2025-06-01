import json
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import List
import anthropic

load_dotenv()

# Configure the Gemini API
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable in your .env file.")

# Initialize the client
client = genai.Client(api_key=ANTHROPIC_API_KEY)

async def generate_tech_stack(prompt: str) -> dict:
    try:
        # Add schema information to the prompt
        schema_prompt = f"""
{prompt}
"""
        response = anthropic.Anthropic().messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=5000,
        messages=[
            {"role": "user", "content": schema_prompt}
        ]
        )
        
        print('claude response:', response.content[0].text)
        return response.content[0].text
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return {}