num1 = float(input("Enter any number:"))
op = input("Any Mathematical operator:")
num2 = float(input("Enter any number:"))
if op == "+":
    print(num1 + num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")