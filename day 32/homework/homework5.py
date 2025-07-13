my_list = [1, 2, 3, 4, 5]
print("თავდაპირველი სია:", my_list)

index = int(input("რომელ ინდექსზე გსურთ ჩანაცვლება (0-4): "))
new_value = int(input("რისი ჩასმა გსურთ ამ ადგილას: "))

if 0 <= index < len(my_list):
    my_list[index] = new_value
    print("განახლებული სია:", my_list)
else:
    print("არასწორი ინდექსი")
