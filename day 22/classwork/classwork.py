#დავალება - 1

# if ამოწმებს პირველ პირობას. თუ პირობა სწორია  შესრულდება შესაბამისი კოდი.

# elif ნიშნავს "else if" და გამოიყენება დამატებითი პირობების შესამოწმებლად, თუ if არ შესრულდა.

# else გამოიყენება, როცა არც ერთი პირობა არ შესრულდა  მაშინ შესრულდება else ბლოკის კოდი.

# დავალება - 2

my_surname = "Kabulashvili" 
user_surname = input("Enter your surname: ")

if my_surname == user_surname:
    print("Our surnames are similar")
else:
    print("Our surnames are not similar")
 
# დავალება - 3

my_height = 175
user_height = int(input("Enter your height in cm: "))

if my_height > user_height:
    print("I'm taller than you.")
elif my_height < user_height:
    print("You're taller than me.")
else:
    print("We have equal heights.")


