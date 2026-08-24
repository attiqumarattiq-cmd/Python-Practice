
print("=============================================")
print("    --- STUDENT ELIGIBILITY ANALYZER---")
print("=============================================")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

print("-------------------------------------------")
print("    --- DISPLAYING INFORMATION ---")
print("-------------------------------------------")
print("Your name is ", name)
print("Your age is ", age)
print("Your attendance percentage is ", attendance)
print("-------------------------------------------")
if marks >= 50 and attendance >=75.0 and age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")
print("-------------------------------------------")