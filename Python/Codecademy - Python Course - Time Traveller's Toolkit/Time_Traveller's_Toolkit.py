import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from Custom_Module import generate_time_travel_message

# print(dt.date.today())
# print(dt.datetime.now().time())

# Base cost of travel per year, can be altered to whatever value
travel_base_cost = Decimal(1000.00)

# Retrieves the current year, and a random year either forwards or backwards in time,
# The random year is then subtracted from the base year, and then converted with abs()
# This makes it so the number is positive no matter what
current_year = dt.datetime.now().year
random_year = randint(1, 9999)
# print(random_year)
year_difference = current_year - random_year
year_difference = abs(year_difference)

# The year difference is then multiplied with the base travel cost, and rounded to 2 decimal places
# This is to account for any "cents" or "pence" in the price, like 1.50 per year etc.
total_travel_cost = Decimal(travel_base_cost) * Decimal(year_difference)
total_travel_cost = round(total_travel_cost, 2)
# print(total_travel_cost)

# A list of destinations which can be expanded or appended if need be
destination_list = ["Madrid", "London", "Los Angeles", "Chongqing"]

destination_choice = choice(destination_list)
# print(destination_choice)

# MESSAGE

print(generate_time_travel_message(random_year, destination_choice, total_travel_cost))
if total_travel_cost > 2000000:
  print("Time travel is expensive you know.")