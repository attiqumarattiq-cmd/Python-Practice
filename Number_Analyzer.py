
number = int(input("Enter a number: "))

if number >= 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negarive")
    
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    
square = number * number
cube = number * number * number

print("Square:", square)
print("Cube:", cube)
print(type(number))