import json
from tech_normalizer import normalize_technology

def create_outputs():
    # Full results for the json
    results = {}

    # Read the existing project ideas
    filename = "./project_ideas/ideas_with_tech.json"
    output_filename = "./project_ideas/project.json"
    
    with open(filename, 'r') as f:
        project_ideas = json.load(f)
    
    processed_ideas = project_ideas.copy()
    
    # Process each category and its project ideas
    results ['all_project_ideas'] = {}
    for category_data in processed_ideas:
        category = category_data.get('category', '')
        ideas = category_data.get('ideas').get('project_ideas')
        results['all_project_ideas'][category] = [{'title': idea['title'], 'description': idea['description'], 'difficulty': idea['difficulty']} for idea in ideas]

    # Initialize tech stack categories
    tech_categories = ['hosting', 'frontend_frameworks', 'frontend_styling_solutions', 'frontend_libraries', 
                      'backend_frameworks', 'backend_languages', 'authentication', 'orms', 'databases', 'other_tools']
    
    for category in tech_categories:
        results[category] = {}
    
    # Tech stack sources to iterate through
    tech_sources = ['claude_tech', 'gemini_tech', 'chatgpt_tech']
    
    counter = 0
    for category in processed_ideas:
        ideas = category.get('ideas').get('project_ideas')
        for idea in ideas:
            # Loop through each tech source (claude, gemini, chatgpt)
            for tech_source in tech_sources:
                tech_data = idea.get('tech_stacks_json', {}).get(tech_source, {})
                
                # Loop through each tech category (hosting, frontend_frameworks, etc.)
                for tech_category in tech_categories:
                    tech_items = tech_data.get(tech_category, [])
                    
                    # Normalize each tech item and count the normalized version
                    normalized_items = []
                    for item in tech_items:
                        normalized_item = normalize_technology(item, tech_category)
                        normalized_items.append(normalized_item)
                    
                    # Count each normalized item in the category
                    for normalized_item in normalized_items:
                        results[tech_category][normalized_item] = results[tech_category].get(normalized_item, 0) + 1

    # LLM preferences
    results['llm_preferences'] = {}
    
    # Initialize LLM preferences structure
    for tech_source in tech_sources:
        llm_name = tech_source.replace('_tech', '')  # Remove '_tech' suffix to get clean LLM name
        results['llm_preferences'][llm_name] = {}
        
        # Initialize each tech category for this LLM
        for tech_category in tech_categories:
            results['llm_preferences'][llm_name][tech_category] = {}
    
    # Initialize difficulty preferences structure
    results['difficulty_preferences'] = {}
    difficulty_levels = ['Easy', 'Medium', 'Difficult']
    
    for difficulty in difficulty_levels:
        results['difficulty_preferences'][difficulty] = {}
        for tech_category in tech_categories:
            results['difficulty_preferences'][difficulty][tech_category] = {}
    
    # Count LLM preferences and difficulty preferences
    for category in processed_ideas:
        ideas = category.get('ideas').get('project_ideas')
        for idea in ideas:
            difficulty = idea.get('difficulty', '')
            
            # Loop through each tech source (claude, gemini, chatgpt)
            for tech_source in tech_sources:
                llm_name = tech_source.replace('_tech', '')
                tech_data = idea.get('tech_stacks_json', {}).get(tech_source, {})
                
                # Loop through each tech category for this LLM
                for tech_category in tech_categories:
                    tech_items = tech_data.get(tech_category, [])
                    
                    # Normalize each tech item and count the normalized version
                    normalized_items = []
                    for item in tech_items:
                        normalized_item = normalize_technology(item, tech_category)
                        normalized_items.append(normalized_item)
                    
                    # Count each normalized item suggested by this LLM
                    for normalized_item in normalized_items:
                        # Count for LLM preferences
                        results['llm_preferences'][llm_name][tech_category][normalized_item] = results['llm_preferences'][llm_name][tech_category].get(normalized_item, 0) + 1
                        
                        # Count for difficulty preferences
                        if difficulty in difficulty_levels:
                            results['difficulty_preferences'][difficulty][tech_category][normalized_item] = results['difficulty_preferences'][difficulty][tech_category].get(normalized_item, 0) + 1

    print(counter)
    # Write the results to the output file
    with open(output_filename, 'w') as f:
        json.dump(results, f, indent=4)
            
    print(f"All project ideas with tech stacks have been written to {output_filename}")

create_outputs()