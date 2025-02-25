import time
from src.iot.ac import AC
from src.iot.refrigerator import Refrigerator
from src.utils.db_handler import MongoDBHandler

def simulate_devices(devices, db_handler, duration=10, interval=2):
    """Simulates real-time power readings and stores them in MongoDB."""
    start_time = time.time()
    while time.time() - start_time < duration:
        for device in devices:
            data = device.get_data()
            db_handler.insert_data(data)
            print("Inserted:", data)
        time.sleep(interval)

if __name__ == "__main__":
    db_handler = MongoDBHandler()
    devices = [AC(), Refrigerator()]
    simulate_devices(devices, db_handler, duration=10, interval=2)
