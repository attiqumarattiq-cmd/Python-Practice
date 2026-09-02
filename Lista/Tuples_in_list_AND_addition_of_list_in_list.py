
list = []
print("===========================================")
print(list)
print("===========================================")
list.append(12)
list.append("Fast University")
list.append(34.67)
list.append("^&*$")
list.append("qwerty")
print(list)
print("===========================================")
print("List after adding of 1, 2, 3: ")
for i in range(1,4):
    list.append(i)

print(list)
print("===========================================")
print("Adding tuples in list: ")
list.append((5,6))
print(list)
print("===========================================")
print("Adding of list to a list: ")
list2 = ["HELLO", "I AM", 5634, 34.90]
list.append(list2)
print(list)
print(list[8][1])
    


