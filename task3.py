#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math

a = input("what is a? ")
b = input("what is b? ")
c = input("what is c? ")

f = int(c) - int(b)
x = int (f) /  int (a)

print(x)