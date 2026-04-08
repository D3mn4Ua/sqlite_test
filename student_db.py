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

    