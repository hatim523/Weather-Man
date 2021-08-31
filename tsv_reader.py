import csv

from abstract_reader import AbstractReader


class TSVReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self) -> tuple:
        try:
            tsv_file = open(self.filename)
            read_tsv = csv.reader(tsv_file, delimiter='\t')

            self.file_data = [row for row in read_tsv]
            self.__process_file()
            return True, None
        except FileNotFoundError as e:
            return False, str(e)

    def __process_file(self):
        for row in self.file_data:
            self.map_data(row)
