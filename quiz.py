import random

questions = [
    {
        "q": "What is the capital of France?",
        "o": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
        "a": "c"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "o": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "a": "b"
    },
    {
        "q": "What is the largest mammal in the world?",
        "o": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Lion"],
        "a": "b"
    },
    {
        "q": "Which gas do plants absorb from the atmosphere?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "b"
    },
    {
        "q": "What is the chemical symbol for gold?",
        "o": ["a) Go", "b) Au", "c) Ag", "d) Gd"],
        "a": "b"
    },
    {
        "q": "How many continents are there on Earth?",
        "o": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "a": "c"
    },
    {
        "q": "Who wrote the play 'Romeo and Juliet'?",
        "o": ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) George Orwell"],
        "a": "c"
    },
    {
        "q": "Which gas makes up the majority of Earth's atmosphere?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "c"
    },
    {
        "q": "What is the largest organ in the human body?",
        "o": ["a) Heart", "b) Brain", "c) Skin", "d) Liver"],
        "a": "c"
    },
    {
        "q": "Which country is known as the Land of the Rising Sun?",
        "o": ["a) China", "b) South Korea", "c) Japan", "d) Thailand"],
        "a": "c"
    },
    {
        "q": "What is the smallest prime number?",
        "o": ["a) 0", "b) 1", "c) 2", "d) 3"],
        "a": "c"
    },
    {
        "q": "In which year did Christopher Columbus first reach the Americas?",
        "o": ["a) 1492", "b) 1512", "c) 1620", "d) 1776"],
        "a": "a"
    },
    {
        "q": "What is the chemical symbol for water?",
        "o": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"],
        "a": "a"
    },
    {
        "q": "Which gas do humans exhale when they breathe out?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Helium"],
        "a": "b"
    },
    {
        "q": "What is the largest planet in our solar system?",
        "o": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "a": "d"
    },
    {
        "q": "What is the tallest mountain in the world?",
        "o": ["a) Mount Kilimanjaro", "b) Mount St. Helens", "c) Mount Everest", "d) Mount Fuji"],
        "a": "c"
    },
    {
        "q": "Who painted the Mona Lisa?",
        "o": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Rembrandt"],
        "a": "c"
    },
    {
        "q": "What is the currency of Japan?",
        "o": ["a) Dollar", "b) Euro", "c) Yen", "d) Peso"],
        "a": "c"
    },
    {
        "q": "Which gas is used by plants to convert sunlight into energy through photosynthesis?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "b"
    },
    {
        "q": "How many bones are there in the adult human body?",
        "o": ["a) 106", "b) 206", "c) 306", "d) 406"],
        "a": "b"
    },
    {
        "q": "Who is known as the father of modern physics?",
        "o": ["a) Isaac Newton", "b) Galileo Galilei", "c) Albert Einstein", "d) Stephen Hawking"],
        "a": "c"
    },
    {
        "q": "What is the chemical symbol for silver?",
        "o": ["a) S", "b) Si", "c) Ag", "d) Au"],
        "a": "c"
    },
    {
        "q": "Which gas do firefighters use to extinguish fires?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Carbon Monoxide"],
        "a": "b"
    }
]

def ask_question(question):
    print(question["q"])
    for option in question["o"]:
        print(option)
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()
    return user_answer

def check_answer(question, user_answer):
    return user_answer == question["a"]

def run_quiz():
    random.shuffle(questions)
    score = 0

    for question in questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['a']}.\n")

    print(f"You got {score}/{len(questions)} questions correct.")

if __name__ == "__main__":
    print("Welcome to the Random Quiz!")
    run_quiz()
import random

questions = [
    {
        "q": "What is the capital of France?",
        "o": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
        "a": "c"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "o": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "a": "b"
    },
    {
        "q": "What is the largest mammal in the world?",
        "o": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Lion"],
        "a": "b"
    },
    {
        "q": "Which gas do plants absorb from the atmosphere?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "b"
    },
    {
        "q": "What is the chemical symbol for gold?",
        "o": ["a) Go", "b) Au", "c) Ag", "d) Gd"],
        "a": "b"
    },
    {
        "q": "How many continents are there on Earth?",
        "o": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "a": "c"
    },
    {
        "q": "Who wrote the play 'Romeo and Juliet'?",
        "o": ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) George Orwell"],
        "a": "c"
    },
    {
        "q": "Which gas makes up the majority of Earth's atmosphere?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "c"
    },
    {
        "q": "What is the largest organ in the human body?",
        "o": ["a) Heart", "b) Brain", "c) Skin", "d) Liver"],
        "a": "c"
    },
    {
        "q": "Which country is known as the Land of the Rising Sun?",
        "o": ["a) China", "b) South Korea", "c) Japan", "d) Thailand"],
        "a": "c"
    },
    {
        "q": "What is the smallest prime number?",
        "o": ["a) 0", "b) 1", "c) 2", "d) 3"],
        "a": "c"
    },
    {
        "q": "In which year did Christopher Columbus first reach the Americas?",
        "o": ["a) 1492", "b) 1512", "c) 1620", "d) 1776"],
        "a": "a"
    },
    {
        "q": "What is the chemical symbol for water?",
        "o": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"],
        "a": "a"
    },
    {
        "q": "Which gas do humans exhale when they breathe out?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Helium"],
        "a": "b"
    },
    {
        "q": "What is the largest planet in our solar system?",
        "o": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
        "a": "d"
    },
    {
        "q": "What is the tallest mountain in the world?",
        "o": ["a) Mount Kilimanjaro", "b) Mount St. Helens", "c) Mount Everest", "d) Mount Fuji"],
        "a": "c"
    },
    {
        "q": "Who painted the Mona Lisa?",
        "o": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Rembrandt"],
        "a": "c"
    },
    {
        "q": "What is the currency of Japan?",
        "o": ["a) Dollar", "b) Euro", "c) Yen", "d) Peso"],
        "a": "c"
    },
    {
        "q": "Which gas is used by plants to convert sunlight into energy through photosynthesis?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "a": "b"
    },
    {
        "q": "How many bones are there in the adult human body?",
        "o": ["a) 106", "b) 206", "c) 306", "d) 406"],
        "a": "b"
    },
    {
        "q": "Who is known as the father of modern physics?",
        "o": ["a) Isaac Newton", "b) Galileo Galilei", "c) Albert Einstein", "d) Stephen Hawking"],
        "a": "c"
    },
    {
        "q": "What is the chemical symbol for silver?",
        "o": ["a) S", "b) Si", "c) Ag", "d) Au"],
        "a": "c"
    },
    {
        "q": "Which gas do firefighters use to extinguish fires?",
        "o": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Carbon Monoxide"],
        "a": "b"
    }
]

def ask_question(question):
    print(question["q"])
    for option in question["o"]:
        print(option)
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()
    return user_answer

def check_answer(question, user_answer):
    return user_answer == question["a"]

def run_quiz():
    random.shuffle(questions)
    score = 0

    for question in questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['a']}.\n")

    print(f"You got {score}/{len(questions)} questions correct.")

if __name__ == "__main__":
    print("Welcome to the Random Quiz!")
    run_quiz()
