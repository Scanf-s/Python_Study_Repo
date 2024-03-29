class Calculator:
    def __init__(self, num1, num2): #Constructor
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def mul(self):
        return self.num1 * self.num2
    def sub(self):
        return self.num1 - self.num2
    def div(self):
        try:
           result = self.num1 / self.num2
           return result
        except ZeroDivisionError:
            return print("Exception : ZeroDivisionError")
        else:
            return print("Error")
    def pow(self):
        return self.num1 ** self.num2
        
    
user1 = Calculator(2, 3)
print(user1.add())
print(user1.mul())
print(user1.sub())
print(user1.div())
print(user1.pow())
