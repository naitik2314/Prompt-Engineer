from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_prompt(task, provider, version):
    pass


provider = input("Enter the LLM (Large Language Model) provider you want to generate prompt for? (Examples of Providers: Anthropic, Gemini, ChatGPT, Ollama, Mistral etc). Press Enter for default value (ChatGPT): ")
version = input("Enter the LLM model you would like to use for the selected provider(press Enter for default value ('4o')): ")

if (provider == '' or provider == ' ') and (version == '' or version == ' '):
    provider = 'ChatGPT'
    version = '4o'
else:
    provider = provider
    version = version

print(f"Selected provider: {provider}, selected model version: {version}")




