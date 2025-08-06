import logfire
from dotenv import load_dotenv
import os

load_dotenv()

def setup_logging():
    api_key = os.getenv("LOGFIRE_API_KEY", None)
    if not api_key:
        raise ValueError("LOGFIRE_API_KEY environment variable is not set")
    logfire.configure(token=api_key)
    return logfire

logger = setup_logging()