# 2) check_age - ასაკის შემოწმება
def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")

# 3) print_names - სახელების სიას ბეჭდავს ცალ-ცალკე
def print_names(names):
    for name in names:
        print(name)

# 4) odd_or_even - აბრუნებს Even თუ ლუწია, Odd თუ კენტი
def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 5) student_grade - მოსწავლის ქულის მიხედვით გრადაცია
def student_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 50 <= score <= 69:
        print("C")
    elif 0 <= score <= 49:
        print("F")
    else:
        print("Invalid score")
