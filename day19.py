class Bank_acc:
    Bank_name="python_bank"

    def __init__(self,bank_owner,Balance):
        self.bank_owner=bank_owner
        self.Balance=Balance

    def deposit(self,amount):
        if amount>0:
            self.Balance+=amount
            print(f"After the deposited : {self.Balance}")

    def withdaraw(self,amount):
        if amount>0 and amount<=self.Balance:
            self.Balance-=amount
            print(f"After the  withdraw : {self.Balance}")
        else:
            print("Insufficient Balance")

    def __str__(self):
        return f"{self.bank_owner} your balance is {self.Balance}"
    
    @classmethod
    def change_name(cls,new_bankname):
        cls.new_bankname=new_bankname


acc1=Bank_acc("Pratik",5000)
print(acc1)
acc1.deposit(2000)

acc1.withdaraw(1000)

print(f"old Bank_name:{Bank_acc.Bank_name}")


Bank_acc.change_name("Pratik_Bank")
print(f"New bank name:{Bank_acc.new_bankname}")


        

        
