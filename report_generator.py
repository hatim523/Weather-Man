from weather_calc import WeatherCalculator


class ReportGenerator:
    def __init__(self, weather_calc: WeatherCalculator):
        self.weather_calculator = weather_calc

    def generate_e_report(self):
        highest_temp = self.weather_calculator.calculate_highest_temperature()
        lowest_temp = self.weather_calculator.calculate_lowest_temperature()
        humidity = self.weather_calculator.calculate_highest_humidity()

        print(f"Highest: {highest_temp['value']}C on {highest_temp['date'].strftime('%B %d')}")
        print(f"Lowest: {lowest_temp['value']}C on {lowest_temp['date'].strftime('%B %d')}")
        print(f"Humidity: {humidity['value']}% on {humidity['date'].strftime('%B %d')}")

    def generate_a_report(self):
        pass