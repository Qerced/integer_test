from crud import crud_students
from util import load_students_from_excel


crud_students.create_all(load_students_from_excel())

for student in crud_students.get_by_grade_and_subject(
    3, 'Информатика'
):
    print(student.as_dict())

for student in crud_students.get_top_students():
    print(student)

for course, student_count in crud_students.students_on_courses():
    print(f'Курс: {course}, Количество студентов: {student_count}')
