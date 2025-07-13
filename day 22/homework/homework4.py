age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")

if age < 18 and is_student.lower() == "yes":
    print("Discount granted")
else:
    print("No discount")
