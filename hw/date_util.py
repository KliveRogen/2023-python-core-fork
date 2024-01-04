from datetime import datetime


def parse_date(string_date) -> datetime:
    return datetime.strptime(string_date, '%Y-%m-%d')
