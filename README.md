# LLM Biases Test

A comprehensive tool for analyzing biases in Large Language Models (LLMs) when generating project ideas and recommending technology stacks. This project tests multiple LLMs (OpenAI GPT, Google Gemini, Anthropic Claude) to identify patterns and preferences in their recommendations across different project categories.

A tool for analyzing biases in LLMs, in particular, OpenAI, Google, and Anthropic. The test works by first generating a list of project ideas of different difficulties, in Main.py. The generate_tech_stack function in that file can be used to generate project guides with the different LLMs. After that, the check.py file can be used to iterate through the list of project plans, and extract different technologies to document how frequently each LLM suggests different frontend frameworks, authentication solutions, backend languages, etc.

## Purpose

This tool was made to help me understand:

- How different LLMs approach project idea generation
- Technology stack preferences across various LLM providers
- Potential biases in AI recommendations for web development projects
- Patterns in difficulty assessment and feature suggestions

## 📁 Project Structure

```
llm-biases-test/
├── main.py                 # Main orchestration script
├── check.py               # Data processing and analysis
├── tech_normalizer.py     # Technology name normalization
├── chatgpt_call.py        # OpenAI GPT integration
├── gemini_call.py         # Google Gemini integration
├── claude_call.py         # Anthropic Claude integration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── project_ideas/         # Generated project data
│   ├── all_project_ideas.json
│   ├── ideas_with_tech.json
│   └── project.json
└── project_ideas/         # Raw project ideas by category
```

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd llm-biases-test
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   GEMINI_API_KEY=your_gemini_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

## 🚀 Usage

### Generate Project Ideas

Run the main script to generate project ideas across all categories:

```bash
python main.py
```

This will:

- Generate project ideas for each category using different LLMs
- Collect technology stack recommendations
- Save results to the `project_ideas/` directory

### Analyze Results

Process and analyze the generated data:

```bash
python check.py
```

This creates normalized technology statistics and bias analysis.

### Individual LLM Testing

You can also test individual LLMs:

```python
# Test OpenAI GPT
import chatgpt_call
result = chatgpt_call.generate_projects(prompt)

# Test Google Gemini
import gemini_call
result = gemini_call.generate_projects(prompt)

# Test Anthropic Claude
import claude_call
result = claude_call.generate_projects(prompt)
```

## Important Notes

- Batch processing for these different LLMs should be considered. Doing so will result in a considerably cheaper and faster experiment.
