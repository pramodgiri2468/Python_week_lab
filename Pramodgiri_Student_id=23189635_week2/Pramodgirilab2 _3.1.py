input_year=int(input("Enter the Year to be checked: "))
if(input_year %4==0):
    if(input_year %100==0):
        if(input_year %400==0):
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")

# Output
# Enter the Year to be checked: 2000
# It is a leap year.

# Output
# Enter the Year to be checked: 2025
# It is not a leap year.
        