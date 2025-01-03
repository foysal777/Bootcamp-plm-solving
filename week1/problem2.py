num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))


print(f"Summation: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")


if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2:.2f}")
else:
    print("Division: Division by zero is not allowed.")

