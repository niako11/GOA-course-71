number = int(input("Enter an integer: "))

if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")







correct_password = "1234"  
user_input = input("Enter password: ")

while user_input != correct_password:
    print("incorrect password")
    user_input = input("Enter password: ")

print("correct password")
