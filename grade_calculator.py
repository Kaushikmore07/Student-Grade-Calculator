
# Student Grade Calculator

name = input("Enter your name: ")

marks = []
for i in range(1, 4):
    score = float(input(f"Enter marks for subject {i}: "))
    marks.append(score)

average = sum(marks) / len(marks)

print("\n--- Student Report ---")
print("Name:", name)
print("Average:", round(average, 2))

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")
