class bankaccount():
    def __init__(self):
        self.balance=0
        
    def deposit(self):
        deposit=int(input('enter the deposit amount'))
        self.balance+=deposit
        print("balance after deposit",self.balance)
        
    def withdraw(self):
        withdraw=int(input('enter the amount to withdraw'))
        if self.balance>=withdraw:
            self.balance-=withdraw
        else:
            print("insufficient balance")
        print('balance afer withdrawal',self.balance)

s=bankaccount()
s.deposit()
s.withdraw()

#2nd assignment

class cone():
    def __init__(self,r,h):
        self.radius=r
        self.height=h
        
        
    def volume(self):
        import math
        pi=math.pi
        return pi * self.radius**2*self.height*(1/3)
        
        
        
    def baseside(self):
        import math
        sqrt=math.sqrt
        pi=math.pi
        return ((pi * self.radius ** 2) + (sqrt(self.radius**2 + self.height**2)))
        

l=cone(3,5)
print(l.volume())
print(l.baseside())




        