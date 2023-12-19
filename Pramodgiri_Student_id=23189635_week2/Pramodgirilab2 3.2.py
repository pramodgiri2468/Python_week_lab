a=float(input("Enter first side :"))
b=float(input("Enter second side :"))
c=float(input("Enter third side :"))
if a+b>c and b+c>a and a+c>b:
   p=a+b+c
   print("The perimeter is:",p)
   s=(a+b+c)/2
   print("Semi-perimeter:",s)
   Area=(s*(s-a)*(s-b)*(s-c))**0.5
   print("The area is:",Area)
else :
    print("Triangle is not possible")

    #Output
      # Enter first side :5
      # Enter second side :4
      # Enter third side :7
      # The perimeter is: 16.0        
      # Semi-perimeter: 8.0
      # The area is: 9.797958971132712

      #Output
      # Enter first side :10
      # Enter second side :10
      # Enter third side :20
      # Triangle is not possible


    
        
    






   

    
    
   
    
    