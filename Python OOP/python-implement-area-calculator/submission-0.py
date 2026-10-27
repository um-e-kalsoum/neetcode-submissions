import math

class AreaCalc:
    
    def calculate(self, *args):
        if len(args) == 1:
            res = math.pi * args[0] ** 2
            res = round(res, 2)
            return res
        if len(args) == 2:
            res = args[0] * args[1]
            return res    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
