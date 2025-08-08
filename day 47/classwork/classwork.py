# 1) filter_positives - აბრუნებს სიიდან მხოლოდ დადებით რიცხვებს
def filter_positives(numbers):
    return [num for num in numbers if num > 0]

# 2) filter_negatives - აბრუნებს სიიდან მხოლოდ უარყოფით რიცხვებს
def filter_negatives(numbers):
    return [num for num in numbers if num < 0]

# 3) ფუნქცია, რომელიც სახელს გადაიყვანს დიდ ასოებად (Uppercase)
def to_uppercase(name):
    return name.upper()
