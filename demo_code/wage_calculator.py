def get_nonnegative_float_from_user(prompt, must_be_less_than_24):
    while True:
        try:
            input_value = float(input(prompt))
            if (input_value < 0):
                print("Only nonnegative values are allowed. Please re-enter the value.\n")
                continue
            if(input_value > 24 and must_be_less_than_24):
                print("ERROR: Hours worked must be less than 24")
                continue
            break
        except ValueError:
            print("Please enter a nonnegative numerical value.\n")
            continue
    
    return input_value


#declare known variable values
#12% tax rate
tax_rate = 0.12
days_worked = 350
another_calculation = True
  
#ask user for number of hours worked daily by calling the get_nonnegative_float_from_user function
hours = get_nonnegative_float_from_user("Enter the number of hours worked daily: ", True)

#ask user for hourly wage by calling the get_nonnegative_float_from_user function
hourly_wage = get_nonnegative_float_from_user("Enter the hourly wage: ", False)

#calculate annual wage
annual_wage = hours * hourly_wage * days_worked

#calculate tax amount
tax_amount = tax_rate * annual_wage

#calculate annual wage minus tax
annual_wage_minus_tax = annual_wage - tax_amount

#output results
print(f"\nPay Advice")
print(f"-------------")
print(f"Hours Worked: {hours}")
print(f"Hourly Wage: ${hourly_wage}")
print(f"Wages Before Taxes: ${annual_wage:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Annual Wage After Taxes: ${annual_wage_minus_tax:.2f}")
    
