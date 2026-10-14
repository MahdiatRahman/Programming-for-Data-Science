#Problem 1

a = float(input("Enter first no: "))
b = float(input("Enter second no: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


#Problem 2
name = input("Enter name: ")
student_id = input("Enter ID: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))

print("\nStudent Profile")
print("Name:", name)
print("ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)


#Problem 3
c = float(input("Enter Celsius: "))

f = (c * 9/5) + 32
k = c + 273.15

print("Fahrenheit:", f)
print("Kelvin:", k)


#Problem 4
name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input("Enter mark: "))
    marks.append(mark)

print("Name:", name)
print("Total:", sum(marks))
print("Average:", sum(marks) / 5)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Passed courses:", sum(1 for m in marks if m >= 50))