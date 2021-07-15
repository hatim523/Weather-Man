import pandas as pd

from abstract_reader import AbstractReader


class TSVReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self):
        try:
            self.file_data = pd.read_csv(self.filename, sep='\t')
        except Exception as e:
            print(str(e))
