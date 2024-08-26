import random

# This is the list of characters that can be in the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

# This will hold the final password (a blank string)
password = ""

# This will set the password to be 16 characters long
for i in range(16):
    # Choosing a random character from 'chars' and add it to 'password'
    password += random.choice(chars)

# Print the generated password
print("Your password: " + password)