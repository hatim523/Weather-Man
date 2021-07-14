import datetime
from typing import List, Union

from helpers import read_float_value
from weather_data_class import Weather


class AbstractReader:
    """
    Currently supports reading of files with following extensions:
        ♦ tsv
        ♦ txt
        ♦ xlsx
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.file_data = None
        self.weather_data = []

    def read_file(self) -> tuple:
        raise NotImplementedError

    def get_data(self) -> List[Weather]:
        return self.weather_data

    def map_data(self, row_data: Union[list, tuple]):
        try:
            self.weather_data.append(Weather(
                date=datetime.datetime.strptime(row_data[0], "%Y-%m-%d").date(),
                max_temp=read_float_value(row_data[1]),
                mean_temp=read_float_value(row_data[2]),
                min_temp=read_float_value(row_data[3]),
                dew_point_c=read_float_value(row_data[4]),
                mean_dew_point_c=read_float_value(row_data[5]),
                min_dew_point_c=read_float_value(row_data[6]),
                max_humidity=read_float_value(row_data[7]),
                mean_humidity=read_float_value(row_data[8]),
                min_humidity=read_float_value(row_data[9]),
                max_sea_lvl_pressure=read_float_value(row_data[10]),
                mean_sea_lvl_pressure=read_float_value(row_data[11]),
                min_sea_lvl_pressure=read_float_value(row_data[12]),
                max_visibility=read_float_value(row_data[13]),
                mean_visibility=read_float_value(row_data[14]),
                min_visibility=read_float_value(row_data[15]),
                max_wind_speed=read_float_value(row_data[16]),
                mean_wind_speed=read_float_value(row_data[17]),
                max_gust_speed=read_float_value(row_data[18]),
                precipitation=read_float_value(row_data[19]),
                cloud_cover=read_float_value(row_data[20]),
                events=row_data[21],
                wind_dir=read_float_value(row_data[22])
            ))
        except Exception as e:
            pass
            # print("Exception in map_data: ", str(e))


