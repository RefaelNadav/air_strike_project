
class Target:
    def __init__(self, city_name: str, priority: int, location: dict, weather: dict):
        self.city_name = city_name
        self.priority = priority
        self.location = location
        self.weather = weather