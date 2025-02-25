from pymongo import MongoClient

class MongoDBHandler:
    """Handles MongoDB connection and data insertion."""
    def __init__(self, db_name="IoTData", collection_name="SensorReadings"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        """Inserts sensor data into MongoDB collection."""
        self.collection.insert_one(data)