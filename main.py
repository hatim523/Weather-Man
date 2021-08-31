import sys
import getopt

from file_processor import FileProcessor
from helpers import get_year_and_month_from_input
from report_generator import ReportGenerator

usage_text = "usage: main.py /path/to/files -e <year> " \
             "-a <year/month> -c <year/month>"

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

    weather_man = file_processor.weather_man
    opts, args = getopt.getopt(sys.argv[2:], "a:c:e:h")

    for opt, arg in opts:
        if opt == '-a':
            year, month = get_year_and_month_from_input(arg)
            calculator = weather_man.filter_data(year=year, month=month)
            report_generator = ReportGenerator(calculator)
            report_generator.generate_a_report()
        elif opt == '-e':
            calculator = weather_man.filter_data(year=arg)
            report_generator = ReportGenerator(calculator)
            report_generator.generate_e_report()
        elif opt == '-c':
            year, month = get_year_and_month_from_input(arg)
            calculator = weather_man.filter_data(year=year, month=month)
            report_generator = ReportGenerator(calculator)
            report_generator.generate_c_report()
        elif opt == '-h':
            print(usage_text)
            sys.exit(0)

except getopt.GetoptError:
    print(usage_text)
    sys.exit(2)
