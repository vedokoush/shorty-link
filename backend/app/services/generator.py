import random
import string

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def generate_numeric_code(length: int = 9):
    return ''.join(random.choices(string.digits, k=length))