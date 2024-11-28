student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_scores[key] = 'Outstanding'
    elif student_scores[key] > 80 and student_scores[key] < 90:
        student_scores[key] = 'Exceeds Expectations'
    elif student_scores[key] > 70 and student_scores[key] < 80:
        student_scores[key] = 'Acceptable'
    elif student_scores[key] <= 70:
        student_scores[key] = 'Fail'
        
student_grades = student_scores
print(student_grades)