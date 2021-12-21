def add(val1, val2):
    result = val1 + val2
    return result


def subtract(val1, val2):
    result = val1 - val2
    return result


def divide(val1, val2):
    result = val1 / val2
    return result


def multiply(val1, val2):
    result = val1 * val2
    return result


operations = ["+", "-", "/", "*"]

while True:
    value1 = float(input("Enter first value: "))
    value2 = float(input("Enter second value: "))

    choice = input(
        "Select an operation:\n+ for add;\n- for subtract;\n/ for divide;\n* for multiply;\nEnter a choice: ")
    if choice == "+":
        print(f"{value1} + {value2} = " + str(add(value1, value2)))
    elif choice == "-":
        print(f"{value1} - {value2} = " + str(subtract(value1, value2)))
    elif choice == "/":
        print(f"{value1} / {value2} = " + str(divide(value1, value2)))
    elif choice == "*":
        print(f"{value1} * {value2} = " + str(multiply(value1, value2)))
    else:
        print("You entered a not valid operation!\n")

    response = input("Do you want to do another calculation? Answer Y or N: ").upper()
    if response != "Y":
        print("Goodbye")
        break
