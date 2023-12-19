def create_list():
    return['PlayStation','Xbox','Steam','iOS','Google Play']
def get_info(my_list):
    firstelement=my_list[0]
    secondlastelement=my_list[-2]
    num1=len(my_list)
    return (firstelement,secondlastelement,num1)
def get_partial(my_list):
    return[my_list[1],my_list[2],my_list[3]]
def get_last_three(my_list):
    return[my_list[-1],my_list[-2],my_list[-3]]
def double_list(my_list):
    my_list=my_list+my_list
    return my_list
def amend(my_list):
    my_list[1]="None"
    my_list.append("Bye")
    return my_list

test_list=create_list()
print(test_list)
print(get_info(test_list))
print(get_partial(test_list))
print(get_last_three(test_list))
print(double_list(test_list))
print(amend(test_list))

# Output
# ['PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play']
# ('PlayStation', 'iOS', 5)
# ['Xbox', 'Steam', 'iOS']
# ['Google Play', 'iOS', 'Steam']
# ['PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play', 'PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play']
# ['PlayStation', 'None', 'Steam', 'iOS', 'Google Play', 'Bye']



