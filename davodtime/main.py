#!/usr/bin/env python3

import sys
from datetime import datetime
import pytz

def format_time(dt):
    return dt.strftime('%m%d%Y-%H%M%S')

def get_time_for_timezone(tz_name):
    try:
        tz = pytz.timezone(tz_name)
        return format_time(datetime.now(tz))
    except pytz.UnknownTimeZoneError:
        return f"Unknown timezone: {tz_name}"

def main():
    if len(sys.argv) == 1:
        # No arguments, return local system time
        print(format_time(datetime.now()))
    else:
        arg = sys.argv[1].lower()
        if arg == "utc":
            print(format_time(datetime.utcnow()))
        else:
            print(get_time_for_timezone(arg.upper()))

if __name__ == "__main__":
    main()