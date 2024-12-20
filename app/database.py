from pymongo import MongoClient

client = MongoClient('mongodb://binit:binit@localhost:27017/') #DATABASE_URL for docker setup
db = client['binit_fastapi'] #DATABSE_NAME
