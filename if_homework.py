# # function to find average marks
# def to_find_averagemarks(marks):
#     sum_of_marks = sum(marks)
#     total_subjects = len(marks)
#     average_marks = sum_of_marks / total_subjects
#     return average_marks
# marks = [55, 89, 76, 40, 65]
#
# averagemark = to_find_averagemarks(marks)
# print('Your average marks is', averagemark)

def compute_grade(marks):
    if marks >= 80:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = 78
grade = compute_grade(marks)
print('Your grade is', grade)


