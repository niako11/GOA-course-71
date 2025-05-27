celsius = float(input("Enter room temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

if fahrenheit > 89.6:
    print("Cooling system ON.")
else:
    print("Cooling system OFF.")
