from typing import List

from weather_calc import WeatherCalculator
from weather_data_class import Weather


class WeatherMan:
    def __init__(self):
        self.weather_data = []

    def add_new_data(self, data: List[Weather]):
        self.weather_data += data

    def filter_data(self, year, month=None) -> WeatherCalculator:
        if month is not None:
            return self.__filter_data_by_year_and_month(year, month)

        return self.__filter_data_by_year__(year)

    def __filter_data_by_year__(self, year):
        year = int(year)
        filtered_data = []
        for data in self.weather_data:
            if data.date.year == year:
                filtered_data.append(data)
        return WeatherCalculator(filtered_data, year=year)

    def __filter_data_by_year_and_month(self, year, month):
        year = int(year)
        month = int(month)

        filtered_data = []
        for data in self.weather_data:
            if data.date.year == year and data.date.month == month:
                filtered_data.append(data)

        return WeatherCalculator(filtered_data, year=year, month=month)

