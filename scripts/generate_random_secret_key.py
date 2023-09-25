import secrets
import os

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.

    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)

    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))


def get_random_secret_key():
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return get_random_string(50, chars)


def secret_key_set():
    # Check if the .env file exists
    if not os.path.isfile('.env'):
        return False

    # Open the .env file and search for a line with SECRET_KEY
    with open('.env', 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and split by '='
            parts = line.strip().split('=')
            if len(parts) == 2 and parts[0] == 'SECRET_KEY':
                return True

    # If no matching line is found, return False
    return False


if not secret_key_set():
    with open(".env", "a") as f:
        secret_key = get_random_secret_key()
        f.write(f"SECRET_KEY={secret_key}")


