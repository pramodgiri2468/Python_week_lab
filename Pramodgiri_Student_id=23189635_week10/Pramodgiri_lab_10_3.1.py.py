class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        
        self.__cID=cID
        self.__first_name=first_name
        self.__second_name=second_name
        self.__address=address
        self.__balance=balance
        

    def get_cID(self):
        return self.__cID
    

    def set_cID(self, new_cID):
     self.__cID=new_cID
    

    def get_first_name(self):
       
        return self.__first_name
        

    def set_(self, new_first_name):

        self.__first_name=new_first_name
         

    def get_second_name(self):
        return self.__second_name
         

    def set_second_name(self, new_second_name):
        self.__second_name=new_second_name
         

    def get_address(self):
        return self.__address
    
    def set_address(self, addObj):
        self.__address =addObj

    def get_balance(self):
        return self.__balance
   
    def set_balance(self, value):
        self.__balance = value

    def deposite(self,value):
        self.__balance+=value

    def withdraw(self,value):
        self.__balance-=value

    def check_balnce(self):
        return self.__balance 

class Address:
    def __init__(self, number, street, town, post_code):
        self.__number=number
        self.__street=street
        self.__town=town
        self.__post_code=post_code
        
  
    def get_number(self):
        return self.__number
  
    def set_number(self, value):
        self.__number = value

  
    def get_street(self):
        return self.__street
    
    def set_street(self, value):
        self.__street = value

 
    def get_town(self):
        return self.__town
 
    def set_town(self, value):
        self.__town = value

  
    def get_post_code(self):
        return self.__post_code
    
    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self,new_address):
        self.number = new_address.number
        self.street = new_address.street
        self.town = new_address.town
        self.post_code= new_address.post_code

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"

def new_customer():

    cid= int(input("Enter customer id number: "))
    f_name= input( "Enter first name: ")
    s_name= input("Enter second name: ")
    adres = input("Enter address (number, street, town, postCode): ")
    while len(adres.split(',')) != 4:
        adres = input( "Please re-enter address (number, street, town, postCode): ")
    a = adres.split(',')
    print(a)
    balance = float(input( "Enter balance: "))
    return Customer(cid, f_name, s_name, Address(a), balance)

   

c = Customer('12A','Anna','Duka',Address(42,'Curzon Street','Birmingham', 'B4 2SU'),888)


def save_cRecords(lst):
    try:
        with open("client_list.txt" , 'w') as fd:

            for c in lst:
               fd.write(
                   f"{c.get_cID()},{c.get_first_name()},{c.get_second_name()},{c.get_address()} {c.get_balance()}\n")
        fd.close()
    except:
         
         return False
    else:
         return True


c1 = Customer('12A','Rea','Koci',Address('42','Curzon Street','Birmingham', 'B4 2SU'),888)
c2 = Customer('11A','Liora','Koci',Address('42b','Curzon Street2','Birmingham2', 'B4 2SU'),33)

save_cRecords([c1,c2])

def read_customerRecords(data_file):
    cList = []
    try:
        with open(data_file, 'r') as fd:
            for cust in fd:
                print(cust.split(','))
                cList.append(cust)
    except FileNotFoundError:
        print("File does not exist")
    finally:
        return cList
   
   


print(read_customerRecords('client_list.txt'))

# Output
# ['12A', 'Rea', 'Koci', '42', 'Curzon Street', 'Birmingham', 'B4 2SU 888\n']
# ['11A', 'Liora', 'Koci', '42b', 'Curzon Street2', 'Birmingham2', 'B4 2SU 33\n']
# ['12A,Rea,Koci,42,Curzon Street,Birmingham,B4 2SU 888\n', '11A,Liora,Koci,42b,Curzon Street2,Birmingham2,B4 2SU 33\n']






