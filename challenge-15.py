"""
Python Challenge Level 15.

The page title is 'whom?' and the image is a calendar of January 1??6 with Monday
Jan 26th circled. There are two comments in the page source, 'he ain't the
youngest, he is the second' and 'todo: buy flowers for tomorrow'.
"""
import calendar
import datetime

GREGORIAN_CALENDAR_START = 1582


def ends_in_6(year):
    """
    Does the year end in '6'?
    """
    return year % 10 == 6


def jan_26th_is_monday(year):
    """
    In this year, is January 26th a monday?
    """
    return calendar.weekday(year, 1, 26) == 0

matching_years = []
for year in range(GREGORIAN_CALENDAR_START, 2000):
    # Determine the years which could match the calendar conditions:
    if jan_26th_is_monday(year) and calendar.isleap(year) and ends_in_6(year):
        matching_years.append(year)

# 'he ain't the youngest, he is the second' - take the second youngest year
year = matching_years[-2]

# 'todo: buy flowers for tomorrow
print(datetime.date(year, 1, 26 + 1))
# '1756-01-27', which is Mozart's birthday
# http://www.pythonchallenge.com/pc/return/mozart.html is the next URL.
