print("შეიყვანე 5 რიცხვი:")

a = int(input("რიცხვი 1: "))
b = int(input("რიცხვი 2: "))
c = int(input("რიცხვი 3: "))
d = int(input("რიცხვი 4: "))
e = int(input("რიცხვი 5: "))

numbers = [a, b, c, d, e]
total = sum(numbers)
average = total / len(numbers)

print(f"The arithmetic mean of this list is: {average}")
print(f"The sum of all numbers in this list is: {total}")
