# Calculator program
op = input("Enter operator: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid operator"
print("Result:", result)
