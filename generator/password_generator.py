import string
import random

def generator_password(length = 12):
    characters = (
        string.ascii_lowercase + 
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(characters)for _ in range(length))

    return password

def has_lowercase(password):
    return any(c.islower() for c in password)

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_number(password):
    return any(c.isdigit() for c in password)   

def has_symbol(password):
    return any(c in string.punctuation for c in password)