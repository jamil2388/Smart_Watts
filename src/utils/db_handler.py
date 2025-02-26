from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBHandler:
    """Handles MongoDB connection and data insertion."""
    def __init__(self, host = "localhost", port = 27017, db_name="IoTData", collection_name="SensorReadings"):

        self.timeout = 5000

        try:
            self.client = MongoClient(host, port, serverSelectionTimeoutMS=self.timeout)
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_data(self, data):
        """Inserts sensor data into MongoDB collection."""
        print(f"insert one -> \n{data}\n")
        self.collection.insert_one(data)