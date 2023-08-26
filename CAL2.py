def calculator():
    print("Welcome to the calculator! Please enter two numbers and an operator (+ - * /) for calculation.")
    num1 = int(input("Please enter the first number: "))
    operator = input("Please enter the operator: ")
    num2 = int(input("Please enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print("Result: ", result)
    elif operator == "-":
        result = num1 - num2
        print("Result: ", result)
    elif operator == "*":
        result = num1 * num2
        print("Result: ", result)
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result: ", result)
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Error: Please enter a valid operator!")

calculator()
