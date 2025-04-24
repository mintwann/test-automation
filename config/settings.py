import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
WAIT_TIME = int(os.getenv("WAIT_TIME", 10))
