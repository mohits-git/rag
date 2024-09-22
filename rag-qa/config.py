import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
