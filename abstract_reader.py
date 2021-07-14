import pandas as pd


class AbstractReader:
    def __init__(self, filename: str):
        self.filename = filename
        self.file_data = None

    def read_file(self) -> pd.DataFrame:
        raise NotImplementedError


