import pandas as pd

from abstract_reader import AbstractReader


class XLSXReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self) -> pd.DataFrame:
        try:
            self.file_data = pd.read_excel(self.filename)
            return self.file_data
        except Exception as e:
            print(str(e))