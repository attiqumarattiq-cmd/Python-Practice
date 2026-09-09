
numbers = [1,2,3,4,5]
squared = []

for i in numbers:
    squared.append(i * i)
    
print(squared)

# SYNTEX: newList = [expression for element in oldList]

numbers = [5,4,3,2,1]
squared = [i * i for i in numbers]
print(squared)