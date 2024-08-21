import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")

headers = {
    'Accept': '*/*',
    'User-Agent': os.getenv("USERAGENT")
}