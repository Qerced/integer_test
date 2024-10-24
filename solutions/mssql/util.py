import pandas as pd


def load_students_from_excel():
    df = pd.read_excel(
        './mssql/students.xlsx', sheet_name='Лист1',
        names=['id', 'full_name', 'birth_date', 'course', 'subject', 'grade']
    )
    return df.to_dict(orient='records')
