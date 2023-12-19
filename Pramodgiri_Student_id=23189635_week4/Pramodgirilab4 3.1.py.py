'''Create a program that takes three parameters; two numbers and one string. The string is used to
indicate the arithmetic operation to apply on the two numbers. The program output should look
like the following:

4. The program must use an if statement that uses the sign operator string to decide on
the arithmetic operation to be done on the two numbers (See above example).
5. The program should returns the answer plus an explanation. For example, if the user
inputs 7, then 5 and then *, the program should return “multiplying 7 by 5 = 35”
6. The program should be able to call 4 functions to perform 4 arithmetic operations and
these are add, subtract, multiply and divide.
7. Then create a function calculator to implement the actual calculator.'''

def add(k,l):
    adding=k+l
    return adding

def subtract(k,l):
    sub=k-l
    return sub

def multiplication(k,l):
    multiply=k*l
    return multiply

def division(k,l):
    divi=k/l
    return divi

def calculator():
 m=int(input("Enter a number: "))
 n=int(input("Enter a number :"))
 o=input("Enter the operator here\n\n 1.press + for addition\n\n 2.press - for subtraction\n\n 3.press * for multiplication\n\n 4.press / for division\n ")

 if o=="+":
    adding=add(m,n)
    print(f"{adding} is your answer\n\n here the {m} and {n} is adding using the operator {o}")
 elif o=="-":
     sub=subtract(m,n)
     print(f"{sub} is the answer\n\n here the {n} is subtracted from {m} using the operator {o} ")
 elif o=="*":
    multiply=multiplication(m,n)
    print(f"{multiply} is the answer\n\n here the {m} is multiplied with {n} using the operator {o} ")

 elif o=="/":
    divi=division(m,n)
    print(f"{divi} is the answer\n\n here the {m} is divided by {n} using the operator {o}")

ans=calculator()


# Output
#Enter a number: 45
#Enter a number :50
#Enter the operator here      

#1.press + for addition      

#2.press - for subtraction   

#3.press * for multiplication

#4.press / for division      
#+
#95 is your answer

#here the 45 and 50 is adding using the operator +

# Output
#Enter a number: 46
#Enter a number :20
#Enter the operator here      

#1.press + for addition      

#2.press - for subtraction   

#3.press * for multiplication

#4.press / for division      
#-
#26 is the answer

#here the 20 is subtracted from 46 using the operator -

# Output
#Enter a number: 7
#Enter a number :8
#Enter the operator here      

#1.press + for addition      

#2.press - for subtraction   

#3.press * for multiplication

#4.press / for division      
# *
#56 is the answer

#here the 7 is multiplied with 8 using the operator *

# Output
#Enter a number: 60
#Enter a number :10
#Enter the operator here      

#1.press + for addition      

#2.press - for subtraction   

#3.press * for multiplication

#4.press / for division      
# /
#6.0 is the answer

#here the 60 is divided by 10 using the operator /
