# 2) manual sum ფუნქცია - სიაში ელემენტების ჯამი
def manual_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

# 3) მომხმარებლის მონაცემების დაბრუნება წინადადებად (f-string-ით)
def user_info(name, surname, age):
    return f"მომხმარებლის სახელი: {name}, გვარი: {surname}, ასაკი: {age} წლისაა."

# 4) Arithmetic_mean - სიაში ელემენტების საშუალო არითმეტიკული
def arithmetic_mean(lst):
    if len(lst) == 0:
        return 0  # თუ სია ცარიელია, დავუბრუნოთ 0 (ან შეიძლება გამოაგდოთ შეცდომა)
    total = manual_sum(lst)
    return total / len(lst)

# 5) ფუნქცია, რომელიც სტრინგიდან ხმოვანებს ფილტრავს და აბრუნებს
def filter_vowels(s):
    vowels = "აეიოუAEIOUaeiou"  # ქართული და ინგლისური ხმოვანი ასოები (თუ ქართულად გინდა, ამოშალე ინგლისური)
    result = ""
    for ch in s:
        if ch in vowels:
            result += ch
    return result



print(manual_sum([1, 2, 3, 4]))  
# Output: 10

print(user_info("ანა", "ბერიძე", 25))  
# Output: მომხმარებლის სახელი: ანა, გვარი: ბერიძე, ასაკი: 25 წლისაა.

print(arithmetic_mean([10, 20, 30, 40]))  
# Output: 25.0

print(filter_vowels("გამარჯობა"))  
# Output: ააოა
