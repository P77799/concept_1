import time
import sys
import random

# --- Slow print for intro/outro ---
def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro():
    slow_print("===========================================")
    slow_print("        DAY 30: THE FINAL CHAPTER          ")
    slow_print("===========================================")
    time.sleep(1)
    slow_print("Loading your Python creations...\n")
    time.sleep(1.5)

def outro():
    slow_print("\n===========================================")
    slow_print("      THANK YOU FOR WATCHING MY JOURNEY     ")
    slow_print("===========================================")
    slow_print("From Day 1 to Day 30, this journey was filled with learning, creativity, and growth.")
    slow_print("This is not the end, it's the beginning of something greater.")
    slow_print("Signing off — Pratik Nepali\n")

# --- Projects ---
def calculator(demo=False):
    print("\n--- Calculator ---")
    if demo:
        print("Demo: 12 + 8 = 20")
        time.sleep(1)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("1. Add  2. Subtract  3. Multiply  4. Divide")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Division by zero not allowed.")
        else:
            print("Invalid choice.")

def rock_paper_scissors(demo=False):
    print("\n--- Rock Paper Scissors ---")
    if demo:
        print("You: rock  Computer: scissors  Result: You win!")
        time.sleep(1)
    else:
        choices = ["rock", "paper", "scissors"]
        user = input("Enter rock, paper, or scissors: ").lower()
        comp = random.choice(choices)
        print("Computer chose:", comp)
        if user == comp:
            print("It's a tie.")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("You lose.")

def math_quiz(demo=False):
    print("\n--- Math Quiz Puzzle ---")
    if demo:
        print("Q1: 3 + 4 = 7  Correct")
        print("Q2: 2 + 5 = 7  Correct")
        print("Q3: 6 + 1 = 7  Correct")
        print("Score: 3 / 3")
        time.sleep(1)
    else:
        score = 0
        for i in range(3):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            ans = a + b
            user = int(input(f"What is {a} + {b}? "))
            if user == ans:
                print("Correct!")
                score += 1
            else:
                print("Wrong. The answer was", ans)
        print("Your score:", score, "/ 3")

def banking_system(demo=False):
    print("\n--- Simple Banking System ---")
    class Bank:
        def __init__(self, balance=0):
            self.balance = balance
        def deposit(self, amount):
            self.balance += amount
            print("Deposited:", amount)
        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient funds.")
        def display(self):
            print("Current balance:", self.balance)

    account = Bank()
    if demo:
        print("Demo: Deposited 1000, Withdrew 250, Balance: 750")
        time.sleep(1)
    else:
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                account.deposit(float(input("Enter amount: ")))
            elif choice == "2":
                account.withdraw(float(input("Enter amount: ")))
            elif choice == "3":
                account.display()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

def hangman(demo=False):
    print("\n--- Hangman Game ---")

    # HANGMAN STAGES
    HANGMAN_STAGES = [
        r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
        r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
        r"""
  +---+
  |   |
      |
      |
      |
      |
========="""
    ]

    people = {
        "Sisan Baniya": ["Popular Nepali vlogger", "recently trend on song with Durgesh Thapa"],
        "Ronaldo": ["Famous football player","suuiiiiii"],
        "Ashika Tamang": ["Famous Nepali social worker", "ya mutna thau hoo?"],
        "Eva Giri": ["Current famous female Tik-toker", "xori manxa ko kuttha tanne xori manxa nai hunxa"],
        "Samaya Raina": ["Famous Stand-up comedian", "famous for Dark Humor comedy"],
        "Kavrali Samdi": ["Famous on TikTok for unique group dance", "also famous for wearing tight jeans"],
        "iShowSpeed": ["Energetic streamer from USA", "Biggest Fan of Ronaldo"],
        "Purav Jha": ["Current famous content creator of India", "Member of 'Also known as Human AI'"],
        "Harka sampang":["Famous politician of Nepal","Famous for carrying stone"]
    }

    if demo:
        # Demo mode output
        print("Difficulty: E")
        print("Word: Ronaldo  Guessed correctly!")
        time.sleep(1)
        print(HANGMAN_STAGES[6])
        return

    difficulty = input("Choose difficulty – E (Easy), M (Medium), H (Hard): ").upper()
    lives = {'E': 6, 'M': 5, 'H': 4}[difficulty]
    options = {
        'E': ["Sisan Baniya", "Ronaldo", "Ashika Tamang"],
        'M': ["Eva Giri", "Samaya Raina", "Kavrali Samdi"],
        'H': ["iShowSpeed", "Purav Jha", "Harka sampang"]
    }[difficulty]

    word = random.choice(options)
    hints = people[word]
    guessed = ['-' if c != ' ' else ' ' for c in word]
    print(" ".join(guessed))

    game_over = False
    hint_stage = 0

    while not game_over:
        guess = input("Guess a letter or type 'hint': ").lower()

        if guess == 'hint':
            if hint_stage < len(hints):
                print("Hint:", hints[hint_stage])
                if hint_stage == 1:
                    lives -= 1
                    print("Life deducted for 2nd hint. Lives left:", lives)
                hint_stage += 1
            else:
                print("No more hints available!")

            if lives == 0:
                game_over = True
                print(f"Game over! The word was: {word}\nPolice: Hands up! You are under arrest!!")
            print(HANGMAN_STAGES[min(lives, len(HANGMAN_STAGES)-1)])
            continue

        for pos in range(len(word)):
            if word[pos].lower() == guess:
                guessed[pos] = word[pos]
        print(" ".join(guessed))

        if guess not in word.lower():
            lives -= 1
            print("Lives left:", lives)
            if lives == 0:
                game_over = True
                print(f"Game over! The word was: {word}")

        if '-' not in guessed:
            game_over = True
            print("Booyaha! You win!!!!!!!!!!!!!")

        print(HANGMAN_STAGES[min(lives, len(HANGMAN_STAGES)-1)])

def library_management(demo=False):
    print("\n--- Library Management ---")
    if demo:
        print("Added 'Python Basics'. Books: Python Basics")
        time.sleep(1)
    else:
        library = []
        while True:
            print("\n1. Add Book\n2. View Books\n3. Remove Book\n4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                book = input("Enter book name: ")
                library.append(book)
                print("Book added.")
            elif choice == "2":
                if not library:
                    print("No books available.")
                else:
                    for i, book in enumerate(library, 1):
                        print(i, book)
            elif choice == "3":
                book = input("Enter book name to remove: ")
                if book in library:
                    library.remove(book)
                    print("Book removed.")
                else:
                    print("Book not found.")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

# --- Main Menu ---
def main_menu(demo=False):
    if demo:
        intro()
        calculator(demo=True)
        rock_paper_scissors(demo=True)
        math_quiz(demo=True)
        banking_system(demo=True)
        hangman(demo=True)
        library_management(demo=True)
        outro()
    else:
        intro()
        while True:
            print("\n========== PYTHON UNIVERSE ==========")
            print("1. Calculator")
            print("2. Rock Paper Scissors")
            print("3. Math Quiz Puzzle")
            print("4. Banking System (OOP)")
            print("5. Hangman Game")
            print("6. Library Management")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                calculator()
            elif choice == "2":
                rock_paper_scissors()
            elif choice == "3":
                math_quiz()
            elif choice == "4":
                banking_system()
            elif choice == "5":
                hangman()
            elif choice == "6":
                library_management()
            elif choice == "7":
                outro()
                break
            else:
                print("Invalid choice.")

# --- Run ---
if __name__ == "__main__":
    if "--demo" in sys.argv:
        main_menu(demo=True)
    else:
        main_menu()