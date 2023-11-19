"""
This module performs various operations including power operation, string formatting, 
and string interpolation. It calculates the power of 11 to -3, prints the value of pi 
with 2 decimal accuracy, and prints formatted strings with names and ages.
"""

SUMVALUE  = 11**-3
print(SUMVALUE)

X = 3.141592653589793
# formatted string with 2 decimal accuracy
print (f"The value of X is {X:.2f}")

# another way: use round()
print(f"The value of X is {round(X, 2)}")

NAME = "Alice"
AGE = 30

NAME2 = "Thomas"
AGE2 = 24

print(f"My name is {NAME} and I am {AGE} years old.")

STRING_CHECK = "hello"
print(STRING_CHECK[1:4])

STRING_CHECK = "123456789"
print(STRING_CHECK[1:8:2])

print("abc"< "acfdrgfdyfga")
print("apple" < "Banana")
print(ord("A"))

print('C' in 'Code')
print('c' in 'Code')
print('abc' in 'abfc')
print('mail' not in 'email')

DATE = "19/12/1898"
FIRST_SLASH_INDEX = DATE.find("/")
SECOND_SLASH_INDEX = DATE.find("/", FIRST_SLASH_INDEX + 1)
YEAR = DATE[SECOND_SLASH_INDEX + 1:]
MILLENNIUM = DATE[SECOND_SLASH_INDEX + 1]+"000"

print(YEAR)
print(MILLENNIUM)
