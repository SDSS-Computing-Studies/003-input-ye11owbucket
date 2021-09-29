#! python3
"""
Ask the user for their name and their email address.
You will need to use the .strip() method for this assignment. Be aware of your 
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""


x = input("what is your name? ").strip()
y = input("what is your email address? ").strip()
print("your name is " + x + "," + " your email address is " + y + "." )