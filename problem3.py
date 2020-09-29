#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 mark
username= input("enter a username")

if "admin" in username:
  print("Enter password")
else:
  print("invalid user")
if "12345password" in password:
  print("Access granted")

