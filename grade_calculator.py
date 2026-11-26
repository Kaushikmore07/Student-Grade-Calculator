
# Student Grade Calculator

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


def main():
    name = input("Enter student name: ")
    subjects = ["Biology", "Chemistry", "Physics"]

    marks = []

    for subject in subjects:
        score = float(input(f"Enter {subject} marks (out of 100): "))
        marks.append(score)

    total = sum(marks)
    average = total / len(subjects)
    grade = calculate_grade(average)

    print("\n====== STUDENT REPORT ======")
    print("Name:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(average, 2), "%")
    print("Grade:", grade)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    if all(mark >= 40 for mark in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")


if __name__ == "__main__":
    main()

