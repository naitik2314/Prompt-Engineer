from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

if not GEMINI_API_KEY:
    print("Invalid Gemini API key, please refer to the readme file to add Gemini key to your .env file")

def generate_prompt(task, provider, version):
    sys_instruct = "You are a prompt engineer, now you implement the best practices of prompt engineer to get the best model output out of llm defined"
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model = gemini_model,
        config = types.GenerateContentConfig(
            system_instruction=sys_instruct
        ),
        contents=[f"Generate a really extensive prompt for {task}. This prompt will be passed to {provider}'s {version} model. Use the best practices recommened for entering prompt for the given llm proveder and model"]
    )
    return response


provider = input("Enter the LLM (Large Language Model) provider you want to generate prompt for? (Examples of Providers: Anthropic, Gemini, ChatGPT, Ollama, Mistral etc). Press Enter for default value (ChatGPT): ").strip()
version = input("Enter the LLM model you would like to use for the selected provider(press Enter for default value ('4o')): ").strip()
gemini_model = input("Enter the Gemini model to use for generating the prompt or press enter to use the default (Default value is gemini-2.0-flash-exp): ").strip()
task = input("Enter the prompt you want engineered: ").strip()

if (provider == '') and (version == '') and (gemini_model == ''):
    provider = 'ChatGPT'
    version = '4o'
    gemini_model = 'gemini-2.0-flash-exp'
else:
    provider = provider
    version = version
    gemini_model = gemini_model

print(f"Selected provider: {provider}, selected model version: {version}")

response = generate_prompt(task=task, provider=provider, version=version)

print("Here is the generated prompt!")
print(response)

