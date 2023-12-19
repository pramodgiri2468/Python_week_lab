'''3.1 A positive whole number n > 2 is prime if no number between 2 and √n (inclusive) evenly
divides n. Write a program that accepts a value of n as input and determines if the number is
prime. If n is not prime, your program should print all the divisors of n.'''

num1=int(input("Enter any positive number:"))
if num1>1:
    for i in range(2,num1):
        if(num1%i)==0:
            print(num1,"is not a prime number")
            count=0
            for i in range(1,num1+1):
                if num1%i==0:
                    count+=1
                    print(i,end="\n")
            
            print("Total", count ,'divisor')
            break

            
            
    else:
      print(num1,"is a prime number")


