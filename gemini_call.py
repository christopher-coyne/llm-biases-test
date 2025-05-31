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

class TechStack(BaseModel):
    frontend_frameworks: List[str] = Field(..., description="The language for the web app")
    frontend_libraries: List[str] = Field(..., description="Libraries for the web app")
    frontend_styling_solutions: List[str] = Field(..., description="Styling solutions for the web app")
    hosting: List[str] = Field(..., description="How to host the web app")
    backend_frameworks: List[str] = Field(..., description="Frameworks for the web app")
    backend_languages: List[str] = Field(..., description="Languages for the web app")
    authentication: List[str] = Field(..., description="Authentication solutions for the web app")
    orms: List[str] = Field(..., description="ORMs for the web app")
    databases: List[str] = Field(..., description="Databases for the web app")
    other_tools: List[str] = Field(..., description="Other tools for the web app")

class ModelTechStack(BaseModel):
    claude_tech: TechStack = Field(..., description="The tech stack for the project idea")
    chatgpt_tech: TechStack = Field(..., description="The tech stack for the project idea")
    gemini_tech: TechStack = Field(..., description="The tech stack for the project idea")

def generate_projects(prompt: str) -> dict:
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
    
def generate_tech_stack(prompt: str) -> dict:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=prompt,
            config={
                "response_mime_type": "text/plain",
            }
        )
        return response.text
    except Exception as e:
        print(f"Error generating tech stack: {str(e)}")
        return {}
    
def jsonify_tech_stack(prompt: str) -> dict:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": ModelTechStack,
            }
        )
        text = response.text

        print('jsonified tech stack: ', text)

        parsed_data = json.loads(text)
        validated_data = ModelTechStack.model_validate(parsed_data)
        return validated_data.model_dump()
    except Exception as e:
        print(f"Error generating tech stack: {str(e)}")
        return {}
    