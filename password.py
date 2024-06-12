import random

# List of characters to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Taking user inputs for the number of letters, symbols, and numbers
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initializing an empty list to store the password characters
password_list = []

# Adding random letters to the password list
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Adding random symbols to the password list
for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

# Adding random numbers to the password list
for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

# Printing the unshuffled password list
print(password_list)

# Shuffling the password list to ensure randomness
random.shuffle(password_list)

# Printing the shuffled password list
print(password_list)

# Converting the password list to a string
password = ""
for char in password_list:
  password += char

# Displaying the generated password
print(f"Your password is: {password}")
