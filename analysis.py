import string


def analyze_password(password):
    if len(password) < 8:
        return False, "Password is too short! Use at least 8 characters."

    if not any(char.isdigit() for char in password):
        return False, "Password should include at least one digit."

    if not any(char.isupper() for char in password):
        return False, "Password should include at least one uppercase letter."

    if not any(char in string.punctuation for char in password):
        return False, "Password should include at least one special character."

    return True, "Your password is strong!"
