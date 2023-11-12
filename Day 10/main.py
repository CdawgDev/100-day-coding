# def format_name(fname, lname):
#     """This returns a formatted name with the first letter of the two words and capitalize them"""
#     first = fname.title()
#     last = lname.title()
#     new_name = f"{first} {last}"
#     return(new_name)

# output_name = format_name("cORy", "cotterell")
# print(output_name)

#Calculator
from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
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
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type y to continue calculating with {answer} or type n to a new Calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()