"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

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

percent: int = int(target_percent / population)
people_total: int = int(percent * population)
people_left: float = int(people_total - (.5 * doses_administered))
doses_needed: int = round(int(people_left * 2))
days: int = int(doses_day / doses_needed)

today: datetime = datetime.today()
days_left: timedelta = timedelta(days)
future: datetime = today + days_left
print(future.strftime("%B %d, %Y"))

