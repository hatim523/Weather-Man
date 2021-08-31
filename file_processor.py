import os
import re

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
        self.file_extension_regex = re.compile("^.*\.(tsv|txt|xlsx)$")

    def read_files(self) -> tuple:
        """
        Checks if the given directory exists and invokes relevant reader
        """
        if not os.path.exists(self.directory):
            return False, "Invalid location"

        self.weather_files = [f for f in os.listdir(self.directory) if
                              os.path.isfile(os.path.join(self.directory, f))
                              and self.file_extension_regex.match(f) is not None]

        if not self.weather_files:
            return False, f"No files found in the directory: {self.directory}"

        self.__process_files()
        return True, None

    def __process_files(self):
        """
        Invokes relevant reader class based on file extension
        """
        for file in self.weather_files:
            file_reader = self.__get_file_reader__(os.path.join(self.directory,
                                                                file))

            if file_reader is None:
                print(f"File: {file} cannot be read. "
                      f"Extension currently not supported.")
                continue

            status, details = file_reader.read_file()
            if not status:
                print(details)

            self.weather_man.add_new_data(file_reader.get_data())

    def __get_file_reader__(self, filename: str) -> AbstractReader:
        """
        Returns a reader based on file extension
        """
        if filename.endswith(".tsv"):
            return TSVReader(filename)
        elif filename.endswith(".txt"):
            return TxtReader(filename)
        elif filename.endswith(".xlsx"):
            return XLSXReader(filename)
