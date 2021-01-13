# Day 2: 30 Days of python programming

first_name= "Harry"
last_name = "Potter"
full_name = first_name+''+last_name
country = "Briten"
city = "UK"
age = 14
year = 2000
is_married = "No"
is_true = False
is_light_on = True
fname,lname,age = "Emma","Watson",16

type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)

print(len(first_name))

print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
variable_total = num_one + num_two
print(variable_total)

variable_diff = num_two - num_one
print(variable_diff)

variable_product = num_two * num_one
print(variable_product)

variable_division =  num_one / num_two
print(variable_division)

variable_reminder = num_two % num_one
print(variable_reminder)

variable_exp = num_one ** num_two
print(variable_exp)

variable_floor_division = num_one // num_two
print(variable_floor_division)


firstName = input("Enter your firstName: ")
print(firstName)
lastName = input("Enter your lastName: ")
print(lastName)
countryName = input("Enter your country name: ")
print(countryName)
yourAge = input("Enter your age: ")
print(yourAge)

help('keywords')

from math import pi
r = float(input("Input the radius of circule: "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("Circumference of the circle is : %.2f" % circumference)
