import time
import random

class IoTDevice:
    """Base class for IoT devices that generate power consumption data."""
    def __init__(self, name, min_power, max_power):
        self.name = name
        self.min_power = min_power
        self.max_power = max_power

    def generate_power_consumption(self):
        """Simulates power consumption reading in watts."""
        return round(random.uniform(self.min_power, self.max_power), 2)

    def get_data(self):
        """Returns a simulated sensor reading with timestamp."""
        return {
            "device": self.name,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "power_consumption_watts": self.generate_power_consumption()
        }
