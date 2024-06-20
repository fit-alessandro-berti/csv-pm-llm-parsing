import os

SLEEP_TIME = 3
MAX_RETRY = 5
OPENAI_API_URL = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", None)

if os.path.exists("openai_api_url.txt"):
    OPENAI_API_URL = open("openai_api_url.txt", "r").read().strip()

if os.path.exists("openai_api_key.txt"):
    OPENAI_API_KEY = open("openai_api_key.txt", "r").read().strip()

if os.path.exists("openai_model.txt"):
    OPENAI_MODEL = open("openai_model.txt", "r").read().strip()
