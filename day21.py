class Calculator:
    def __init__(self, value=0):
        self.value = value

    @staticmethod
    def Add(num1, num2):
        print("Result =", num1 + num2)

    @staticmethod
    def Subtract(num1, num2):
        print("Result =", num1 - num2)

    @staticmethod
    def Multiply(num1, num2):
        print("Result =", num1 * num2)

    @staticmethod
    def Divide(num1, num2):
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print("Result =", num1 / num2)


def main():
    print("Welcome to the Pratik Calculator!!!!!")
    while True:
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:
            # Take input numbers
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))

            if choice == 1:
                Calculator.Add(n1, n2)
            elif choice == 2:
                Calculator.Subtract(n1, n2)
            elif choice == 3:
                Calculator.Multiply(n1, n2)
            elif choice == 4:
                Calculator.Divide(n1, n2)

        elif choice == 5:
            print("Exiting Calculator... Bye ")
            break
        else:
            print("Invalid choice, please try again!")


main()    
           
    






    








   