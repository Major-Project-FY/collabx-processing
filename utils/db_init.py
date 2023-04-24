from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv('DEV_SECONDARY_DB_URI')

client = MongoClient(connection_string)

db = client['test']
gh_info = db['user github infos']
repo_info = db['user repos']
