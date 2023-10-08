import random
str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Generate a password that no one can hack you, unless they have a big 🧠")
letters_int = int(input("How many letters would you like in your password?\n"))
symbols_int = int(input(f"How many symbols would you like?\n"))
number_int = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, letters_int + 1):
  password_list.append(random.choice(str))

for char in range(1, symbols_int + 1):
  password_list += random.choice(sym)

for char in range(1, number_int + 1):
  password_list += random.choice(num)

print(password_list)
random.shuffle(password_list)
print(password_list)

pwrd = ""
for char in password_list:
  pwrd += char

print(f"Your password is: {pwrd}")
