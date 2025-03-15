import os
from dotenv import load_dotenv

load_dotenv()

GET_IP_API_URL = os.getenv("GET_IP_API_URL")
LOCATOR_API_URL = os.getenv("LOCATOR_API_URL")
LOCATOR_API_TOKEN = os.getenv("LOCATOR_API_TOKEN")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
TIMEOUT = 60
