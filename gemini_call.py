import json
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable in your .env file.")

# Initialize the client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Define Pydantic models for schema validation
class ProjectIdea(BaseModel):
    title: str = Field(..., description="The title of the project idea")
    description: str = Field(..., description="A detailed description of the project idea")
    difficulty: str = Field(..., description="The difficulty level: Easy, Medium, or Difficult")

class ProjectIdeasResponse(BaseModel):
    category: str = Field(..., description="The category these project ideas belong to")
    project_ideas: List[ProjectIdea] = Field(..., description="List of project ideas for this category")

def generate_content(prompt: str) -> dict:
    try:
        # Add schema information to the prompt
        schema_prompt = f"""
{prompt}

IMPORTANT: Your response must strictly follow this JSON schema:
{ProjectIdeasResponse.model_json_schema()}

Respond ONLY with valid JSON that matches this schema. Do not include any other text, markdown formatting, or explanations.
"""
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=schema_prompt,
            config={
            "response_mime_type": "application/json",
            "response_schema": ProjectIdeasResponse,
        })
        
        print('Raw response text:', response.text)
        try:
            # Strip markdown code block markers if present
            text = response.text

            parsed_data = json.loads(text)
            validated_data = ProjectIdeasResponse.model_validate(parsed_data)
            return validated_data.model_dump()
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            print("Invalid JSON content:", text)
            return {}
        except Exception as e:
            print(f"Schema validation error: {str(e)}")
            return {}
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return {}