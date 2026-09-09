
#USING FOR LOOP
numbers = []

for i in range(1, 6):
    numbers.append(i * 10)
print(numbers)


#USING LIST COMPREHENSION

list2 = [i * 10 for i in range(1,6)]
print(list2)