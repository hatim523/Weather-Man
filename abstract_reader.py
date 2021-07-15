import pandas as pd


class AbstractReader:
    """
    Currently supports reading of files with following extensions:
        ♦ tsv
        ♦ csv
        ♦ txt
        ♦ xlsx
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.file_data = None

    def read_file(self):
        raise NotImplementedError


