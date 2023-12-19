'''1. In this task, you will design a program which display a census report of the numbers and percentages
of houses with particular numbers of occupants in a road.
2. When the program starts, it should ask the user 8 times about houses with occupancy of 0 to 6, plus 6+
to count the numbers of houses with particular numbers of occupants.
• For each question, the user should enter a digit for the number of houses, e.g.:
• Please note there is a space after the colon mark.
• This step should be implemented in a function named get_data().
• The function will return all the 8 integer values entered by the user.
3. After user entered the data, the program will calculate the percentage of each occupancy category.
• For example, if the total house is 35 and the house with 0 occupant is 2, the percentage of
houses with 0 occupancy is 5.7%. This is because (2/35) * 100 is 5.7%.
• This step should be implemented in a function named cal_percentage().
• The function should take 8 parameters of the house number for each occupancy category. The
order of the parameters must be the same as the user entered in step 2.
• The function will return 8 float values for percentages of each occupancy category in the same
order.

4. When the calculation finished, the program outputs the census result as below:

• The output must comply with the width specification given above.
• Read this article to find out more about setting format.
• This step should be implemented in a function named display_result().
• The function takes 16 parameters. The first 8 are for the house number of each occupancy
category and second 8 are for the corresponding percentages.
• The output of the function should follow the specification above.
5. To sum up, in the program, it should include definition of the three functions you have created and the
necessary codes to run the program. See below for the result of the completed program (user inputs are
highlighted in yellow):'''

from colorama import init, Fore, Style

#Initialize colorama
init()
#This is the the function to take 8 input from user about house with 0,1,2,3,4,5,6,6+ occupancy.
def get_data(value):
    user=int(input(f"provide the number of houses with {value} occupancy:{Fore.YELLOW} "))
    print(Style.RESET_ALL)
    return user

a1=get_data(0)
a2=get_data(1)
a3=get_data(2)
a4=get_data(3)
a5=get_data(4)
a6=get_data(5)
a7=get_data(6)
a8=get_data("6+")

house_list=[a1,a2,a3,a4,a5,a6,a7,a8]
#here we calculate the sum of houses
total=sum(house_list)

#this is the function to calculate the percentage.
def cal_percentage(part):
    r=(part/total)*100
    return f"{r:.1f}%"

r1=cal_percentage(a1)
r2=cal_percentage(a2)
r3=cal_percentage(a3)
r4=cal_percentage(a4)
r5=cal_percentage(a5)
r6=cal_percentage(a6)
r7=cal_percentage(a7)
r8=cal_percentage(a8)

#this is the function to display the reports.
def display_result(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16):
     print(f'{" occupants:":<15} {0:<9} {1:<9} {2:<9} {3:<9} {4:<9} {5:<9} {6:<9} {">6"}')
     print(f'{" No.Houses:":<15} {b1:<9} {b2:<9} {b3:<9} {b4:<9} {b5:<9} {b6:<9} {b7:<9} {b8}')
     print(f'{"percentage:":<12} {b9:<9} {b10:<9} {b11:<7}  {b12:<8}  {b13:<8}  {b14:<8}  {b15:<9}  {b16}')

report=display_result(a1,a2,a3,a4,a5,a6,a7,a8,r1,r2,r3,r4,r5,r6,r7,r8)

# Output
#provide the number of houses with 0 occupancy: 2

#provide the number of houses with 1 occupancy: 3

#provide the number of houses with 2 occupancy: 4

#provide the number of houses with 3 occupancy: 2

#provide the number of houses with 4 occupancy: 3

#provide the number of houses with 5 occupancy: 1

#provide the number of houses with 6 occupancy: 6

#provide the number of houses with 6+ occupancy: 2

#  occupants:     0         1         2         3         4         5         6         >6
#  No.Houses:     2         3         4         2         3         1         6         2
# percentage:  8.7%      13.0%     17.4%    8.7%      13.0%     4.3%      26.1%      8.7%




