
class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2
    
    def div(self, num1, num2):
        if(num2 != 0):
            return num1 / num2
        raise ValueError("Tried to divide by zero!")
        
    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

