#    1

# len() აბრუნებს სიის სიგრძეს.
# append() ამატებს ახალ ელემენტს სიის ბოლოში.
# insert() ამატებს ახალ ელემენტს სიაში მითითებულ ინდექსზე.
# pop() შლის სიიდან ელემენტს.

#    2

names = ["Anamaria", "Giorgi", "Nia", "Luka", "Nita"]
new_name = input("Enter new name:")
names.append(new_name)

print("The length of the list is:", len(names))
print("Updated list:", names)

#    3

fruits= ["Malon", "Orange", "Xantaloupe", "Watermalon", "Kiwi"]
fruits.pop()
fruits.insert(3, "Pomegrante")
print(fruits)