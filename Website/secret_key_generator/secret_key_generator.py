from string import ascii_letters
from random import randint


class SecretKeyGenerator:
    @staticmethod
    def generate_secret_code() -> str:
        secret_code: str = ''
        ascii_length = len(ascii_letters) - 1

        for i in range(40):
            index = randint(0, ascii_length)
            secret_code += ascii_letters[index]

        return secret_code
