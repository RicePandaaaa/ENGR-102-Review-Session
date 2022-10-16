"""
Write a program that will ask a user to enter names and ages of people, stopping when an age of 0 is entered
(and not processing that person). The program should collect this information, and then output the average
age, the name of the oldest person, and the name of the youngest person. Assume no two people have the
same age.
"""

"""
Dictionaries Crash Course

d = {}

To add...

d[key] = value
d["Name"] = "Anthony" # d = {"Name": "Anthony"}

If you want all the keys or all the values
.keys() and .values()

# NOT LISTS
d.keys() -> dict_keys(["Name"])
d.values() -> dict_values(["Anthony"])

to make them lists...
keys = list(d.keys()) -> ["Name"]
values = list(d.values()) -> ["Anthony"]
"""

# Storing data
people = {}

# Loop until I get an age of 0
age = int(input("Enter your age: "))

while age != 0:
    # Ask for the name
    name = input("Enter your name: ")

    # Add to people
    people[age] = name

    # Ask again for the age
    age = int(input("Enter your age: "))

# Calculate the average
ages = list(people.keys())
average = "N/A"

# If there are people, calculate the average
if len(ages) > 0:
    average = sum(ages) / len(ages)

# Find the oldest and youngest people
ages.sort()
youngest_name = "N/A"
oldest_name = "N/A"

# If there are people
if len(ages) > 0:
    youngest_age = ages[0]
    oldest_age = ages[-1]

    youngest_name = people[youngest_age]
    oldest_name = people[oldest_age]

# Output
print(f"Average: {average}, Oldest: {oldest_name}, Youngest: {youngest_name}")