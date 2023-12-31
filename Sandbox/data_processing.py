"""
This module performs various string operations based on user input.
It includes operations such as converting to upper case, word count, checking 
if a string is alphabetic, replacing characters in a string, and finding the 
length of a string.
"""

sentence = input("Please enter a sentence: ")
sentence = sentence.strip().upper()
print(f"{sentence} is your sentence with all characters in upper case")

paragraph = input("Please enter a paragraph: ")
print(f"The number of words in the paragraph is: {len(paragraph.split())}")

input_string = input("Please enter a string: ")

if(input_string.isalpha()):
    print("The characters are all alphabetic")
else:
    print("The characters contain digits or special characters")

o_string = input("Please enter a string: ").replace('a', 'o')
print(f"The string is with 'a' replaced with 'o' is: {o_string}")

full_name = input("Please enter your full name: ")

print(f"Your initials are: {full_name[0].capitalize()}. " +
        "{full_name[full_name.find(' ') + 1].capitalize()}.")

string_len = len(input("Please enter a string: "))
print(f"The length of the string is: {string_len}")
