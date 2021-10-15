#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

lenght = nr_letters + nr_symbols + nr_numbers

password = []

password_str = ''

for l in range(0, nr_letters):
  password.append(letters[random.randint(0, len(letters) - 1)])
for s in range(0, nr_symbols):
  password.append(symbols[random.randint(0, len(symbols) - 1)])
for n in range(0, nr_numbers):
  password.append(numbers[random.randint(0, len(numbers) - 1)])

for n in range(0, len(password)):
  password_str += str(password[n])

print(str(password_str))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_random = []

password_str_random = ''

for l in range(0, nr_letters):
  password_random.append(letters[random.randint(0, len(letters) - 1)])
for s in range(0, nr_symbols):
  password_random.append(symbols[random.randint(0, len(symbols) - 1)])
for n in range(0, nr_numbers):
  password_random.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(password_random)

for n in range(0, len(password_random)):
  password_str_random += str(password_random[n])

print(str(password_str_random))