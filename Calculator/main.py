import art
print(art.logo)


# Add
def add(n1, n2):
    return n1+n2


# Subtract
def subtract(n1, n2):
    return n1-n2


# Multiply
def multiply(n1, n2):
    return n1*n2


# Divide
def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(f"Type {symbol}")

    keep_going = True

    while keep_going:
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        another_operation = input(f"Type 'y' to continue with {answer}, type 'n' to start a new operation, or type 'e' to exit. : ")

        if another_operation == 'y':
            num1 = answer
        elif another_operation == 'n':
            keep_going = False
            calculator()
        else:
            print("Thanks for using the calculator!!!")
            keep_going = False


calculator()










































