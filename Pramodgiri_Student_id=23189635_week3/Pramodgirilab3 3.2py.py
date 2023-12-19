# lab 3.2
balance=1000
i=0
name=input("Enter a name:")
print(f"welcome,{name}")
while True:
    k=input("1.If you want to make a deposit press K\n\n"
             "2. If you want to make a withdraw press L\n\n "
             "3. If you want to obtain a balance press M\n\n"
             " 4. If you want to quit press Q\n")
    if k=="K" or k=="k":
        l=int(input("How much you want to deposit?"))
        balance=balance+l
        print(f"{balance} is your total balance and deposit amount is {l}")
    elif k=="L" or k=="l":
        m=int(input("How much you want to withdraw?"))
        if m>1000:
            print("You cannot withdraw more than 1000.")
        else:
            balance=balance-m
            print(f"{balance} is your total balance now and your withdraw amount is {m}")
    elif k=="M" or k=="m":
        total_balance=balance
        print(f"{total_balance}is your total balance")
    
    elif k=="Q" or k=="q":
        print("Exit from program")
        break

   
#    Output
# Enter a name:Pramod
# welcome,Pramod
#1.If you want to make a deposit press K    

#2. If you want to make a withdraw press L  

#3. If you want to obtain a balance press M

# 4. If you want to quit press Q
# k
# How much you want to deposit?600
# 1600 is your total balance and deposit amount is 600.

# Output
#1.If you want to make a deposit press K

#2. If you want to make a withdraw press L

#3. If you want to obtain a balance press M

#4. If you want to quit press Q
# l
# How much you want to withdraw?600
# 1000 is your total balance now and your withdraw amount is 600

#Output
#1.If you want to make a deposit press K

#2. If you want to make a withdraw press L

#3. If you want to obtain a balance press M

#4. If you want to quit press Q
# m
# 1000is your total balance

# Output
#1.If you want to make a deposit press K

#2. If you want to make a withdraw press L

#3. If you want to obtain a balance press M

#4. If you want to quit press Q
#q
# Exit from program