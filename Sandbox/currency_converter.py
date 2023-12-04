"""
This module performs various operations on lists and dictionaries.

It converts a list of transactions from AED to USD and prints the converted values.
It also iterates over a list of numbers and prints each number multiplied by 2 if 
the number is even.

Furthermore, it iterates over a list of dictionaries representing students, calculates 
the total, average, and maximum grades for each student,
and prints a detailed message about each student including their name, age, average 
score, highest score, and all their grades.
It also checks if the student is graduating with honors (assuming an average score of 
85 is required to graduate) and adds this information to the message.
"""

transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21, 11.22, 33.44, 55.66, 77.88, 99.0]

transactions_usd = []

for item in transactions_aed:
    ITEM_USD = item*0.27
    print("Converting value", item, "to USD")
    transactions_usd.append(ITEM_USD)

print(transactions_usd)

lst = [2, 4, 5, 6]

for number in lst:
    if number%2 == 0:
        print(number*2)

students_data = [
    {'name': 'Alice', 'grades': [85, 88, 92], 'age': 20},
    {'name': 'Bob', 'grades': [90, 87, 80, 88], 'age': 21},
    {'name': 'Charlie', 'grades': [78, 80, 82, 77], 'age': 22},
]

for student in students_data:
    total_grades = sum(student['grades'])
    number_of_grades = len(student['grades'])
    average_grade = total_grades/number_of_grades
    max_grade = max(student['grades'])

    # Create a message about the student
    message = f"{student['name']} is {student['age']} years old. "
    message += f"They have an average score of {average_grade:.2f} and their highest score was {max_grade}.\n"
    message += "Here are their grades: \n"

    # Adding a nested loop to iterate over grades and create a detailed message
    for idx, grade in enumerate(student['grades']):
        message += f"\t- Test {idx+1}: {grade}\n"

    # Check if the student is graduating with honors (assuming average score of 85 is required to graduate)
    if average_grade >= 85:
        message += f"{student['name']} is graduating with honors! "
    else:
        message += f"{student['name']} is graduating. "

    # Print the message
    print(message)

