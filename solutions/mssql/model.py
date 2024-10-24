from sqlalchemy import NVARCHAR, Column, Date, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    full_name = Column(NVARCHAR(100))
    birth_date = Column(Date)
    course = Column(Integer)
    subject = Column(NVARCHAR(100))
    grade = Column(Integer)

    def as_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'birth_date': self.birth_date,
            'course': self.course,
            'subject': self.subject,
            'grade': self.grade
        }
