import random

def math_puzzle():
    print("Welcome to the Math Quiz puzzle!!!")
    print("1 - Easy (Addition)")
    print("2 - Medium (Multiplication)")
    print("3 - Hard (Algebra)")
    
    score = 0
    level = int(input("Enter your choice: "))

    for i in range(5):
        if level == 1:   # Easy
            a, b = random.randint(1,15), random.randint(1,20)
            ans = a + b
            print(f"{a} + {b} = ??")

        elif level == 2: # Medium
            a, b = random.randint(1,20), random.randint(1,20)
            ans = a * b
            print(f"{a} * {b} = ??")

        else:            # Hard
            a, b = random.randint(1,20), random.randint(1,20)
            ans = a
            print(f"a + {b} = {a+b}. Find value of a:")

        user = int(input("Enter your answer: "))
        if user == ans:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {ans}\n")

    print(f" Final Score: {score}/5")

math_puzzle()


                
