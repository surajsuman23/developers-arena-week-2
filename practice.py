"""Small Week 2 exercises. Run this file separately from the main project."""


def rectangle_area(length, width):
    return length * width


def calculator(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            return "Cannot divide by zero."
        return first / second
    else:
        return "Choose +, -, * or /."


def main():
    # Change these example values to explore each condition.
    hour = 15
    if hour < 12:
        print("Good morning!")
    elif hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")

    print("Numbers from 1 to 100:")
    for number in range(1, 101):
        print(number, end=" ")
    print()

    print("Area of a 5 by 3 rectangle:", rectangle_area(5, 3))
    for operation in ["+", "-", "*", "/"]:
        print(f"12 {operation} 4 = {calculator(12, 4, operation)}")

    age = 20
    if age < 13:
        print("Age category: child")
    elif age < 18:
        print("Age category: teenager")
    else:
        print("Age category: adult")

    # A small guessing game uses a loop, comparisons and error handling.
    secret_number = 7
    while True:
        try:
            guess = int(input("Guess a number from 1 to 10: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not 1 <= guess <= 10:
            print("Choose a number from 1 to 10.")
        elif guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Correct! Well done.")
            break


if __name__ == "__main__":
    main()
