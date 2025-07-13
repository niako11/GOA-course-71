stock = 300

while stock > 0:
    if stock >= 2:
        stock -= 2
        print("You have bought the drink")
        print("Remaining stock:", stock)
    else:
        break

print("Out of stock")
