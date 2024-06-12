#Write a program to convert pounds to kilograms
#Write a function to get a positive number from the user
def get_positive_float_input():
  #ask a user to enter their weight in pounds, and validate correct input
  #if bad input, reprompt the user
  user_weight = 0
  #bad_input = True
  while(True):
    try:
      user_weight = float(input("Enter your weight in pounds:"))
      #check in user weight is > 0. If not, reprompt the user
      if user_weight <= 0:
        print("ERROR: Enter a weight greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number greater than 0")

  return user_weight
  

#INPUT
#get weight from the user
user_weight = get_positive_float_input()

#PROCESSING
#use a conversion to convert pounds to kilos: 2.205lbs = 1kg
lbs_to_kg_conversion = 2.205
user_weight_in_kg = user_weight / lbs_to_kg_conversion

#OUTPUT
#print output to the user
#You weight XXXX kgs
print(f"You weigh {user_weight_in_kg:.2f}kgs.")
