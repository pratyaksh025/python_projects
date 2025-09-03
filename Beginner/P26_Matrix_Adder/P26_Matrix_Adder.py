rows=int(input("Rows: "))
cols=int(input("Comlumns: "))


matrix1 = []
print("Enter Elements for Matrix 1:")
for i in range(rows):
    while True:
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Invalid number of elements! Please enter exactly {cols} numbers.")
        else:
            matrix1.append(row)
            break

print(matrix1)


matrix2 = []
print("Enter Elements for Matrix 2")

for i in range(rows):
    while True:
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Invalid number of elements! Please enter exactly {cols} numbers.")
        else:
            matrix2.append(row)
            break

result=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)

print("Result Matrix")
for row in result:
    print(" ".join(map(str, row)))