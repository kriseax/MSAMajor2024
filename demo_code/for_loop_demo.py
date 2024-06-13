
def main():
    #print integers between 0 and 10:
    for number in range(11):
        print(number)

    #print integers between 5 and 10
    print("\n\n")
    for number in range(5, 11):
        print(number)

    #print even numbers between 0 and 10
    print("\n\n")
    for number in range(0, 11, 2):
        print(number)

    #prompt the user for start and stop values and print the numbers between start and stop
    #get the start value from the user and convert to an integer
    #get the stop value from the user and convert to an integer
    start_value = int(input("Enter a start value: "))
    #use start and stop values in a for loop
    stop_value = int(input("Enter a stop value: "))

    for number in range(start_value, stop_value):
        print(number)



main()