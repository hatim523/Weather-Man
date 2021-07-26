from weather_calc import WeatherCalculator
from termcolor import colored


class ReportGenerator:
    def __init__(self, weather_calc: WeatherCalculator):
        self.weather_calculator = weather_calc

    def generate_e_report(self):
        if not self.weather_calculator.data:
            print("No data found for selected date.")
            return

        highest_temp = self.weather_calculator.calculate_highest_temperature()
        lowest_temp = self.weather_calculator.calculate_lowest_temperature()
        humidity = self.weather_calculator.calculate_highest_humidity()

        print(f"Highest: {highest_temp['value']}C on "
              f"{highest_temp['date'].strftime('%B %d')}")
        print(f"Lowest: {lowest_temp['value']}C on "
              f"{lowest_temp['date'].strftime('%B %d')}")
        print(f"Humidity: {humidity['value']}% on "
              f"{humidity['date'].strftime('%B %d')}")
        print()

    def generate_a_report(self):
        if not self.weather_calculator.data:
            print("No data found for selected date.")
            return

        avg_highest_temp = self.weather_calculator. \
            calculate_avg_highest_temperature()
        avg_lowest_temp = self.weather_calculator. \
            calculate_avg_lowest_temperature()
        avg_mean_humidity = self.weather_calculator. \
            calculate_avg_mean_humidity()

        print(f"Highest Average: {round(avg_highest_temp, 2)}C")
        print(f"Lowest Average: {round(avg_lowest_temp, 2)}C")
        print(f"Average Mean Humidity: {round(avg_mean_humidity, 2)}%")
        print()

    def generate_c_report(self):
        if not self.weather_calculator.data:
            print("No data found for selected date.")
            return

        print(self.weather_calculator.filtered_data_for.strftime("%B %Y"))
        for i in range(1, 32):
            temp_values = self.weather_calculator. \
                get_temperature_values_for_day(i)
            if temp_values is None:
                continue

            # if either value is None, skip that day
            if not (temp_values[0] and temp_values[1]):
                continue

            print(str(i).zfill(2), end=' ')

            highest_temp_repr = "+" * int(temp_values[0])
            lowest_temp_repr = "+" * int(temp_values[1])

            print(colored(highest_temp_repr, "red"), end=" ")
            print(int(temp_values[0]))

            print(str(i).zfill(2), end=' ')
            print(colored(lowest_temp_repr, "blue"), end=" ")
            print(int(temp_values[1]))
