import json
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import List
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable in your .env file.")
client = genai.Client(api_key=OPENAI_API_KEY)

async def generate_tech_stack(prompt: str) -> dict:
    try:
        schema_prompt = f"""
        {prompt}
        """
        client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        )

        response = client.responses.create(
            model="gpt-4o",
            input=schema_prompt,
        )
            
        print('chatgpt response:', response.output_text)
        return response.output_text
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return {}