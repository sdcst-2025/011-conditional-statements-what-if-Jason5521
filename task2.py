#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
number = input("Please enter a number.")
if number > 0:
    print("This number is a positive number.")
if number < 0:
    print("This number is a negative number.")
if number == 0:
    print("This number is zero.")