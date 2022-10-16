"""
Write a program that will ask a user to enter names and ages of people, stopping when an age of 0 is entered
(and not processing that person). The program should collect this information, and then output the average
age, the name of the oldest person, and the name of the youngest person. Assume no two people have the
same age.
"""

"""
Speedrun Crash Course of Dictionaries

d = {}

if I want to add to a dictionary

d[key] = value

inside d: {key: value}

My keys will be the ages, the values will be the names

Getting all the keys and all the values
.keys()
.values()

d = {"Frodo": "Best Doggo"}
keys = d.keys()  # ["Frodo"]
WRONG
keys[0]
RIGHT
list(keys)[0]  # Gets you "Frodo"
"""

# Storage
people = {}

# Grab input
age = int(input("Enter your age: "))
while age != 0:
    # Ask for name
    name = input("Enter your name: ")

    # Add to people
    people[age] = name

    # Keep asking
    age = int(input("Enter your age: "))

# Getting the averages
ages = list(people.keys())
average = -1

if len(ages) != 0:
    average = sum(ages) / len(ages)

# Sorting people
ages.sort()
youngest_person = ages[0]
oldest_person = ages[-1]


# Output
print(f"Average: {average}, Oldest: {people[oldest_person]}, Youngest: {people[youngest_person]}")

"""
ages = [1, 2, 7, 4]
names = ["a", "b", "c", "d"]

loop through and find min and max
oldest is 7, youngest is 1
loop through again and get their indices
1 is at index 0
7 is at index 2
so...
the names you need are names[0] and names[2]
"""