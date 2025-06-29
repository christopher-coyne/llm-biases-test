import json

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

    # get tech stacks
    results['hosting'] = {}
    results['frontend_frameworks'] = {}
    results['frontend_styling'] = {}
    results['frontend_libraries'] = {}
    counter = 0
    for category in processed_ideas:
        ideas = category.get('ideas').get('project_ideas')
        for idea in ideas:
            # add hosting to results
            claude_hosting = idea['tech_stacks_json']['claude_tech']['hosting']
            for hosting in claude_hosting:
                results['hosting'][hosting] = results['hosting'].get(hosting, 0) + 1
            gemini_hosting = idea['tech_stacks_json']['gemini_tech']['hosting']
            for hosting in gemini_hosting:
                results['hosting'][hosting] = results['hosting'].get(hosting, 0) + 1
            chatgpt_hosting = idea['tech_stacks_json']['chatgpt_tech']['hosting']
            for hosting in chatgpt_hosting:
                results['hosting'][hosting] = results['hosting'].get(hosting, 0) + 1

            # add frontend frameworks to results
            claude_frontend = idea['tech_stacks_json']['claude_tech']['frontend_frameworks']
            for frontend in claude_frontend:
                results['frontend_frameworks'][frontend] = results['frontend_frameworks'].get(frontend, 0) + 1
            gemini_frontend = idea['tech_stacks_json']['gemini_tech']['frontend_frameworks']
            for frontend in gemini_frontend:
                results['frontend_frameworks'][frontend] = results['frontend_frameworks'].get(frontend, 0) + 1
            chatgpt_frontend = idea['tech_stacks_json']['chatgpt_tech']['frontend_frameworks']
            for frontend in chatgpt_frontend:
                results['frontend_frameworks'][frontend] = results['frontend_frameworks'].get(frontend, 0) + 1

            # add frontend styling to results
            claude_frontend_styling = idea['tech_stacks_json']['claude_tech']['frontend_styling_solutions']
            for styling in claude_frontend_styling:
                results['frontend_styling'][styling] = results['frontend_styling'].get(styling, 0) + 1
            gemini_frontend_styling = idea['tech_stacks_json']['gemini_tech']['frontend_styling_solutions']
            for styling in gemini_frontend_styling:
                results['frontend_styling'][styling] = results['frontend_styling'].get(styling, 0) + 1
            chatgpt_frontend_styling = idea['tech_stacks_json']['chatgpt_tech']['frontend_styling_solutions']
            for styling in chatgpt_frontend_styling:
                results['frontend_styling'][styling] = results['frontend_styling'].get(styling, 0) + 1
            
            # add frontend libraries to results
            claude_frontend_libraries = idea['tech_stacks_json']['claude_tech']['frontend_libraries']
            for library in claude_frontend_libraries:
                if library == 'React Image Compare':
                    print('idea', idea['title'])
                    counter += 1
                results['frontend_libraries'][library] = results['frontend_libraries'].get(library, 0) + 1
            gemini_frontend_libraries = idea['tech_stacks_json']['gemini_tech']['frontend_libraries']
            for library in gemini_frontend_libraries:
                if library == 'React Image Compare':
                    print('idea', idea['title'])
                    counter += 1
                results['frontend_libraries'][library] = results['frontend_libraries'].get(library, 0) + 1
            chatgpt_frontend_libraries = idea['tech_stacks_json']['chatgpt_tech']['frontend_libraries']
            for library in chatgpt_frontend_libraries:
                if library == 'React Image Compare':
                    print('idea', idea['title'])
                    counter += 1
                results['frontend_libraries'][library] = results['frontend_libraries'].get(library, 0) + 1

            

    print(counter)
    # Write the results to the output file
    with open(output_filename, 'w') as f:
        json.dump(results, f, indent=4)
            
    print(f"All project ideas with tech stacks have been written to {output_filename}")

create_outputs()