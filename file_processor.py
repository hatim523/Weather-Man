import os

from abstract_reader import AbstractReader
from tsv_reader import TSVReader
from txt_reader import TxtReader
from weather_man import WeatherMan
from xlsx_reader import XLSXReader


class FileProcessor:
    def __init__(self, directory_location: str):
        self.directory = directory_location
        self.weather_files = None

        self.weather_man = WeatherMan()

    def read_files(self) -> tuple:
        """

        :rtype: object
        """
        if not os.path.exists(self.directory):
            return False, "Invalid location"

        self.weather_files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and
                         (f.endswith(".tsv") or f.endswith(".txt") or f.endswith(".xlsx"))]

        if not self.weather_files:
            return False, f"No files found in the directory: {self.directory}"

        self.__process_files()
        return True, None

    def __process_files(self):
        for file in self.weather_files:
            file_reader = self.__get_file_reader(file)

            if file_reader is None:
                print(f"File: {file} cannot be read. Extension currently not supported.")
                continue

            file_reader.read_file()
            self.weather_man.add_new_data(file_reader.get_data())


    def __get_file_reader(self, filename: str) -> AbstractReader:
        if filename.endswith(".tsv"):
            return TSVReader(filename)
        elif filename.endswith(".txt"):
            return TxtReader(filename)
        elif filename.endswith(".xlsx"):
            return XLSXReader(filename)