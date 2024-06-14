
def main():

    a = 7
    b = 7
    if a > b:
        print(f"{a} is greter than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else: 
        print(f"{a} is equal to {b}")

    #print the appropriate letter grade based on the test score
    #A: 100 - 90, B: 89 - 80, C: 79 - 70, D: 69 - 60, F
    print("\nGrade Decision: 1")
    test_score = 77

    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif test_score <= 90 and test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score <= 80 and test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score <= 70 and test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")
    
    #Grade decision statement restructured
    print("\nGrade Decision: 2")
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    #Create a decision structure to determine the season winter, spring, summer, fall based on the month
    #Winter: 12, 1, 2; Spring: 3, 4, 5; Summer: 6, 7, 8; Fall: 9, 10, 11
    #Ask the user to enter the number of the month. Must be 1 to 12 
    #Output the season based on the month



    c = 4
    d = 10
    if a == 4 or b == 5 or c == 5 or d == 9:
        print("The or condition is true") 

main()