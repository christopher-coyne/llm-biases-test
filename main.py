"""
llms to test:
- openai
- gemini
- claude
- grok
- deepseek
"""

import os
from typing import List
import time
from gemini_call import generate_projects
import json
import claude_call
import gemini_call
import chatgpt_call  # Import the module instead of the function
import asyncio

categories = [
    # Core Business & Commerce
    "Accounting", "Advertising", "Auctions", "Business",
    "Consulting", "CRM", "Crowdfunding", "E-commerce", "Entrepreneurship", 
    "Finance", "Human Resources", "Insurance", "Investment", 
    "Legal", "Logistics", "Manufacturing", "Marketing",
    "Payroll", "Real Estate", "Recruiting", "Sales", "Supply Chain", "Tax Preparation",
    
    # Technology & Development
    "AI", "API Management", "Automation", "Backup Services", "Blockchain", 
    "CDN", "Cloud Computing", "Code Repository", "Database Management", 
    "Developer Tools", "DevOps", 
    "Technology Error Tracking", "Integration", "IoT", "Legacy Systems", "Technology Migration", "Network Monitoring", "Open Source Technologies", 
    "SaaS Tools", "Software Security", "Server Management", "Technology", "TestingFrameworks",
    "Version Control", "VR/AR", "Web Hosting", "Webhooks", "Software Development Workflow",
    
    # Healthcare & Wellness
    "Healthcare Accessibility", "Dental Care", "Emergency Services", "Health", 
    "Medical Records", "Medicine", "Mental Health", "Pharmacy", 
    "Telemedicine", "Therapy", "Veterinary", "Wellness",
    
    # Media & Entertainment
    "Art", "Audio", "Books", "Broadcasting", "Design", "Entertainment", 
    "Gaming", "Journalism", "Live Streaming", "Music", "News", 
    "Photography", "Podcasting", "Publishing", "Radio", 
    "Video", "Writing", "Content Creation", "Content Marketing",
    "Social Media", "Influencer Marketing", "Graphic Design",
    "Video Production", "Video Editing", "Audio Production", 
    
    # Education & Learning
    "Education", "Languages", "Academic Research", "Science", "Tutoring",
    "Online Courses", "Online Tutoring",
    
    # Lifestyle & Personal
    "Beauty", "Charity", "Collectibles", "Community", "Dating", "DIY", 
    "Events", "Fashion", "Fitness", "Food", "Gardening", "Gift Giving", 
    "Hobbies", "Meditation", "Nutrition", "Parenting", "Party Planning", 
    "Personal Services", "Pets", "Recipes", "Religion", "Seasonal/Holiday", 
    "Social Causes", "Sports", "Travel", "Volunteering", 
    "Wedding Planning",
    
    # Government & Public Services
    "City Services", "Fire Department", "Government", "Military", 
    "Municipal", "Police", "Politics", "Public Safety",
    
    # Industry & Professional
    "Agriculture", "Aviation", "Automotive", "Chemicals", "Construction", 
    "Defense", "Environment", "Maritime", "Mining", "Oil & Gas", 
    "Renewable Energy", "Textiles", "Transportation",
    
    # Communication & Collaboration
    "Communication", "Customer Support", "Help Desk", 
    "Localization", "Privacy", "Remote Work", "Scheduling", "Translation",
    
    # Information & Services
    "Analytics", "Cultural Heritage", "Cultural Sites",
    "Documentation", "Genealogy", "Geography",
    "Libraries", "Local Business", "Maps", "Membership Sites", "Museums", 
    "Parks", "Polls", "Productivity", "Property Management", "Quizzes", 
    "Recreation", "Repair Services", "Reviews", "Subscription Services", 
    "Surveys", "Testing", "Ticketing", "Tourism", "Weather",
    
    # Professional Services & Compliance
    "Activism", "Auditing", "Inventory Management", "Market Research", "Quality Control"
]

"""
VERY IMPORTANT: also explain the tech stack that you would recommend for this project, and why. At a bare minimum, the tech stack must include the Language for the web app and how to host it, although you may also provide any frameworks, authentication solutions, ORMs, styling solutions, libraries, authentication, databases, and tools that you think are relevant. 
"""

def get_project_ideas(category: str) -> str:
    prompt = f"Generate a list of project ideas in web development that pertain to this category: {category}. You should generate 9 project ideas. These projects should try to address some problem or need that exists in the category. The project idea descriptions should be a lengthy few paragraphs, and explain in detail the idea and the features it has. Also, generate projects of different difficulty. Generate 3 Easy projects (which a beginner web dev could do), 3 Medium difficulty projects (which may take a mid level engineer several months to finish) and 3 Difficult projects (which would require a senior engineer and operate on a very large scale and with novel challenges). IMPORTANT: do not focus on the tech stack, only include the features and what the project is about. Provide your answer as json, in the following format: {{'category': 'The category you are doing this for', 'project_ideas': [{{'title': 'Project Title', 'description': 'Project Description', 'difficulty': 'Easy/Medium/Difficult''}}, ...]}}"
    return generate_projects(prompt)

