#Create a function to return the season based on the month
#Input: month number
#Output: Season name
def get_season_name(month_number):

    #determine the season using an if statement
    if month_number == 12 or month_number == 1 or month_number == 2:
        return "Winter"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "Spring"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "Summer"
    else:
        return "Fall"

def get_month_number():
    while True:
        try:
            month_number = int(input("Enter month number 1 - 12: "))
            if month_number < 1 or month_number > 12:
                print("ERROR: enter a number 1 - 12")
                continue
            break
        except:
            print("ERROR: enter a number 1 - 12")

    return month_number

def main():
    #Create a decision structure to determine the season winter, spring, summer, fall based on the month
    #Winter: 12, 1, 2; Spring: 3, 4, 5; Summer: 6, 7, 8; Fall: 9, 10, 11
    #Ask the user to enter the number of the month. Must be 1 to 12 
    #Output the season based on the month
    
    #get the month number
    while True:
        month_number = get_month_number()
        season_name = get_season_name(month_number)
        print(f"It is {season_name}!")

        #ask user if they want to contine
        run_again = input("Do you want to run the program again? y or Y: ")
        if run_again == "y" or run_again == "Y":
            continue
        else:
            print("Ending the program...")
            break

main()