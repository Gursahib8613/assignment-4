marks = int(input("Enter marks: "))

if marks < 25:
    grade = 'F'
elif marks >= 25 and marks < 45:
    grade = 'E'
elif marks >= 45 and marks < 50:
    grade = 'D'
elif marks >= 50 and marks < 60:
    grade = 'C'
elif marks >= 60 and marks < 80:
    grade = 'B'
elif marks >= 80:
    grade = 'A'

print("Grade:",grade)
