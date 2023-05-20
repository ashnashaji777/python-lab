class bank:
    def __init__(self,accn,name,accty):
        self.accn=accn
        self.name=name
        self.accty=accty
        self.bal=0
    def showamount(self):
        print("Account holder name:",self.name)
        print("Account number:",self.accn)
        print("Account type:",self.accty)
        print("your balance amount:",self.bal)
    def deposite(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("enter your name:")
a=int(input("enter account number:"))
t=input("enter your account type:")
o=bank(a,n,t)
o.showamount()
while(True):
    print("\nMenu")
    print("\n1.Deposit")
    print("\n2.Withdraw")
    c=int(input("enter your choice:"))
    
    if(c==1):
        d=int(input("enter the amount to be depiosite:"))
        print("your total balance amount is:",o.deposite(d))
    elif(c==2):
        w=int(input("enter the amount to be withdrawn:"))
        if(w>d):
            print("insufficient balance")
        else:
            print("your local balance is:",o.withdraw(w))
    else:
        print("enter a valied choice")
        
            
              

    
      
      
    
        
