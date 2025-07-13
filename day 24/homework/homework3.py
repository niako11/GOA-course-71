secret_number = 7 

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Try again")
    guess = int(input("Guess the number again: "))
print("You guessed the number successfully!")




