"""
Basic quiz program
"""
import random
import logging
import sys

def setup_logger():
    """
    Sets up the logger
    """
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

QUESTIONS = [
    {'question': 'What is the highest singing voice?', 'answer': 'Soprano', 'incorrect_answers': ['Baritone', 'Alto', 'Tenor'], 'category': 'Music'},
    {'question': 'What is the chemical symbol for gold?', 'answer': 'Au', 'incorrect_answers': ['G', 'Ag', 'AuAu'], 'category': 'Science'},
    {'question': 'Which two countries share the longest international border?', 'answer': 'Canada and United States', 'incorrect_answers': ['Russia and China', 'Brazil and Argentina', 'India and Pakistan'], 'category': 'Geography'},
    {'question': 'Who wrote the play "Romeo and Juliet"?',  'answer': 'William Shakespeare', 'incorrect_answers': ['Jane Austen', 'Charles Dickens', 'Mark Twain'], 'category': 'Literature'},
    {'question': 'What is the value of π (pi) to two decimal places?', 'answer': '3.14', 'incorrect_answers': ['3.16', '3.12', '3.20'], 'category': 'Mathematics'},
    {'question': 'In what year did Christopher Columbus first reach the Americas?', 'answer': '1492', 'incorrect_answers': ['1450', '1520', '1600'], 'category': 'History'},
    {'question': 'Who is known as the "King of Pop"?', 'answer': 'Michael Jackson', 'incorrect_answers': ['Elvis Presley', 'Prince', 'David Bowie'], 'category': 'Music'},
    {'question': 'In which sport would you perform a slam dunk?', 'answer': 'Basketball', 'incorrect_answers': ['Football', 'Golf', 'Tennis'], 'category': 'Sports'},
    {'question': 'What does the acronym "URL" stand for?', 'answer': 'Uniform Resource Locator', 'incorrect_answers': ['Universal Remote Locator', 'Unified Resource Language', 'User Registration Link'], 'category': 'Technology'},
    {'question': 'Who directed the film "Jurassic Park"?', 'answer': 'Stephen Spielberg', 'incorrect_answers': ['James Cameron', 'Quentin Tarantino', 'Christopher Nolan'], 'category': 'Movies'},
    {'question': 'What is the capital city of Australia?', 'answer': 'Canberra', 'incorrect_answers': ['Sydney', 'Melbourne', 'Perth'], 'category': 'General Knowledge'},
    {'question': 'What is the powerhouse of the cell?', 'answer': 'Mitochondria', 'incorrect_answers': ['Cell Wall', 'Cell Membrane', 'Nucleus'], 'category': 'Biology'},
    {'question': 'Who painted the Mona Lisa?', 'answer': 'Leonardo da Vinci', 'incorrect_answers': ['Pablo Picasso', 'Claude Monet', 'Michelangelo'], 'category': 'Art'},
    {'question': 'What is the SI unit of force?', 'answer': 'Netwon', 'incorrect_answers': ['Watt', 'Joule', 'Volt'], 'category': 'Physics'},
    {'question': 'In George Orwells "1984" what is the totalitarian regime called?', 'answer': 'The Party', 'incorrect_answers': ['The Empire', 'The Republic', 'The Federation'], 'category': 'Literature'},
    {'question': 'Which river is the longest in the world?', 'answer': 'The Nile', 'incorrect_answers': ['Amazon River', 'Yangtze River', 'Mississippi River'], 'category': 'Geography'},
    {'question': 'What is the square root of 64?', 'answer': '8', 'incorrect_answers': ['7', '6', '9'], 'category': 'Mathematics'},
    {'question': 'Who was the first President of the United States', 'answer': 'George Washington', 'incorrect_answers': ['Thomas Jefferson', 'John Adams', 'Abraham Lincoln'], 'category': 'History'},
    {'question': 'In which Olympic sport would you perform a vault?', 'answer': 'Gynmastics', 'incorrect_answers': ['Swimming', 'Track and Field', 'Cycling'], 'category': 'Sports'},
    {'question': 'What does the acronym "HTML" stand for?', 'answer': 'Hypertext Markup Language', 'incorrect_answers': ['Hyperlink and Text Markup Language', 'High-Level Text Markup Language', 'Home Tool Markup Language'], 'category': 'Technology'},
    {'question': 'Who played the character Jack Dawson in the movie "Titanic"?', 'answer': 'Leonardo DiCaprio', 'incorrect_answers': ['Brad Pitt', 'Tom Cruise', 'Johnny Depp'], 'category': 'Movies'},
    {'question': 'Which planet is known as the Red Planet?', 'answer': 'Mars', 'incorrect_answers': ['Venus', 'Jupiter', 'Mercury'], 'category': 'General Knowledge'},
    {'question': 'What is the largest organ in the human body?', 'answer': 'Skin', 'incorrect_answers': ['Heart', 'Liver', 'Lung'], 'category': 'Biology'},
    {'question': 'Who painted "Starry Night"?', 'answer': 'Vincent van Gogh', 'incorrect_answers': ['Picasso', 'Rembrandt', 'Dali'], 'category': 'Art'},
    {'question': 'Which ocean is the largest by surface area?', 'answer': 'Pacific Ocean', 'incorrect_answers': ['Atlantic Ocean', 'Indian Ocean', 'Southern Ocean'], 'category': 'Geography'}
]

SCORE = 0

def game_start():
    """
    Start the game
    """
    print('Welcome to the exciting Quiz Show.')
    print('You have 5 questions each worth 10 points, please choose the right answer.')
    for _ in range(5):
        ask_question()
    final_result()

def ask_question():
    """
    Ask a question
    """
    # Ask random question
    index = random.randint(0, len(QUESTIONS) - 1)
    question = QUESTIONS.pop(index)
    print(question['question'])

    # List answers
    correct_answer_index = random.randint(0, 3)
    answers = question['incorrect_answers']

    answers.insert(correct_answer_index, question['answer'])

    for i, answer in enumerate(answers, start=1):
        print(f'{i}. {answer}')

    # Handle answers
    answer = input('Your answer (1/2/3/4): ')

    if answer==str(correct_answer_index+1):
        correct_answer()
    else:
        incorrect_answer()

def correct_answer():
    """
    Handles a correct answer
    """
    global SCORE
    print('Great job that is the correct answer!')
    SCORE += 1

def incorrect_answer():
    """
    Handles incorrect answers
    """
    print('That is not the correct answer')

def final_result():
    """
    Handles the final results
    """
    if SCORE>2:
        print(f'Congratulations you scored {SCORE}')
    else:
        print(f'You tried your best but you scored {SCORE}')


game_start()