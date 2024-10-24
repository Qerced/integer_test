from sqlalchemy import func
from sqlalchemy.orm import Session

from db import SessionLocal
from model import Student


class CRUDStudents:
    def __init__(self, model, session: Session):
        self.model = model
        self.session = session

    def create_all(self, students: list[Student]):
        with self.session() as session:
            session.add_all(Student(**row) for row in students)
            session.commit()

    def get_by_grade_and_subject(self, grade: int, subject: str):
        with self.session() as session:
            return session.query(self.model).filter(
                self.model.grade >= grade, self.model.subject == subject
            ).all()

    def get_top_students(self):
        with self.session() as session:
            return (
                session.query(self.model.full_name)
                .filter(self.model.grade == 5)
                .group_by(self.model.full_name)
                .having(func.count() >= 2)
                .all()
            )

    def students_on_courses(self):
        with self.session() as session:
            return (
                session.query(
                    self.model.course,
                    func.count(self.model.id).label('student_count')
                )
                .group_by(Student.course)
                .all()
            )


crud_students = CRUDStudents(Student, SessionLocal)
