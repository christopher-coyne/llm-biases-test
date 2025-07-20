import json
from tech_normalizer import normalize_technology

frontend_frameworks = ['React', 'Angular', 'Vue', "Next.js", "Nuxt.js", "Svelte", "Svelte Kit", "Astro", "Alpine.js", "Hugo", "HTMX", "Eleventy"]
frontend_styling_solutions = ["Material UI", "Tailwind CSS", "Daisy UI", "Chakra UI", "Ant Design", "ShadCN", "Headless UI", "CSS Modules", "Styled Components", "SASS/SCSS", "Radix UI", "Bootstrap", "Emotion", "Mantine", "Pico.css"]

databases = ['MongoDB', 'PostgreSQL', 'Redis', 'Pinecone', "Timescale DB", "Amazon Redshift", "Elasticsearch", "Clickhouse", "Snowflake", "Amazon S3", "InfluxDB", "AWS Timestream", "Neo4J", "Amazon Dynamo DB", "AWS RDS", "AWS Elasticache", "AWS OpenSearch", "PostGIS", "Amazon DocumentDB", "SQLite", "Cassandra", "OrbitDB", "IndexedDB"]
db_orms = ['Mongoose', 'Sequelize', 'Prisma', 'TypeORM', 'Django ORM', 'SQLAlchemy', 'GORM', 'Knex.js', 'Alembic', 'Drizzle', 'SQLModel']

backend_languages = ['Python', 'Typescript', 'Javascript', 'Go', 'Ruby', 'Solidity', 'PHP', 'C#', 'Java', 'Rust']
backend_frameworks = ['Express', 'Fast API', 'NestJS', 'Django', 'Flask', 'Gin', 'Spring Boot', 'Gorilla Mux', 'Hardhat']

hosting = ['Railway', 'Vercel', 'Render', 'Heroku', 'AWS', 'Azure', 'Supabase', 'Neon', 'Google Cloud', 'Netlify', 'Fly.io', 'Cloudflare', 'Digital Ocean', '']

# TODO - Batch processing is a much faster way to process the project ideas
def create_outputs():
    # Full results for the json
    results = {}

    # Read the existing project ideas
    filename = "./project_ideas/ideas_with_tech.json"
    output_filename = "./project_ideas/project.json"
    
    with open(filename, 'r') as f:
        project_ideas = json.load(f)
    
    processed_ideas = project_ideas.copy()
    
    # process each category
    results ['all_project_ideas'] = {}
    for category_data in processed_ideas:
        category = category_data.get('category', '')
        ideas = category_data.get('ideas').get('project_ideas')
        results['all_project_ideas'][category] = [{'title': idea['title'], 'description': idea['description'], 'difficulty': idea['difficulty']} for idea in ideas]

    tech_categories = ['hosting', 'frontend', 'backend', 'authentication', 'orms', 'databases', 'other_tools']
    frontend_subcategories = ['frontend_frameworks', 'frontend_styling_solutions', 'frontend_libraries']
    backend_subcategories = ['backend_frameworks', 'backend_languages']
    
    for category in tech_categories:
        results[category] = {}
    
    tech_sources = ['claude_tech', 'gemini_tech', 'chatgpt_tech']
    
    counter = 0
    for category in processed_ideas:
        ideas = category.get('ideas').get('project_ideas')
        for idea in ideas:
            counter += 1
            # each tech source (claude, gemini, chatgpt)
            for tech_source in tech_sources:
                tech_data = idea.get('tech_stacks_json', {}).get(tech_source, {})
                
                # frontend categories grouped under 'frontend'
                for frontend_subcat in frontend_subcategories:
                    tech_items = tech_data.get(frontend_subcat, [])
                    
                    # Normalize each tech item
                    normalized_items = set()
                    for item in tech_items:
                        #some technologies are not normalized, e.g React.js --> react
                        normalized_item = normalize_technology(item, frontend_subcat)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results['frontend'][normalized_item] = results['frontend'].get(normalized_item, 0) + 1
                
                # backend subcategories grouped under 'backend'
                for backend_subcat in backend_subcategories:
                    tech_items = tech_data.get(backend_subcat, [])
                    
                    normalized_items = set()
                    for item in tech_items:
                        normalized_item = normalize_technology(item, backend_subcat)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results['backend'][normalized_item] = results['backend'].get(normalized_item, 0) + 1
                
                # Handle other tech categories (non-frontend, non-backend)
                other_tech_categories = ['hosting', 'authentication', 'orms', 'databases', 'other_tools']
                for tech_category in other_tech_categories:
                    tech_items = tech_data.get(tech_category, [])
                    
                    normalized_items = set()
                    for item in tech_items:
                        normalized_item = normalize_technology(item, tech_category)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results[tech_category][normalized_item] = results[tech_category].get(normalized_item, 0) + 1

    # LLMs
    results['llm_preferences'] = {}
    
    for tech_source in tech_sources:
        llm_name = tech_source.replace('_tech', '') 
        results['llm_preferences'][llm_name] = {}
        
        # Initialize each tech category for this LLM
        for tech_category in tech_categories:
            results['llm_preferences'][llm_name][tech_category] = {}
    
    # difficulties
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
            
            for tech_source in tech_sources:
                llm_name = tech_source.replace('_tech', '')
                tech_data = idea.get('tech_stacks_json', {}).get(tech_source, {})
                
                for frontend_subcat in frontend_subcategories:
                    tech_items = tech_data.get(frontend_subcat, [])
                    
                    normalized_items = set()
                    for item in tech_items:
                        normalized_item = normalize_technology(item, frontend_subcat)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results['llm_preferences'][llm_name]['frontend'][normalized_item] = results['llm_preferences'][llm_name]['frontend'].get(normalized_item, 0) + 1
                        
                        if difficulty in difficulty_levels:
                            results['difficulty_preferences'][difficulty]['frontend'][normalized_item] = results['difficulty_preferences'][difficulty]['frontend'].get(normalized_item, 0) + 1
                
                for backend_subcat in backend_subcategories:
                    tech_items = tech_data.get(backend_subcat, [])
                    
                    normalized_items = set()
                    for item in tech_items:
                        normalized_item = normalize_technology(item, backend_subcat)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results['llm_preferences'][llm_name]['backend'][normalized_item] = results['llm_preferences'][llm_name]['backend'].get(normalized_item, 0) + 1
                        
                        if difficulty in difficulty_levels:
                            results['difficulty_preferences'][difficulty]['backend'][normalized_item] = results['difficulty_preferences'][difficulty]['backend'].get(normalized_item, 0) + 1
                
                other_tech_categories = ['hosting', 'authentication', 'orms', 'databases', 'other_tools']
                for tech_category in other_tech_categories:
                    tech_items = tech_data.get(tech_category, [])
                    
                    normalized_items = set()
                    for item in tech_items:
                        normalized_item = normalize_technology(item, tech_category)
                        normalized_items.add(normalized_item)
                    
                    for normalized_item in normalized_items:
                        results['llm_preferences'][llm_name][tech_category][normalized_item] = results['llm_preferences'][llm_name][tech_category].get(normalized_item, 0) + 1
                        
                        if difficulty in difficulty_levels:
                            results['difficulty_preferences'][difficulty][tech_category][normalized_item] = results['difficulty_preferences'][difficulty][tech_category].get(normalized_item, 0) + 1

    print(f"Total number of projects processed: {counter}")
    with open(output_filename, 'w') as f:
        json.dump(results, f, indent=4)
            
    print(f"All project ideas with tech stacks have been written to {output_filename}")