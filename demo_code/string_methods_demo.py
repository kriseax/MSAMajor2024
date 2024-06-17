
def main():
    #Capitalize a string
    my_name = "Kristofferson"
    print(my_name.capitalize())

    #MAke a string uppercase
    print(my_name.upper())

    #MAke a string lowercase
    last_name = "CULMER"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #Determine if a string starts with a set of characters
    print(my_name.startswith("k"))

    if(not my_name.startswith("kris") and not my_name.startswith("Kris")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    #Determine if a string ends with a specified set of characters
    print(my_name.endswith("son"))

    #find a set of characters in a string
    print(my_name.find("f", 7))

    #loop through a string
    print("\n\n")
    for letter in my_name:
        print(letter)
    
    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of occurences of the word dog in sentnce
    #expected output: 3
    #use a while loop to read the string
    #start at the beginning of the string
    #read the string until you fing the first occurence of dog
    #add 1 to the number of found dogs 
    #continue reading from the next index: update the start index in the find method()
    dog_index = 0
    number_of_dogs = 0
    while True:
        #loof for do in sentence
        dog_index = sentence.find("dog", dog_index)

        #if dog not found break the loop, else add 1 to satrt_index and add 1 to number_of_dogs
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            dog_index += 1
            continue
    
    print(f"Number of Dogs: {number_of_dogs}")

    #Solution 2
    more_dogs = True
    start_index = 0
    dog_count = 0
    while more_dogs:
        found_index = sentence.find("dog", start_index)

        if found_index != -1:
            dog_count += 1
            start_index = found_index + 1
        else:
            more_dogs = False

    print(f"Number of Dogs: {dog_count}")

    #How to use the split method
    car_info = "Ferrari,f-50,2021,500000,4.8\n"

    car_data = car_info.split(",")
    print(car_data)


        

main()