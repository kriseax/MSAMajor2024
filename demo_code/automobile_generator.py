import automobile

def main():
    #create autmobile objects
    auto1 = automobile.Automobile("Ford", "Focus", "1234", 2.2, "Alice", 2013)
    auto2 = automobile.Automobile("Honda", "Accord", "23456", 3.0, "Bob", 2017)

    #print data for auto1 and auto2
    auto1.print_info()
    auto2.print_info()

    #change auto2 engine size
    auto2.set_engine_size("2.4")

    #change auto1 owner
    auto1.set_owner("Cyd")

    auto1.print_info()
    auto2.print_info()

    #print car age information
    print(f"Auto1 is {auto1.get_age()} years old")
    print(f"Auto2 is {auto2.get_age()} years old")

    
    
main()