import datetime
from dataclasses import dataclass


@dataclass
class Weather:
    date: datetime.date
    max_temp: float
    mean_temp: float
    min_temp: float
    dew_point_c: float
    mean_dew_point_c: float
    min_dew_point_c: float
    max_humidity: float
    mean_humidity: float
    min_humidity: float
    max_sea_lvl_pressure: float
    mean_sea_lvl_pressure: float
    min_sea_lvl_pressure: float
    max_visibility: float
    mean_visibility: float
    min_visibility: float
    max_wind_speed: float
    mean_wind_speed: float
    max_gust_speed: float
    precipitation: float
    cloud_cover:  float
    events: str
    wind_dir: float
