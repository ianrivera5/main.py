# Ian Rivera
"""This is the docstring of this assignment.

    It describes what this code does and its meaning."""
# Integration of what I have learned about programming.
# My program is based on my current job as a tennis instructor
# /court maintenance to help me manage my work and keep track of my supplies.
# Hackerrank.com was used as source.
# Introduction/Greetings
print("Hello Everyone!")
print("Welcome to my Integration Project!")
print("This is to", end=' ')
print("keep track of my work.")
# Name of company I work for
print("@BlackWoodTennis")
print("My weekly court grooming tasks")
# There are five courts that need maintenance five days a week, this determines
# how much is done in a month
print(5 * 5)
# Determines how many times in a month I scarify each court
print(5 ** 2)
# Remainder to raise net
court = 1
print("Raise the net for court", court)
# There are 110 net holders and 10 are used for all five courts
print(110 - 10 * 5)
# The remaining net holders are divided by 5 to determine how much each court
# gets the leftovers
print(60 / 5)
# The 12 net holders in each court are divided to see how many remain in each
# court
print(12 // 5)
# The remaining 2 net holders in each court by 5
print(5 % 2)
# An important reminder that sometimes is forgotten
print(
    "Remember" + " " + "to" + " " + "check" + " " + "the" + " " +
    "windscreens" + '.')
# This is the code to a storage room
print(1 + 3 + 1 + 5)
# Code for storage shed
print('1', '9', '5', '4', sep='')
# Monthly date to clean nets
print('09', '29', '2021', sep='-')
# Remainder that low end of courts has drains
a = "Low end " + "has drains"
print(a)
# Technique for scarifying courts using a rake
a = "up down " * 5
print(a)
# There are 50 total balls in a lesson and 30 are normally used
print(50 - 30)
# Describes that only mixed gas is used for leaf blower
print("Mixed gas", "Leaf blower", sep='==')
# Important back and forth direction when rolling tennis lines
tech = "left right " * 5
print(tech)
# These courts are only used for lessons
print("Court 1\nCourt 2\nCourt 5")
# How many gallons of gas are used monthly + gallons of pesticide used monthly
print(5 * 2 + 5)
# Tells me which days I have Lessons
print("Lessons", end=' only on ')
print("Tuesday and Thursday")
# Helps me determine how many gallons of gas are left in container used for
# golf cart/Enter #5
redContainer = '5 Gallons'
print(redContainer)
# Tells me to only wash pickle ball courts
string = input("Pickle ball courts can only be washed")
print(string)
# Start of sprint 2
# There are 50 clay bags in a shed and 50 bags outside beside the shed
bags = 50
outside_bags = 50
bags += outside_bags
print(bags)
# tells me that there is 5 tennis courts and only 2 pickle ball courts,
# not the same amount
tennis_court = 5
pickle_ball = 2
print(tennis_court == pickle_ball)
# there is supposed to be 50 balls in each court, determining how much in total
balls = 50
courts = 5
balls *= courts
print(balls)
# Explains there are more tennis courts on location
tennis = 5
ball = 4
if tennis > ball:
    print("More tennis courts on site")
# If the gas container has 5 gallons, there is no need for gas,
# if equal, I wait for my boss, if less, I must call my boss for more
gas_container = 5
call = 1
if gas_container > call:
    print("No need for more gas")
elif gas_container == call:
    print("Wait for Nick")
else:
    print("Call Nick for more gas")


# The days of week that I must clean the shoe washers
def clean_shoe(name):
    """

    :param name:
    """
    print(name + " clean shoe washer")


clean_shoe("Tuesday")
clean_shoe("Friday")
clean_shoe("Saturday")
# One location that I work only has 3 courts and the other location only has
# five
hammock_bay = 3
reserve = 5
print(hammock_bay != reserve)
# There are more tennis nets in the Naples reserve location
nets_reserve = 9
nets_hammock = 3
print(nets_reserve < nets_hammock)
# There are only seven windscreens on a court
windscreens = 7
if not windscreens > 10:
    print('True')
else:
    print('False')
# There are only 4 pickle ball nets, no less or more
p_nets, courts = 4, 4
print(p_nets and courts)
# There are only 5 exact tennis courts
tennis_nets = 5
print(tennis_nets > 3 or tennis_nets < 4)
# This tells me how many times I go to Naples Reserve/Hammock Bay location
# in a week
reserve = 0
while reserve < 3:
    print('Naples Reserve')
    reserve += 1
else:
    print("Hammock Bay")
# The three locations I work in listed
locations = ["Naples Reserve", "Hammock Bay", "The Dunes"]
for places in locations:
    print(places)
# Determines how many lessons I have in a week
lessons = range(12)
for student in lessons:
    print(student)


# The days that I rake the courts
def rake(name):
    """

    :param name:
    """
    print(name + " Rake")


rake("Tuesday")
rake("Thursday")
rake("Friday")

# numbers represent the daily tasks I have to do, number of tasks depends on
# size of location, if less than 10, day off
work = int(input("Enter Number: "))
if work >= 20:
    print("Go to Hammock Bay")
elif 20 > work >= 15:
    print("Go to Naples Reserve")
elif 15 > work >= 10:
    print("Go to The Dunes")
else:
    print("It's my day off")
