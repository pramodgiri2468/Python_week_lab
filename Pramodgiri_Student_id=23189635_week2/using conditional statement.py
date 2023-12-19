input_year=int(input("Enter the Year to be checked: "))
if ((input_year%400==0) or ((input_year%4==0) and (input_year% 100!=0))):
    print("It is a leap year.")
else:
    print("It is not a leap year.")

# Output
# Enter the Year to be checked: 2036
# It is a leap year.

# Output
# Enter the Year to be checked: 2034
# It is not a leap year.
