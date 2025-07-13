my_height = 175 
user_height = int(input("Please enter your height in centimeters: "))

if user_height > my_height:
    print("You are taller than me.")
elif user_height == my_height:
    print("Our heights are the same.")
else:
    print("I am taller than you.")
