from abstract_reader import AbstractReader
import openpyxl


class XLSXReader(AbstractReader):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_file(self):
        try:
            self.__xlsx_reader__()
            self.__process_file__()
            return True
        except Exception as e:
            print(str(e))
            return False

    def __xlsx_reader__(self):
        """
        Implementation copied from stackoverflow:
        Ref: https://stackoverflow.com/questions/35744613/read-in-xlsx-with-csv-module-in-python/59973648#59973648
        """
        wb = openpyxl.load_workbook(self.filename)
        ws = wb.active

        self.file_data = []
        for row in ws.iter_rows(values_only=True):
            self.file_data.append(row)

    def __process_file__(self):
        """
        file_data: format -> [ ('2016-5-1', '27', '21', '15', '9', '3', '-1', '22', '19', '15', None, None, None,
                                '10.0', '7.0', '4.0', '4', '2', None, '0.0', None, None, '-1') ]
        """

        # removing first row as it is header row
        self.file_data.pop(0)

        # now processing remaining rows
        for row in self.file_data:
            self.map_data(row)