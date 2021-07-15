import sys
import getopt

from file_processor import FileProcessor
from weather_man import WeatherMan

usage_text = "usage: main.py /path/to/files -e <year> -a <year/month> -c <year/month>"

try:
    if len(sys.argv) < 4:
        print(usage_text)
        sys.exit(1)

    file_directory = sys.argv[1]
    # reading and processing all files in given directory
    file_processor = FileProcessor(file_directory)
    status, details = file_processor.read_files()
    if not status:
        print(details)
        sys.exit(1)

    opts, args = getopt.getopt(sys.argv[2:],"a:c:e:h")

    for opt, arg in opts:
        if opt == '-a':
            """TODO"""
        elif opt == '-e':
            """TODO"""
        elif opt == '-c':
            """TODO"""
        elif opt == '-h':
            print(usage_text)
            sys.exit(0)

except getopt.GetoptError:
    print(usage_text)
    sys.exit(2)

