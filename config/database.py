import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def get_mongo_uri():
    db_password = os.getenv("DB_PASSWORD")
    db_username = os.getenv("DB_USERNAME")
    db_host = os.getenv("DB_HOST")
    db_cluster_name = os.getenv("DB_CLUSTER_NAME")
    if not db_password or not db_username or not db_host or not db_cluster_name:
        raise Exception(
            "Database credentials not found. Please set DB_USERNAME, DB_PASSWORD, DB_HOST, DB_CLUSTER_NAME environment variables."
        )
    return f"mongodb+srv://{db_username}:{db_password}@{db_host}/?retryWrites=true&w=majority&appName={db_cluster_name}"


def get_mongo_client():
    mongo_uri = get_mongo_uri()
    return MongoClient(mongo_uri)
