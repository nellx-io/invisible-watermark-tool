from dotenv import load_dotenv
import os

# Load environment variables from .env file in project root
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Pull variables from the loaded environment
CREATOR_ID = os.getenv("CREATOR_ID")
SECRET_KEY = os.getenv("SECRET_KEY")

# Safety check
if not CREATOR_ID or not SECRET_KEY:
    raise ValueError("Missing CREATOR_ID or SECRET_KEY in .env file.")
