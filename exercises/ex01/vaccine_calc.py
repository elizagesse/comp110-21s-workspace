"""A vaccination calculator."""

__author__ = "730386298"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinatied: "))

percent: float = float(target_percent / 100)
people_total: float = float(percent * population)
people_given: int = int(.5 * doses_administered)
people_left: int = int(people_total - people_given)
doses_needed: int = int(people_left * 2)
days: int = round(doses_needed / doses_day)

days_updated: str = str(days)
percent_updated: str = str(target_percent)
first = "We will reach "
second = "% vaccination in "
third = " days, which falls on "


today: datetime = datetime.today()
days_left: timedelta = timedelta(days)
future: datetime = today + days_left
print(first + percent_updated + second + days_updated + third + future.strftime("%B %d, %Y"))