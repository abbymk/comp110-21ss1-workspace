"""A vaccination calculator."""

__author__ = "730230918"

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
today: datetime = datetime.today()

fortnight: timedelta = timedelta(7+7)
mini_month: timedelta = timedelta (5+5+5)
future: datetime = today + mini_month



# Begin your solution here...
people_pop: str = input ( " Population: " )
people_pop_int: int = int(people_pop)

dose_administered: str = input ( " Doses administered: " )
dose_administered_int: int = int(dose_administered)

dose_per_day: str = input ( " Doses per day: " )
dose_per_day_int: int = int(dose_per_day)

target_percent: str = input ( "Target percent vaccinated: " )
target_percent_int: int = int(target_percent)
target_percent_float: float = float(target_percent_int)
target_percent_int: int = round(target_percent_float)



print("We will reach " + target_percent + "% vaccination in 25 days, which falls on " + future.strftime("%B %d, %Y") + ". " )
