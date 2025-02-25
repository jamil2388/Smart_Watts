from device import IoTDevice


class Refrigerator(IoTDevice):
    """Refrigerator with periodic cycling power consumption."""
    def __init__(self):
        super().__init__("Refrigerator", 100, 400)