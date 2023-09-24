from ...metadata.custom_exceptions.webapp_exceptions import PasswordIntegrityException as __PasswordIntegrityException
import re

def verify_password(
        password1:str,
        password2:str=None,
        capital_letter=True,
        number=True,
        special_sign=False,
        accepted_special_signs=["$","!","&", "*", "#"],
        min_len=8,
        max_len=127):
    
    if password2:
        if password1 != password2:
            raise __PasswordIntegrityException("Passwords are not matching.")
    
    if len(password1) < min_len:
        raise __PasswordIntegrityException(f"Password too short - minimal number of characters: {min_len}.")
    elif len(password1) > max_len:
        raise __PasswordIntegrityException(f"Password too long - maximal number of characters: {max_len}.")
    elif capital_letter and re.search('[A-Z]',password1) is None:
        raise __PasswordIntegrityException("Password must contain capital character.")
    elif number and re.search('[0-9]',password1) is None:
        raise __PasswordIntegrityException("Password must contain number.")
    elif special_sign and re.search(f'[{"".join(accepted_special_signs)}]', password1) is None:
        raise __PasswordIntegrityException(f"One of special characters has to be used: {', '.join(accepted_special_signs)}")

    
