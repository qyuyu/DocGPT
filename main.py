# python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()

print("this comes from .env: ",os.getenv('MY_API_KEY'))