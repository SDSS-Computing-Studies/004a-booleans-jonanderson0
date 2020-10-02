#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
 import math
  
a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

if a > b and a > c:
  hyp = a
elif b > a and b > c:
  hyp = b
elif c > a and c > b:
  hyp = c
  
if hyp == a:
  side1 = b
  side2 = c
elif hyp == b:
  side1 = a
  side2 = c
elif hyp == c:
  side1= a
  side2= b

actual_hyp = side1**2 + side2**2

if side1**2 + side2**2 == round(hyp)**2 and (hyp - actual_hyp > 0.02*hyp or hyp - actual_hyp < -0.02*hyp):
  print("that is a right triangle")
elif side1**2 + side2**2 > hyp**2:
  print("that is an acute triangle")
elif side1**2 + side2**2 < hyp**2:
  print("that is an obtuse triangle")

