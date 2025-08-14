import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard level from user input
user_letter = "".join(random.choices (letters,k=nr_letters))
user_symbols = "".join(random.choices(symbols,k=nr_symbols))
user_numbers= "".join(random.choices(numbers,k=nr_numbers))
print(user_letter+user_numbers+user_symbols)

# Generate own password
nr_letters=random.randint(1,10)
nr_symbols=random.randint(1,5)
nr_numbers=random.randint(1,5)

#Hard level
user_letter = "".join(random.choices (letters,k=nr_letters))
user_symbols = "".join(random.choices(symbols,k=nr_symbols))
user_numbers= "".join(random.choices(numbers,k=nr_numbers))
print(user_letter+user_numbers+user_symbols)