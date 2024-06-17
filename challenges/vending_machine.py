#Vending Machine

def main():
    #initialize amount due to 50
    amount_due = 50
    print("Vending Machine\n------------------\n")

    #loop until amount due is 0 or less
    while True:
        #print the amount due
        print(f"Amount Due: {amount_due}")

        #ask user to enter a coin
        coin = input("\nEnter coin: ")

        #determine if coin denomination is valid. if not, reprompt user and continue to the top of the loop
        if coin not in ["1", "5", "10", "25"]:
            continue

        #subtract from amount due
        amount_due -= int(coin)

        #determine if amount due is 0 or less. If amount due > 0, reprompt the user, else break out of the loop
        if amount_due <= 0:
            amount_due *= -1
            break
        else:
            continue
    
    print(f"Change due: {amount_due}")


main()