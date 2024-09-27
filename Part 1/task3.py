import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_char = '!@#$%^&*()'

def generate_password(length):
    password = ''

    combined_set = lower_case + upper_case + digits + special_char

    for char in range(length):
        random_char = random.choice(combined_set)
        password += random_char  

    return password

Password = generate_password(23)
print(Password)
