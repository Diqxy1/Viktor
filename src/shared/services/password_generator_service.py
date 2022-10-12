import random
import string


class PasswordGeneratorService:

    def generate(self, quantity: int) -> str:
        if quantity < 6:
            raise ValueError('Quantidade minima 6 caracteres')

        letters = random.choices(string.ascii_letters, k=2)
        numbers = random.choices(string.digits, k=2)

        choices = random.choices(f'{string.ascii_letters}{string.digits}', k=quantity - 4)

        return ''.join(choices).join(letters).join(numbers)
