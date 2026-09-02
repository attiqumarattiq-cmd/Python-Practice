
list = [10,20,30,40,50,60]

it = iter(list)
print(type(it))                 # it --------- iterator
print(type(list))               # list --------- iterable

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("============================")
list1 = ["ISLAMABAD", "LAHORE", "KARACHI"]
for i in list1:
    print(i)
print("============================")
list2 = ["ISLAMABAD", "LAHORE", "KARACHI"]
iterator = iter(list2)
print(next(iterator))
print(next(iterator))
print(next(iterator))


