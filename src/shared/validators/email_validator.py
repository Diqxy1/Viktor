import re


class EmailValidator:

    def __init__(self, email: str):
        self._email = email

    def validate_email(self) -> bool:
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self._email):
            return True
        else:
            return False

