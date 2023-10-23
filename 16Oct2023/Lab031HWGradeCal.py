score = int(input("Enter your score"))

if score >= 90:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score <= 59:
    grade = "F"
else:
    grade = "Invalid score"
print(f"the grade for {score} is {grade}")
