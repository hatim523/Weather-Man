from zipfile import ZipFile


def extract_files(file_location, extract_location) -> tuple:
    try:
        with ZipFile(file_location, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(extract_location)
        return True, None
    except Exception as e:
        return False, str(e)


def read_float_value(value):
    try:
        return float(value)
    except:
        return None


def get_max_value(value_1, value_2):
    if value_1 is None:
        return value_2
    if value_2 is None:
        return value_1

    return value_1 if value_1 > value_2 else value_2


def get_min_value(value_1, value_2):
    if value_1 is None:
        return value_2
    if value_2 is None:
        return value_1

    return value_1 if value_1 < value_2 else value_2


def get_max_value_with_date(value_1, value_1_date, value_2, value_2_date):
    if value_1 is None:
        return value_2, value_2_date
    if value_2 is None:
        return value_1, value_1_date

    return (value_1, value_1_date) if value_1 > value_2 else (value_2, value_2_date)


def get_min_value_with_date(value_1, value_1_date, value_2, value_2_date):
    if value_1 is None:
        return value_2, value_2_date
    if value_2 is None:
        return value_1, value_1_date

    return (value_1, value_1_date) if value_1 < value_2 else (value_2, value_2_date)


def get_year_and_month_from_input(input_str: str):
    input_str = input_str.split("/")
    if len(input_str) != 2: raise Exception("Invalid input. Please enter input as <year/month>")

    return input_str[0], input_str[1]