
matrix = [
    [j for j in range(3)]      # IT CREATES A LIST
    for i in range(4)          # IT CONTROLS THE ROWS
    ]

print(matrix)



matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(j)
    matrix.append(row)
    
print(matrix)