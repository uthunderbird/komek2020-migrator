from datetime import datetime


# Datetime sample:
# 05.07.2020 18:24:24

# Read about format here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
FORMAT = '%d.%m.%Y %H:%M:%S'


def convert_datetime(str_date):
    return datetime.strptime(str_date, FORMAT)
