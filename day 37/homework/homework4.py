data_types = [42, 3.14, True, "hello", None, [1, 2], False, "Python", 99, True]

# ვიღებთ მხოლოდ Boolean-ებს
for value in data_types:
    if type(value) == bool:
        print(value)
