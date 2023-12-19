my_list=[]

def get_next_point(step):
    x=int(input(f"Input x{step} coordinates:"))
    y=int(input(f"Input y{step} coordinates:"))
    return (x,y)

def cal_distance(p1,p2):
   
    distance=(((p1)**2)+((p2)**2))**0.5
    return distance

def main():
    x1=0
    y1=0
    step=1
    while True:
        x2,y2=get_next_point(step)
        step +=1
        if x2==999 and y2==999:
            break
        p1=(x2-x1)
        p2=(y2-y1)
        distance_step=cal_distance(p1,p2)
        my_list.append(distance_step)
        x1=x2
        y1=y2

    step_loop=1
    for i in my_list:
        print(f"Step {step_loop}: {i:.2f} units")
        step_loop=step_loop+1
 

main()
total_distance=sum(my_list)
print(f"Total distance travelled by the robot:{total_distance:.2f} units ")

if __name__=="_main_":
    main()
print(__name__)

# Output
# Input x1 coordinates:3
# Input y1 coordinates:7
# Input x2 coordinates:8
# Input y2 coordinates:9
# Input x3 coordinates:2
# Input y3 coordinates:1
# Input x4 coordinates:999
# Input y4 coordinates:999
# Step 1: 7.62 units
# Step 2: 5.39 units
# Step 3: 10.00 units
# Total distance travelled by the robot:23.00 units







