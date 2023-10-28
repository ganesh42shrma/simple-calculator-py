from art import logo
#calculator functions
#Adding function
def add(a, b):
    """Add Two Numbers"""
    return a + b


#Subtracting function
def subtract(a, b):
    """Subtract Two Numbers"""
    return a - b


#Multiplying function
def multiply(a, b):
    """Multiply Two Numbers"""
    return a * b


def division(a, b):
    """Divide Two Numbers"""
    return a / b


#Function Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}


def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
