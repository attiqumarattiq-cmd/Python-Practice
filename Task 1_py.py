
my_var = 50
# now it is int
print("==============================")
print("Now, it is in integer: ")
print(id(my_var))
Address = id(my_var)

print("==============================")

# convert to string
print("Now it converts to string:")
print(str(my_var))
string = str(my_var)

#Joining address and value

result = str(Address) + ">>" + string
print("==============================")
print("After joining address and value: ")
print(result)
print("==============================")




