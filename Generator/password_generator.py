import random
import string
from math import log2

def estimate_password_strength(password):
    char_types = 0
    if any(char.islower() for char in password):
        char_types += 1
    if any(char.isupper() for char in password):
        char_types += 1
    if any(char.isdigit() for char in password):
        char_types += 1
    if any(char in string.punctuation for char in password):
        char_types += 1

    entropy = log2(len(password) ** char_types)
    return entropy

def generate_password(length=12,
                      uppercase=True,
                      lowercase=True,
                      numbers=True,
                      special_chars=True,
                      min_upper=1,
                      min_lower=1,
                      min_numbers=1,
                      min_special=1,
                      ambiguous_chars=False,
                      passphrase=False):
    # Define character sets
    upper_chars = string.ascii_uppercase if uppercase else ''
    lower_chars = string.ascii_lowercase if lowercase else ''
    digit_chars = string.digits if numbers else ''
    special_chars_set = "!@#$%^&*()_+[]{}|;:,.<>?/" if special_chars else ''

    # Include ambiguous characters (e.g., 'l', '1', 'I', '0', 'O')
    ambiguous_chars_set = 'l1I0O' if ambiguous_chars else ''

    # Combine character sets
    all_chars = upper_chars + lower_chars + digit_chars + special_chars_set + ambiguous_chars_set

    # Ensure at least one character type is selected
    if not all_chars:
        raise ValueError("At least one character type should be selected")

    if passphrase:
        # Generate a passphrase with words
        words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'watermelon', 'kiwi', 'blueberry']
        password = ' '.join(random.sample(words, length))
    else:
        # Ensure minimum characters for each type
        password = (
            ''.join(random.sample(upper_chars, min_upper)) +
            ''.join(random.sample(lower_chars, min_lower)) +
            ''.join(random.sample(digit_chars, min_numbers)) +
            ''.join(random.sample(special_chars_set, min_special)) +
            ''.join(random.choice(all_chars) for _ in range(length - min_upper - min_lower - min_numbers - min_special))
        )

        # Shuffle the generated password
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

    return password

# Example usage
password = generate_password(length=16,
                             uppercase=True,
                             lowercase=True,
                             numbers=True,
                             special_chars=True,
                             min_upper=2,
                             min_lower=2,
                             min_numbers=2,
                             min_special=2,
                             ambiguous_chars=True,
                             passphrase=False)
print("Generated Password:", password)

# Example for estimating password strength
strength = estimate_password_strength(password)
print("Estimated Password Strength:", strength)
