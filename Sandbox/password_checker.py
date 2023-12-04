"""
Checks passwords
"""

MIN_CHARACTERS = 7
STRONG_CHARACTER_LIMIT = 12
SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '`', '~', '[', ']', '{', '}', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '/', '?']

HAS_SPECIAL_CHARACTERS = False
HAS_NUMBER = False
HAS_7_CHARS = False
FAILED_PASSWORD = 0
MAX_TRIES = 3

def check_password(password):
    """
    Checks password strength
    """
    global MIN_CHARACTERS, STRONG_CHARACTER_LIMIT, SPECIAL_CHARACTERS, NUMBERS

    # Validate min characters
    if len(password) < MIN_CHARACTERS:
        unacceptable_password('Password does not meet minimum length')
        return

    # Validate special characters
    if not any(char in SPECIAL_CHARACTERS for char in password):
        unacceptable_password('Password does not have a special character')
        return

    # Validate digits
    if not any(char.isdigit() for char in password):
        unacceptable_password('Password does not have a number')
        return

    # Validate uppercase character
    if not any(char.isupper() for char in password):
        unacceptable_password('Password does not have an uppercase character')
        return

    # Validate lowercase character
    if not any(char.islower() for char in password):
        unacceptable_password('Password does not have a lowercase character')
        return

    # Validate strong or good password
    if len(password) >= STRONG_CHARACTER_LIMIT and sum(char.isdigit() for char in password)>=2 and sum(char in SPECIAL_CHARACTERS for char in password)>=2:
        strong_password()
    else:
        acceptable_password()

def unacceptable_password(reason):
    """
    Handles passwords that don't meet the criteria
    """
    global FAILED_PASSWORD
    print(reason)
    FAILED_PASSWORD += 1
    if FAILED_PASSWORD < MAX_TRIES:
        check_password(input('Please input your password: '))


def acceptable_password():
    """
    Handles passwords that meet min criteria
    """
    print('Good password provided thank you.')

def strong_password():
    """
    Great jorb
    """
    print('Strong password provided thank you.')

password_to_check = input('Please input your password: ')
check_password(password_to_check)
