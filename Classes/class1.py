from MainClass import Main

compute = Main()

while True:
    try:
        val = input("Enter first value: ")
        val2 = input("Enter second value: ")
        break
    except ValueError:
        print("Enter a valid number!\n")

print(compute.calculate_sum(val, val2))
