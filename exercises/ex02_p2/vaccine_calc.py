"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730386298"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
  
    # TODO 2: Call days_to_target and store result in a variable.
    x = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    y = future_date(x)
    # TODO 5: Print the expected output using the variables above.
    first = "We will reach "
    second = "% vaccination in "
    third = " days, which falls on "
    days_updated: str = str(x)
    percent_updated: str = str(target)
    print(first + percent_updated + second + days_updated + third + y)

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    percent: float = float(target / 100)
    people_total: float = float(percent * population)
    people_given: int = int(.5 * doses)
    people_left: int = int(people_total - people_given)
    doses_needed: int = int(people_left * 2)
    days: int = round(doses_needed / doses_per_day)
    return days
    


# TODO 3: Define future_date function
def future_date(days_out: int) -> str:
    today: datetime = datetime.today()
    days_left: timedelta = timedelta(days_out)
    future: datetime = today + days_left
    final: str = future.strftime("%B %d, %Y")
    return final
    


if __name__ == "__main__":
    main()
