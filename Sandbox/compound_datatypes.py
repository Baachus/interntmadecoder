fruits = ['apple', 'banana', 'cherry' , 'date']

fruits.append('elderberry')
fruits.remove('banana')

# fruits.sort(reverse = True)
fruits.sort()
print(fruits)

student = {
    "Name": "John Doe",
    "Age": 25,
    "Major": "Computer Science"
}

student["Major"] = "Electrical Engineering"
student["Year"] = "Senior"
print(student.keys())
print(student)

library = [
    {
        "Title": "The Stand",
        "Author": "Stephen King",
        "Year": 1987
    },
    {
        "Title": "Carrie",
        "Author": "Stephen King",
        "Year": 1965
    },
    {
        "Title": "Hide",
        "Author": "Carrie Miller",
        "Year": 1995
    }
]

print(f"The title of the second book is {library[1]['Title']}")

print(f"The year of the third book is {library[2]['Year']}")

for book in library:
    print(f"The book is {book['Title']} and was written by {book['Author']}")

courses = {
    "math": ['Bob', 'Suzie', 'Joe', 'Tim', 'Stephen'],
    "history": ['Kelly', 'Anusha', 'Saf', 'Kevin', 'Monty'],
    'chemistry': ['Zack', 'Nithya', 'Timmy', 'Carrie', 'Brown']
}

courses['math'].append('John')
courses['math'].append('James')
courses['math'].append('Jenny')
courses['math'].append('Jacob')
courses['math'].append('Jim')

courses['history'].pop(2)

print(f"The students in chemistry are {courses['chemistry']}")

courses['physics'] = ['Billy', 'Bobby', 'Benny', 'Brittany', 'Blakely']

print(courses)
