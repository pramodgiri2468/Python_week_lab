class BMI:
    def __init__(self) :
        self.__height=0.0
        self.__weight=0.0
    def set_weight(self,weight):
        self.__weight=weight
    def set_height(self,height):
        self.__height=height
    def __call_BMI(self):
        BMI=self.__weight/((self.__height)**2)
        return BMI
    def display_BMI(self):
        BMI=self.__call_BMI()
        print(f"Your BMI is {round(BMI,2)}")
def main():
    Pramod=BMI()
    user_weight=float(input("Insert your weight:"))
    user_height=float(input("Insert your height(in meters):"))
    Pramod.set_weight(user_weight)
    Pramod.set_height(user_height)
    Pramod.display_BMI()
if(__name__)=="__main__":
    main()

# Output
# Insert your weight:55
# Insert your height(in meters):3
# Your BMI is 6.11

        


