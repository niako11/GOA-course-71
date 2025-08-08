# 1) ფუნქცია, რომელიც აბრუნებს სიიდან მხოლოდ უარყოფით რიცხვებს
def get_negative_numbers(numbers):
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
    return negatives

# 2) ფუნქცია, რომელიც აბრუნებს სიიდან მხოლოდ დადებით რიცხვებს
def get_positive_numbers(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives

# 3) ფუნქცია, რომელიც პირველ რიცხვს აყავს მეორე რიცხვის ხარისხში და შემდეგ ამ ნამრავლს უყრის მესამე რიცხვს
def power_and_multiply(a, b, c):
    return (a ** b) * c
