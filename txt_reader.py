from abstract_reader import AbstractReader


class TxtReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self) -> tuple:
        try:
            self.file_data = open(self.filename).read()
            self.__process_file__()
            return True, None
        except Exception as e:
            return False, str(e)

    def __process_file__(self):
        rows = self.file_data.split("\n")

        # removing first row which is header
        rows.pop(0)

        # now processing all rows
        for row in rows:
            self.map_data(row.split(","))
