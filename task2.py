#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
number= input("Enter a number")
#number= int(number)
if number > 0:
  print("positive")
if number < 0:
  print("negative")
if number == 0:
  print("zero")
