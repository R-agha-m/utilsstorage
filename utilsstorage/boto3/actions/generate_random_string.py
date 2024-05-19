from random import choices
from string import ascii_lowercase, digits

all_letters = ascii_lowercase + digits


def generate_random_string(length: int = 20) -> str:
    return ''.join(choices(
        all_letters,
        k=length,
    ))
