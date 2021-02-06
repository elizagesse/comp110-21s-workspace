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

percent: float = float(target_percent / population)
people_needed: float = float(float(percent) * population)
people_done: float = float(doses_administered * float(.5))
people_left: int = round(float(people_needed) - float(people_done))
doses_needed: int = int(people_left * 2)
days: int = int(doses_needed / doses_day)


today: datetime = datetime.today()
days_left: timedelta = timedelta(days)

days_converted: str = str(doses_needed / doses_day)
percent_converted: str = str(target_percent)
first = "We will reach "
second = "% "
third = "vaccination in "
fourth = " days, which falls on "


print((today + days_left).strftime("%B %d, %Y"))

print(first + percent_converted + second + third + days_converted + fourth + (today + days_left).strftime("%B %d, %Y"))