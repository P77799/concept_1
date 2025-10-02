print("Welcome to the Python Quiz Game!")

score = 0

# Question 1
answer = input("Q1: What does OOP stand for? ")
if answer.lower() == "object oriented programming":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is Object Oriented Programming.")

# Question 2
answer = input("Q2: Which keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'def'.")

# Question 3
answer = input("Q3: What symbol is used for comments in Python? ")
if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong! It is '#'.")

print(f"\nYou got {score}/3 correct!")