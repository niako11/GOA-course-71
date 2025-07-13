
vending_machine = ["Coca-Cola", "Pepsi", "Nuts", "Chips", "Chocolate", "Orange Juice", "Hot Chocolate", "Strawberries""Berries""Coffee"]

print("Welcome to the Vending Machine!")
print("Please select a product by entering the product number from the list below:\n")

for i, product in enumerate(vending_machine):
    print(f"{i}. {product}")
while True:
    try:
        user_choice = int(input("\nEnter the number of the product you want: "))
        
        
        if 0 <= user_choice < len(vending_machine):
            print(f"\nYou selected: {vending_machine[user_choice]}")
            break
        else:
            print("\nInvalid choice. Please choose a number between 0 and 9.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
