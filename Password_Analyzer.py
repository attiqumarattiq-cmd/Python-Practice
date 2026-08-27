
print("===========================================")
print("        --- PASSWORD ANALYZER ---")
print("===========================================")
print("Rules to enter password: ")
print("Length should be at least 8")
print("Contains at least one lowercase letter")
print("Contains at least one uppercase letter")
print("Contains at least one digit")
print("-------------------------------------------")
password = input("Enter a password: ")
print("-------------------------------------------")
if len(password) >= 8:
    print("Length: Valid")
else:
    print("Length: Invalid")
    
has_lower = False
has_upper = False
has_digit = False

for i in range(len(password)):
    if i.islower():
        
    
