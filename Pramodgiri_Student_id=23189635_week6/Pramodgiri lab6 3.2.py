def view_contact(contact):
    e=1
    print("------VIEW CONTACT------")
    print("")
    for i in contact:
        print(f"{e}. {i[0]}  {i[1]}")
        e=e+1

def add_contact(contact):
    print("------ADD CONTACT------")
    print("")
    name1=input("Enter contact name :")
    num1=int(input("Enter contact number :"))
    tup=(name1,num1)
    contact.append(tup)
    print(f"{name1}-{num1} has been added into contact.")

def delete_contact(contact):
    print("------DELETE CONTACT-----")
    print("")
    e=1
    for i in contact:
        print(f"{e}. {i[0]}  {i[1]}")
        e=e+1
    
    delete_id=int(input("Enter the ID of the contact to delete:"))
    total_id=len(contact)
    if(total_id>=delete_id and delete_id>0):
        print(f"Deleting: Record {delete_id} {contact[delete_id-1][0]} {contact[delete_id-1][1]}")
        del contact[delete_id-1]
    else:
        print("\nInvalid entry!!! The data couldn't be deleted because the entered number is out of range.")
contact=[("Stish", "123"), ("Rita", "321")]

while(1):
    choice=input("\nSelect an operation:\nv view contact\na add contact\nd delete contact\nq quit\n\nEnter choice(v/a/d/q):")
    if(choice=="v"):
        view_contact(contact)
    elif(choice=="a"):
        add_contact(contact)
    elif(choice=="d"):
        delete_contact(contact)
    elif(choice=="q"):
        print("-----Goodbye-----")
        quit()
    else:
        print("-----Invalid entry-----")
        print("\n.....try again")



# Output
#Select an operation:  
#v view contact        
#a add contact
#d delete contact      
#q quit

#Enter choice(v/a/d/q):v
# ------VIEW CONTACT------

# 1. Stish  123
# 2. Rita  321


# Output
# Enter choice(v/a/d/q):a
# ------ADD CONTACT------

#Enter contact name :Pramod
#Enter contact number :9859
# Pramod-9859 has been added into contact.

#Enter choice(v/a/d/q):v
#------VIEW CONTACT------

# 1. Stish  123
# 2. Rita  321
# 3. Pramod  9859

# Output
# Enter choice(v/a/d/q):d
# ------DELETE CONTACT-----

# 1. Stish  123
# 2. Rita  321
# 3. Pramod  9859
# Enter the ID of the contact to delete:3
# Deleting: Record 3 Pramod 9859

# Output
# Enter choice(v/a/d/q):v
# ------VIEW CONTACT------

# 1. Stish  123
# 2. Rita  321

# Output
# Select an operation:
# v view contact
# a add contact
# d delete contact
# q quit

# Enter choice(v/a/d/q):q
# -----Goodbye-----

# Output
# Select an operation:  
# v view contact        
# a add contact
# d delete contact      
# q quit

# Enter choice(v/a/d/q):v
# ------VIEW CONTACT------

# 1. Stish  123
# 2. Rita  321

# Select an operation:
# v view contact
# a add contact
# d delete contact
# q quit

# Enter choice(v/a/d/q):3
# -----Invalid entry-----

# .....try again




        