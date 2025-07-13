#      1
numbers = []

for i in range(5):
    num = int(input(f"{i+1}-ე რიცხვი: "))
    numbers.append(num)
print("შუა ორი ელემენტია:", numbers[1], "და", numbers[2])

#      2
alphabet = "abcdefghijklmnopqrstuvwxyz"
first_five = alphabet[:5]  
last_five = alphabet[-5:]  
rev_first = first_five[::-1] 
rev_last = last_five[::-1]   
result = rev_first + rev_last
print("შედეგი:", result)  
#         3
text = "IndexingAndSlicingIsPowerful"
part = text[:8]
reversed_part = part[::-1]
result = reversed_part[::3]

print("შედეგი:", result)

#       4
healthy_foods = input("ჩაწერეთ ჯანსაღი საკვები, გამოყავით მძიმით: ").split(",")
healthy_foods = [item.strip() for item in healthy_foods]
reversed_foods = healthy_foods[::-1]
print("ბოლო სამი ელემენტი შებრუნებული სიიდან:")
print(reversed_foods[-3])
print(reversed_foods[-2])  
print(reversed_foods[-1])  


