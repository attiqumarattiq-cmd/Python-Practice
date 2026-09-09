
# Iteration with list comprehension
List = [i for i in [1,2,3]]
print(List)

list2 = []
for i in [1,2,3]:
    list2.append(i)
print(list2)

# List comprehension is basically a shorter way of writing a loop
# that creates a list

# EVEN NUMBER USING LIST COMPREHENSION
list3 = [i for i in range(11) if i % 2 == 0]
print(list3)

list4 = [i for i in [23,34,36,23,78,97,99] if i % 2 == 0]
print(list4)

list5 = [i for i in [23,34,36,23,78,97,99] if i % 2 == 0 and i <= 50]
print(list5)

