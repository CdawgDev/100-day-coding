# Create a password generator that ask for how many letters, symbols, and numbers.
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password_letters = ""
# password_numbers = ""
# password_symbols = ""
# password_characters = []
# password = ""
# for x in range(1, nr_letters + 1):
#     password_characters.append(random.choice(letters))

# for x in range (1, nr_numbers + 1):
#     password_characters.append(random.choice(numbers))

# for x in range(1, nr_symbols + 1):
#     password_characters.append(random.choice(symbols))

# for characters in password_characters:
#     password += characters

# print(f"Your password with {nr_letters} letters, {nr_symbols} symbols, and {nr_numbers} numbers is {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_letters = ""
password_numbers = ""
password_symbols = ""
password_characters = []
password = ""
scrambled_password = ""
for x in range(1, nr_letters + 1):
    password_characters.append(random.choice(letters))

for x in range (1, nr_numbers + 1):
    password_characters.append(random.choice(numbers))

for x in range(1, nr_symbols + 1):
    password_characters.append(random.choice(symbols))

temp_password_characters = password_characters.copy()
for characters in password_characters:
    char = random.choice(temp_password_characters)
    password += char
    temp_password_characters.remove(char)

print(f"Your password with {nr_letters} letters, {nr_symbols} symbols, and {nr_numbers} numbers is {password}")