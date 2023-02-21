from os import urandom

class SecretKeyGenerator:
    @staticmethod
    def generate_secret_code() -> str:
        secret_code: str = urandom(20).hex()
        return secret_code
