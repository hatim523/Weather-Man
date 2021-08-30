import datetime
from typing import List

from helpers import get_max_value_with_date, get_min_value_with_date
from weather_data_class import Weather


class WeatherCalculator:
    """
    Calculates metrics given filtered data
    """

    def __init__(self, filtered_data: List[Weather], year,
                 month=None, include_none=False):
        self.include_none_in_calculations = include_none
        self.data = filtered_data

        self.year = year
        self.month = month
        self.filtered_data_for = datetime.date(year=year,
                                               month=month if month is not None
                                               else 1,
                                               day=1)

        self.calculated_metrics = {}

        # key names
        self.highest_temperature = "highest_temp"
        self.lowest_temperature = "lowest_temp"
        self.humidity = "humidity"  # Assumption: Highest humidity
        self.avg_highest_temperature = "avg_highest_temp"
        self.avg_lowest_temperature = "avg_lowest_temp"
        self.avg_mean_humidity = "avg_mean_humidity"

    def calculate_highest_temperature(self):
        if self.highest_temperature in self.calculated_metrics:
            return self.calculated_metrics[self.highest_temperature]

        self.calculate_all_metrics()
        return self.calculate_highest_temperature()

    def calculate_lowest_temperature(self):
        if self.lowest_temperature in self.calculated_metrics:
            return self.calculated_metrics[self.lowest_temperature]

        self.calculate_all_metrics()
        return self.calculate_lowest_temperature()

    def calculate_highest_humidity(self):
        if self.humidity in self.calculated_metrics:
            return self.calculated_metrics[self.humidity]

        self.calculate_all_metrics()
        return self.calculate_highest_humidity()

    def calculate_avg_highest_temperature(self):
        if self.avg_highest_temperature in self.calculated_metrics:
            return self.calculated_metrics[self.avg_highest_temperature]

        self.calculate_all_metrics()
        return self.calculate_avg_highest_temperature()

    def calculate_avg_lowest_temperature(self):
        if self.avg_lowest_temperature in self.calculated_metrics:
            return self.calculated_metrics[self.avg_lowest_temperature]

        self.calculate_all_metrics()
        return self.calculate_avg_lowest_temperature()

    def calculate_avg_mean_humidity(self):
        if self.avg_mean_humidity in self.calculated_metrics:
            return self.calculated_metrics[self.avg_mean_humidity]

        self.calculate_all_metrics()
        return self.calculate_avg_mean_humidity()

    def get_divide_by_value(self, non_null_values):
        return len(self.data) if self.include_none_in_calculations else non_null_values

    def calculate_all_metrics(self):
        highest_humidity, highest_humidity_date = 0, None
        highest_temp, highest_temp_date = 0, None
        lowest_temp, lowest_temp_date = 999, None

        avg_highest_temp, non_null_highest_temp_values = 0, 0
        avg_lowest_temp, non_null_lowest_temp_values = 0, 0
        avg_mean_humidity, non_null_mean_humidity_values = 0, 0

        for weather in self.data:
            highest_humidity, highest_humidity_date = get_max_value_with_date(
                highest_humidity, highest_humidity_date,
                weather.max_humidity, weather.date)

            highest_temp, highest_temp_date = get_max_value_with_date(
                highest_temp, highest_temp_date, weather.max_temp,
                weather.date)

            lowest_temp, lowest_temp_date = get_min_value_with_date(
                lowest_temp, lowest_temp_date, weather.min_temp,
                weather.date)

            if weather.mean_humidity:
                avg_mean_humidity += weather.mean_humidity
                non_null_mean_humidity_values += 1

            if weather.max_temp:
                avg_highest_temp += weather.max_temp
                non_null_highest_temp_values += 1

            if weather.min_temp:
                avg_lowest_temp += weather.min_temp
                non_null_lowest_temp_values += 1

        self.calculated_metrics[self.highest_temperature] = \
            {"value": highest_temp, "date": highest_temp_date}
        self.calculated_metrics[self.lowest_temperature] = \
            {"value": lowest_temp, "date": lowest_temp_date}
        self.calculated_metrics[self.humidity] = \
            {"value": highest_humidity, "date": highest_humidity_date}

        self.calculated_metrics[self.avg_highest_temperature] = \
            avg_highest_temp / self.get_divide_by_value(non_null_highest_temp_values)

        self.calculated_metrics[self.avg_lowest_temperature] = \
            avg_lowest_temp / self.get_divide_by_value(non_null_lowest_temp_values)

        self.calculated_metrics[self.avg_mean_humidity] = \
            avg_mean_humidity / self.get_divide_by_value(non_null_mean_humidity_values)

    def get_temperature_values_for_day(self, day) -> tuple:
        for weather in self.data:
            if weather.date.day == day:
                return weather.max_temp, weather.min_temp
