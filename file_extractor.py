from zipfile import ZipFile


def extract_files(file_location, extract_location) -> tuple:
    try:
        with ZipFile(file_location, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            zipObj.extractall(extract_location)
        return True, None
    except Exception as e:
        return False, str(e)
