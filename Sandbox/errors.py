"""
errors
"""

def validate_email(email_address):
    """
    Validate email address
    """
    if "@" in email_address and '.' in email_address:
        return True
    else:
        raise ValueError("This is not a valid email address.  ")

email = input("Enter your email address: ")

try:
    validate_email(email)
    # login(email)

    print("Logged in successfully!")

except ValueError as e:
    print(e, "Please try again.")


EGGS = 2
BANANA = 1
SALAD = 10
STEAK_AND_RICE = 30

print("breakfast cost: ")
print((EGGS+BANANA))

print("lunch cost: ")
print((SALAD))

print("dinner cost: ")
print((STEAK_AND_RICE + EGGS))
