# 4) ფუნქცია, რომელიც აბრუნებს სახელსა და ასაკს
def user_info(name, age):
    return f"{name} არის {age} წლის."

# 5) ფუნქცია, რომელიც აბრუნებს რიცხვის კვადრატს
def square(num):
    return num ** 2

# 6) ფუნქცია, რომელიც აბრუნებს პირველ რიცხვს აყვანილს მეორე რიცხვის ხარისხში
def power(base, exponent):
    return base ** exponent

# 7) ფუნქცია, რომელიც სიაში ყველა ელემენტს გააორმაგებს
def double_values(lst):
    return [x * 2 for x in lst]

# 8) ფუნქცია, რომელიც სიაში ყველა ელემენტს კვადრატში აიყვანს
def square_list(lst):
    return [x ** 2 for x in lst]

# 9) ფუნქცია, რომელიც აბრუნებს სამი რიცხვის ჯამს
def sum_three(a, b, c):
    return a + b + c

# 10) ფუნქცია, რომელიც აბრუნებს ორი რიცხვის სხვაობას
def substract(a, b):
    return a - b

# 11) ფუნქცია, რომელიც აბრუნებს ორი რიცხვის ნამრავლს
def multiply(a, b):
    return a * b

# 12) ფუნქცია, რომელიც აბრუნებს ორი რიცხვის განაყოფს
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "ნულზე გაყოფა შეუძლებელია!"



print(user_info("ანა", 20))          # ანა არის 20 წლის.
print(square(5))                     # 25
print(power(2, 3))                    # 8
print(double_values([1, 2, 3]))       # [2, 4, 6]
print(square_list([2, 4, 6]))         # [4, 16, 36]
print(sum_three(1, 2, 3))             # 6
print(substract(10, 4))               # 6
print(multiply(3, 7))                 # 21
print(divide(10, 2))                   # 5.0
