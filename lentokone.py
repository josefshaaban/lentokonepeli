import mysql.connector
import random 
import os 
import time
from random import randint



connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2006",
    database="lentokone", 
    autocommit=True
)

def clean():
    os.system('cls')

def start_game():
    clean()
    print("Welcome to the Flight Game!")
    print("You will be asked a series of questions about flights.")
    print("Try to answer as many questions correctly as possible.")
    input("Press Enter to start the game...")
    score = 0
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    cursor.close()
    
    random.shuffle(questions)
    for question in questions[:20]:
        clean()
        print(question[1])
        print()
        options = question[2].split(",")
        letters = ['a', 'b', 'c', 'd', 'e', 'f']
        for i, option in enumerate(options):
            print(f"{letters[i]}. {option}")
        answer = input("\nEnter the letter of your answer: ").lower()
        if answer in letters and options[letters.index(answer)] == question[4]:
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was: {question[3]}")
        time.sleep(2)
    
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (%s, %s)", ("Player", score))
    cursor.close()
    print(f"Your final score is: {score}")
    input("Press Enter to return to the main menu...")

def check_score():
    clean()
    print("--------------------------------------------------------\n" \
    "   We are showcasing the scoreboard now " \
    "---------------------------------------------------------------------"  )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC")
    scores = cursor.fetchall()
    cursor.close()
    for score in scores:
        print(f"Player: {score[1]}, Score: {score[2]}") 
    input("Press Enter to return to the main menu...")
    

def main():
    while True:
        clean()
        print("1. Start the game")
        print("2. Check the score")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_game()
        elif choice == "2":
            check_score()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

main()