def generate_project_ideas():
    # Create a directory to store results if it doesn't exist
    if not os.path.exists('project_ideas'):
        os.makedirs('project_ideas')
    
    filename = "project_ideas/all_project_ideas.json"
    
    # Initialize the file with an empty list if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    
    # Process each category
    for category in categories:
        print(f"\nProcessing category: {category}")
        
        # Get project ideas
        ideas = get_project_ideas(category)
        print(ideas)
        
        # Read existing data
        with open(filename, 'r') as f:
            all_project_ideas = json.load(f)
        
        # Append the new ideas
        all_project_ideas.append({"category": category, "ideas": ideas})
        
        # Write the updated data back to the file
        with open(filename, 'w') as f:
            json.dump(all_project_ideas, f, indent=4)
        
        time.sleep(1)
    
    print(f"All project ideas have been written to {filename}")


# Assuming your methods are async
async def get_all_tech_stacks(prompt):
    tech_stack_claude, tech_stack_chatgpt, tech_stack_gemini = await asyncio.gather(
        claude_call.generate_tech_stack(prompt),
        chatgpt_call.generate_tech_stack(prompt),
        gemini_call.generate_tech_stack(prompt)
    )
    return tech_stack_claude, tech_stack_chatgpt, tech_stack_gemini

def generate_tech_stack():
    # Read the existing project ideas
    filename = "project_ideas/ideas_with_tech.json"
    output_filename = "project_ideas/ideas_with_tech.json"
    
    with open(filename, 'r') as f:
        project_ideas = json.load(f)
    
    # Initialize or load the output file
    if os.path.exists(output_filename):
        with open(output_filename, 'r') as f:
            processed_ideas = json.load(f)
    else:
        processed_ideas = project_ideas.copy() 
    
    # Process each category and its project ideas
    for category_data in processed_ideas:
        category = category_data.get('category', '')
        ideas = category_data.get('ideas', [])
        
        for project in ideas['project_ideas']:
            print('processing project: ', project.get('title', ''))
            if project.get('tech_stacks_json'):
                print('project already has a tech stack')
            else:
                prompt = f"Give me an overview for how I should Build the following project: {project.get('title', '')} - {project.get('description', '')}. In general, I want some help devising a plan to build this project, including what technologies I should be using. Please include the tech stack in your response, this means telling me how to do the frontend, backend, databases, hosting, authentication, etc. Give me a high level overview of how you would recommend I build this. IMPORTANT: keep this opinionated, don't give me multiple options, just give me the best one."
                
                # Add the tech stack to the project
                tech_stack_claude, tech_stack_chatgpt, tech_stack_gemini = asyncio.run(
                get_all_tech_stacks(prompt))

                project['claude_tech'] = tech_stack_claude
                project['chatgpt_tech'] = tech_stack_chatgpt
                project['gemini_tech'] = tech_stack_gemini

                # jsonify the tech stack
                jsonify_tech_stack_prompt = f"I am going to provide a list of tech project overviews from multiple LLms, I want you to take these, and extract the tech stack recommendations from each, and return them in a json of the following format: claude_tech: {{backend_languages: string, backend_frameworks: string, databases: string, other_tools: string, frontend_frameworks: string, frontend_libraries: string, hosting: string, authentication: string, orms: string, frontend_styling_solutions: string}}, chatgpt_tech: {{...}}, gemini_tech: {{...}} IMPORTANT: Be selective - only return the tech stack recommendations explictly recommended in the project overview, and don't include any other tech stack recommendations. Heres the tech stach for claude: {tech_stack_claude}, heres the tech stack for chatgpt: {tech_stack_chatgpt}, heres the tech stack for gemini: {tech_stack_gemini}"
                tech_stacks_json = gemini_call.jsonify_tech_stack(jsonify_tech_stack_prompt)
                
                project['tech_stacks_json'] = tech_stacks_json
                # Write the updated data after each project
                with open(output_filename, 'w') as f:
                    json.dump(processed_ideas, f, indent=4)
                time.sleep(1)  # Add a small delay between API calls
            
            print(f"Processed project: {project.get('title', '')} in category: {category}")
    
    print(f"All project ideas with tech stacks have been written to {output_filename}")

if __name__ == "__main__":
    # generate_project_ideas()
    generate_tech_stack()