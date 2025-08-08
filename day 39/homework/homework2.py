# .lower() – გარდაქმნის სტრინგს პატარა ასოებად
text = "HELLO"
print(text.lower())  # შედეგი: "hello"

# .upper() – გარდაქმნის სტრინგს დიდი ასოებად
text = "hello"
print(text.upper())  # შედეგი: "HELLO"

# .capitalize() – მხოლოდ პირველი ასო ხდება დიდი, დანარჩენი – პატარა
text = "hELLo"
print(text.capitalize())  # შედეგი: "Hello"

# .title() – თითოეული სიტყვის პირველი ასო დიდი ხდება
text = "hello world"
print(text.title())  # შედეგი: "Hello World"

# .strip() – აშორებს ცარიელ სივრცეებს სტრინგის დასაწყისსა და ბოლოში
text = "   hello   "
print(text.strip())  # შედეგი: "hello"

# .replace() – ცვლის სტრინგში არსებულ სიმბოლოებს ან სიტყვებს
text = "hello world"
print(text.replace("world", "Python"))  # შედეგი: "hello Python"

# .find() – აბრუნებს ინდექსს, სადაც პირველად გვხვდება კონკრეტული სიმბოლო/სიტყვა
text = "hello"
print(text.find("l"))  # შედეგი: 2

# .count() – ითვლის რამდენჯერ გვხვდება კონკრეტული სიმბოლო ან სიტყვა სტრინგში
text = "banana"
print(text.count("a"))  # შედეგი: 3

# .startswith() – ამოწმებს იწყება თუ არა სტრინგი მითითებული ელემენტით (აბრუნებს True/False)
text = "Python"
print(text.startswith("Py"))  # True

# .endswith() – ამოწმებს მთავრდება თუ არა სტრინგი მითითებული ელემენტით
text = "program.py"
print(text.endswith(".py"))  # True

# .split() – ყოფს სტრინგს სიად, ჩვეულებრივ, space-ის მიხედვით
text = "hello world"
print(text.split())  # ['hello', 'world']

# .join() – აერთიანებს ელემენტებს სტრინგად
words = ["hello", "world"]
print(" ".join(words))  # შედეგი: "hello world"
