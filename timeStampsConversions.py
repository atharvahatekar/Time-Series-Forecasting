import pandas as pd
from datetime import datetime, timedelta

def ordinal_to_timestamp(value):

    # Separate the integer part and the fractional part
    ordinal_date = int(value)
    fractional_day = value - ordinal_date

    base_date = datetime(1900, 1, 1)
    dt_date = base_date + timedelta(days=ordinal_date - 1)

    seconds_in_day = fractional_day * 24 * 3600
    dt_time = timedelta(seconds=seconds_in_day)

    timestamp = dt_date + dt_time
    timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    return timestamp


def timestamp_to_ordinal(timestamp_str):

    dt = datetime.strptime(str(timestamp_str), '%Y-%m-%d %H:%M:%S')
    start_date = datetime(1900, 1, 1)
    delta = dt - start_date
    fractional_day = (dt.hour + dt.minute / 60 + dt.second / 3600) / 24
    ordinal = delta.days + fractional_day
    return ordinal