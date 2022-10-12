import re


class PhoneValidator:

    def __init__(self, phone: str):
        self._phone = phone

    def validate_phone(self) -> bool:
        if re.match(r"^[0-9]*$", self._phone):
            return True
        else:
            return False
