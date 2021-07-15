import sys
import getopt

from weather_man import WeatherMan

weather_man = WeatherMan()
usage_text = "usage: main.py /path/to/files -e <year> -a <year/month> -c <year/month>"

try:
    if len(sys.argv) < 4:
        print(usage_text)
        sys.exit(1)

    file_directory = sys.argv[1]
    print(file_directory)
    # print(sys.argv[2:])
    opts, args = getopt.getopt(sys.argv[2:],"a:c:e:h")
    print(opts)
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

