
def main():
    
    while True:
        month_number = input("Enter month number 1 - 12: ")
        if month_number in ["12", "1", "2"]:
            print("It is Winter")   
        elif month_number in ["3", "4", "5"]:
            print("It is Spring")   
        elif month_number in ["6", "7", "8"]:
            print("It is Summer")   
        elif month_number in ["9", "10", "11"]:
            print("It is Fall") 
        else:
            print("ERROR: Enter a number between 1 and 12")
            continue 
        break
            


main()