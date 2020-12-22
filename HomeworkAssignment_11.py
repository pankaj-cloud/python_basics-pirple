"""
Homework Assignment #11: Error Handling
Details:
As you've been completing the past homework assignments and projects, you've undoubtedly run into errors a few times,
and noticed that if you pass certain types of variables to your functions, they will throw exceptions. Now's your time
to go back and make those functions better (bullet-proof them).
For this assignment you can choose any of the homeworks or projects you've done so far. Pick a function that you know is
particularly problematic and add try/except/finally cases to it so that it can handle the errors more gracefully.

So i have chosen If_homework assignment for this assignment.
"""

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
# from typing import Any

def compute_grade(marks):

    try:
        if marks >= 80:
            grade = 'A'
        elif marks >= 60:
            grade = 'B'
        elif marks >= 50:
            grade = 'C'
        else:
            grade = 'F'
        return grade

    except TypeError:
        print("TypeError: Please type only numbers !")

    except NameError:
        print("NameError, Please type only numbers !")
    except Exception:
        print(Exception)
        print("Exception, Please type only numbers !")
    finally:
        print(" Finally ! ")

        # return grade

marks = 78
grade = compute_grade(marks)
print('Your grade is', grade)
print("\n")

marks = '78'
grade = compute_grade(marks)
print('Your grade is', grade)
print("\n")

marks = ['']
grade = compute_grade(marks)
print('Your grade is', grade)
print("\n")
