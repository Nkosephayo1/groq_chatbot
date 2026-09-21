import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Your Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Default model
GROQ_MODEL = "openai/gpt-oss-120b"

if GROQ_API_KEY is None:
    print("⚠️ WARNING: GROQ_API_KEY is not set!")
