"""Calculate a student's grade from a whole-number mark out of 100."""


def calculate_grade(marks):
    """Return the grade and an encouraging message for valid marks."""
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    # Check from highest to lowest so each mark gets one grade.
    if marks >= 90:
        return "A", "Excellent work! Keep challenging yourself."
    elif marks >= 80:
        return "B", "Very good! Keep it up."
    elif marks >= 70:
        return "C", "Good effort! A little more practice will help."
    elif marks >= 60:
        return "D", "You passed! Keep practicing the difficult topics."
    else:
        return "F", "Keep going! Review the basics and try again."


def read_marks():
    """Keep asking until the user enters a whole number from 0 to 100."""
    while True:
        answer = input("Enter marks (0-100): ").strip()
        try:
            marks = int(answer)
        except ValueError:
            print("Please enter a whole number, such as 85.")
            continue

        if 0 <= marks <= 100:
            return marks
        print("Marks must be between 0 and 100. Please try again.")


def main():
    print("Student Grade Calculator")
    print("------------------------")

    name = input("Enter student name: ").strip()
    while not name:
        print("Please enter a student name.")
        name = input("Enter student name: ").strip()

    marks = read_marks()
    grade, message = calculate_grade(marks)

    print(f"\nRESULT FOR {name.upper()}")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. No result was calculated.")
