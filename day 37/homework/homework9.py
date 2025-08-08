text = input("Enter a string: ")

print("Characters at odd indexes:")
for i in range(len(text)):
    if i % 2 != 0:
        print(text[i])
