class  Bankaccount:
    acc_count=0
    def __init__(self,account_no,name,account_type,balance):
        self.account_no=account_no
        self.name=name
        self.account_type=account_type
        self.balance=balance
        Bankaccount.acc_count+=1
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def display(self):
        print("\n\n")
        print(self.account_no,self.name,self.account_type,self.balance)
        print("\n\n")
i=1
while i!=0:
    ch=int(input("1.create\n2.display\n3.deposit\n4.withdraw\n0.exit\n"))
    if ch==1:
        b1=Bankaccount(1,input("enter name:"),input("enter account type:"),int(input("enter balance:")))
    elif ch==2:
        b1.display()
    elif ch==3:
        amount=int(input("enter amount to deposite:"))
        if amount<0:
            print("enter a valied amount")
        else:
             b1.deposit(amount)
    elif ch==4:
         amount=int(input("enter amount to withdraw:"))
         if amount<0:
             print("enter a valid amount:")
         elif b1.balance()<amount:
             print("insufficient balance")
         else:
             b1.withdraw(amount)
    elif ch==0:
         break
    else: 
         print("wrong option")
        
