
marks = int(input("Enter marks (0-100): "))

if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 0:
    grade = "F"
else:
    grade = "Invalid input"

print("Grade:", grade)
