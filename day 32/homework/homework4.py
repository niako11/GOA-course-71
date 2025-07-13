sentence = input("შეიყვანეთ წინადადება: ")

if len(sentence) > 0:
    combined = sentence[0] + sentence[-1]
    print("პირველი და ბოლო ასო ერთად:", combined)
    print("წინადადება შებრუნებულად:", sentence[::-1])
else:
    print("შეიყვანეთ მაინც ერთი სიმბოლო.")
