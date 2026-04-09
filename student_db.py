import sqlite3 as sql

class Database():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sql.connect("student.db", autocommit=True)
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        if self.cursor and self.connection:
            self.cursor.close()
            self.connection.close()
    
    def create_tables(self):
        self.connect()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(128),
            age INTEGER
        );
        '''
        )

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(64),
            teacher VARCHAR(128)
        );
        '''
        )

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        );
        '''
        )

        self.disconnect()

    def add_student(self, name, age):
        self.connect()

        self.cursor.execute('''
                            INSERT INTO students (name, age) VALUES (?, ?)
                            ''', (name, age)
        )

        self.disconnect()

    def add_subject(self, name, teacher):
        self.connect()

        self.cursor.execute('''
                                INSERT INTO subjects (name, teacher) VALUES (?, ?)
                            ''', (name, teacher)
        )

        self.disconnect()

    def add_grade(self, student_id, subject_id, grade):
        self.connect()

        self.cursor.execute('''
                            INSERT INTO grades (student_id, subject_id, grade) VALUES(?, ?, ?)
                            ''', (student_id, subject_id, grade)
        )

        self.disconnect()

    def update_grade(self, grade_id, grade):
        self.connect()

        self.cursor.execute('''
                            UPDATE grades
                            SET grade = ?
                            WHERE id = ?
                            ''', (grade, grade_id)
        )

        self.disconnect()

    def delete_grade(self, grade_id):
        self.connect()

        self.cursor.execute('''
                            DELETE FROM grades
                            WHERE id = ?
                            ''', (grade_id,)
        )

        self.disconnect()

    def get_student(self, student_id):
        self.connect()

        self.cursor.execute('''
                            SELECT students.name, subjects.name, grades.grade
                            FROM grades
                            JOIN students ON grades.student_id = students.id
                            JOIN subjects ON grades.subject_id = subjects.id
                            WHERE students.id = ?
                            ''', (student_id,)
        )

        results = self.cursor.fetchall()

        self.disconnect()

        student_name = results[0][0]

        print(f"Результати студента {student_name}: ")
        grades_list = [(subject, grade) for _, subject, grade in results]
        print(grades_list)

    def get_avg_grade(self, student_id):
        self.connect()

        self.cursor.execute('''
                            SELECT students.name, AVG(grades.grade)
                            FROM grades
                            JOIN students ON grades.student_id = students.id
                            WHERE students.id = ?
                            ''', (student_id,)
        )
        
        results = self.cursor.fetchone()

        self.disconnect()

        student_name, avg_grade = results
        print(f"Середній бал студента {student_name}: {avg_grade}")