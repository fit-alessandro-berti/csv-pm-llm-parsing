import os

OPENAI_API_URL = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)

if os.path.exists("openai_api_url.txt"):
    OPENAI_API_URL = open("openai_api_url.txt", "r").read().strip()

if os.path.exists("openai_api_key.txt"):
    OPENAI_API_KEY = open("openai_api_key.txt", "r").read().strip()

if OPENAI_API_KEY is None or not OPENAI_API_KEY:
    raise Exception("Please check your environment variables before using CSV-PM-LLM-parsing: OPENAI_API_KEY is not defined!")

if OPENAI_API_URL.endswith("/"):
    OPENAI_API_URL = OPENAI_API_URL[:-1]
