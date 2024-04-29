import random as rand
import time as tm

#Asks usr for basic information
while True:
  try:
    user_name = input("What is your name?  ")
    if user_name.isalpha():
      print("Hello ", user_name".")
      break
    else:
      raise TypeError
  except TypeError:
    print("Please enter letters only.")
    return False
