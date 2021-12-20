rows = int(input("insert number of rows: "))
cols = int(input("insert number of columns: "))
symbol = "#"

for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()
