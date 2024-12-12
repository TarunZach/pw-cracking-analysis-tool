import string
import random


def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(characters, k=length))
