import random


def start_game():
    score = 0
    print("Welcome to Vansh's Math Game!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("Type 'exit' at any time to quit.")


    # Choose operation
    choice = input("Enter 1, 2, 3, or 4: ")


    if choice.lower() == "exit":
        return


    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Exiting game.")
        return


    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)


        # Ensure division is clean (no decimals)
        if choice == "4":
            num1 = num1 * num2  # makes num1 divisible by num2


        # Determine correct answer and symbol
        if choice == "1":
            correct_answer = num1 + num2
            symbol = "+"
        elif choice == "2":
            correct_answer = num1 - num2
            symbol = "-"
        elif choice == "3":
            correct_answer = num1 * num2
            symbol = "×"
        elif choice == "4":
            correct_answer = num1 // num2
            symbol = "÷"


        user_input = input(f"What is {num1} {symbol} {num2}? ")


        if user_input.lower() == "exit":
            break


        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Correct! ")
                score += 1
            else:
                print(f"Incorrect.The correct answer was {correct_answer}.")
        except ValueError:
            print("Please enter a valid number or 'exit'.")


    print(f"Game over! Your final score is: {score}")


if __name__ == "__main__":
    start_game()