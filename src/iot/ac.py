from device import IoTDevice

class AC(IoTDevice):
    """Air Conditioner with fluctuating power consumption."""
    def __init__(self):
        super().__init__("Air Conditioner", 500, 1500)