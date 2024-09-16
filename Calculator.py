# Function to perform the chosen arithmetic operation
def calculate(num1,num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operation== '%':
        return  num1 %num2
    elif operation == '//':
        if num2 != 0:
            return num1 // num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation : ")

# Perform the calculation and display the result
result = calculate(num1,num2,operation)
print(f"The result is: {result}")
