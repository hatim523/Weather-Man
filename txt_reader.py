from abstract_reader import AbstractReader


class TxtReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self) -> bool:
        try:
            self.file_data = open(self.filename).read()
            self.__process_file__()
            return True
        except Exception as e:
            print(str(e))
            return False

    def __process_file__(self):
        rows = self.file_data.split("\n")

        # removing first row which is header
        rows.pop(0)

        # now processing all rows
        for row in rows:
            self.map_data(row.split(","))
