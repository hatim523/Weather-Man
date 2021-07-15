from typing import List

from weather_data_class import Weather


class WeatherMan:
    def __init__(self):
        self.weather_data = []

    def add_new_data(self, data: List[Weather]):
        self.weather_data += data



