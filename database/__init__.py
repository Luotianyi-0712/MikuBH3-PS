from __future__ import annotations
import pymongo
from database.create_db import MongoDBCreate
from database.save_data import SaveData
from game_server.resource import ResourceManager


class MongoDBConnection:
    def __init__(self, host="localhost", port=27017, db_name="mikubh3"):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            ResourceManager.instance().load_resources()
            self.client = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/")
            if self.db_name:
                self.db = self.client[self.db_name]
                databases = self.client.list_database_names()
                if self.db_name not in databases:
                    print("Database not found. Will create one")
                    MongoDBCreate(self)
                print("Connected to MongoDB successfully!")
            else:
                print("No database selected.")
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB: %s" % e)

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed.")

    def get_collection(self, collection_name):
        if self.db is not None:
            return self.db[collection_name]
        else:
            print("No database selected. Connect to a database first.")
            return None

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                result = collection.insert_one(document)
                print(f"Document inserted successfully with id:{result.inserted_id}")
            except Exception as e:
                print(f"Error inserting document:{e}")

    def find_documents(self, collection_name, query={}):
        collection = self.get_collection(collection_name)
        if collection is not None:
            return collection.find(query)
        else:
            print("Collection not found.")
            return None
        
    def find_documents_by_key_values(self, collection_name, key_values):
        collection = self.get_collection(collection_name)
        if collection is not None:
            query = {key: value for key, value in key_values.items()}
            return collection.find(query)
        else:
            print("Collection not found.")
            return None

    def update_document(self, collection_name, filter_query, update_query):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                result = collection.update_one(filter_query, update_query)
                print(f"Document updated successfully:{result.modified_count}")
            except Exception as e:
                print(f"Error updating document:{e}")

    def delete_document(self, collection_name, filter_query):
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                result = collection.delete_one(filter_query)
                print(f"Document deleted successfully:{result.deleted_count} document(s) deleted.")
            except Exception as e:
                print(f"Error deleting document:{e}")

    def save(self,session,data_type,ids=[0]):
        save_data = SaveData(self,session,data_type,ids)
        save_data.save()
        
mongo = MongoDBConnection()
mongo.connect()