import pymongo
import dotenv
import os
dotenv.load_dotenv()


CONNECTION_STRING = f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@114.34.239.111/ofc-db"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client['ofc-db']

reports_collection = db['reports']

test_collection = db['test']

test_collection.insert_one({"test_key": "my_test_value"})