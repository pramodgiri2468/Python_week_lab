from L8_Library import Bankaccount
NIMB=Bankaccount(1,100)
NIC=Bankaccount(2,100)
NIMB.withdraw(40)
NIC.withdraw(40)
print(f"The bank balance of NIMB is {NIMB.get_balance()}") 
print(f"The bank balance of NIC is {NIC.get_balance()}")
NIMB.deposit(20)
NIC.deposit(20)
print(f"The bank balance of NIMB is {NIMB.get_balance()}") 
print(f"The bank balance of NIC is {NIC.get_balance()}")
NIC.transfer(20,NIMB)
print(f"The bank balance of NIMB is {NIMB.get_balance()}") 
print(f"The bank balance of NIC is {NIC.get_balance()}")

# Output
# The bank balance of NIMB is 60
# The bank balance of NIC is 60  
# The bank balance of NIMB is 80 
# The bank balance of NIC is 80  
# The bank balance of NIMB is 100
# The bank balance of NIC is 60  
