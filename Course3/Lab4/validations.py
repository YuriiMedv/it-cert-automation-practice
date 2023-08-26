#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Перевіряє, чи заданий користувачський ім'я відповідає вимогам."""
    if type(username) != str:
        raise TypeError("Ім'я користувача повинно бути рядком")
    if minlen < 1:
        raise ValueError("Мінімальна довжина повинна бути не менше 1")

    # Ім'я користувача не може бути коротше за minlen
    if len(username) < minlen:
        return False
    # Ім'я користувача може містити лише літери та цифри
    if not re.match('^[a-zA-Z0-9]*$', username):
        return False
    # Ім'я користувача не може починатися з цифри
    if username[0].isnumeric():
        return False
    return True

print(True)  # True
print(False)  # False
print(True)  # True
print(False)  # False
