import math

print("addition(+)")
print("subtraction(-)")
print("Multiplication(*)")
print("division(*)")
print("power(**)")
print("square roots (sqrt)")

operator = input("enter one of the operators :")

if operator == "+":
    x = float(input("enter the 1st number:"))
    y = float(input("enter the 2nd number:"))
    addition = x + y 
    print(f"it is equal:{addition}")

elif operator == "-":
    x = float(input("enter the 1st number:"))
    y = float(input("enter the 2nd number:"))
    subtraction = x - y 
    print(f"it is equal:{subtraction}")

elif operator == "*":
    x = float(input("enter the 1st number:"))
    y = float(input("enter the 2nd number:"))
    multiplication = x * y 
    print(f"it is equal:{multiplication}")

elif operator == "/":
    x = float(input("enter the 1st number:"))
    y = float(input("enter the 2nd number:"))
    division = x / y 
    print(f"it is equal:{division}")

elif operator == "**":
    x = float(input("enter number:"))
    y = float(input("enter power number:"))
    power = pow(x,y)
    print(f"it is equal:{power}")

elif operator == "sqr":
    x = float(input("enter the number to square :"))
    sqr = math.sqrt(x)
     
    print(f"it is equal:{sqr}")

else:
    print("the operator is not valid")


    
