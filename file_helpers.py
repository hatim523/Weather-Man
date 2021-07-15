import os
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile


def extract_files(file_location, extract_location) -> tuple:
    try:
        with ZipFile(file_location, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(extract_location)
        return True, None
    except Exception as e:
        return False, str(e)


def read_files(location: str) -> tuple:
    if not os.path.exists(location):
        return False, "Invalid location"

    weather_files = [f for f in listdir(location) if isfile(join(location, f)) and
                 (f.endswith(".tsv") or f.endswith(".txt") or f.endswith(".xlsx"))]

    if not weather_files:
        return False, f"No files found in the directory: {location}"
    return True, weather_files
