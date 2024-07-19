from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environment.get("DB_HOST")