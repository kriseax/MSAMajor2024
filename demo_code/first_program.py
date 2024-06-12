print("Hello World!")

#create a variable to store my name
first_name = "Kristofferson"

#print My name is Kristofferson
print("My name is", first_name)

#declare a variables for last name
last_name = "Culmer"

#write a statement to display "My full name is firstname lastname" "
print("My full name is", first_name, last_name, sep="---")

#create a variable to store my age and weight
age = 17
weight = 187.3
half_age = age / 2

#print a sentence with name, age, and weight
print(
    f"My name is {first_name} {last_name}.\nI am {age} years old and I weigh {weight}lbs."
)

#get and print the data type for age and weight and half_age
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 print statements using string interpolation (f string) to print descriptive sentences for the datatypes
#Variable age is an int
print(f"Variable age is a {type(age)}")
print(f"Variable weight is a {type(weight)}")
print(f"Variable half_age is a {type(half_age)}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")

#Variable weight is a float
