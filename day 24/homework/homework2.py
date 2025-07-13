password = input("Enter your password: ")

repeat = input("Repeat the password: ")
while repeat != password:
    print("Passwords do not match. Try again.")
    repeat = input("Repeat the password: ")

print("Password matched!")
