while True:
    number = float(input("Enter a positive number: "))
    
    if number > 0:
        print("Thank you! You entered a positive number.")
        break
    else:
        print("That is not a positive number. Please try again.")
