from student_db import Database

db = Database()
db.create_tables()

while True:
    print("\n1. Додати студента")
    print("2. Додати шкільний предмет")
    print("3. Поставити оцінку учню")
    print("4. Змінити оцінку учню")
    print("5. Видалити оцінку учню")
    print("6. Дізнатися оцінку певного учня")
    print("7. Дізнатися семестрову певного учня")
    print("8. Закінчити сессію")

    choice = input("Обери варіант (1-8): ")

    match choice:
        case "1":
            name = input("Ім'я: ")
            age = int(input("Вік: "))

            db.add_student(name, age)

        case "2":
            name = input("Назва: ")
            teacher = input("Викладач: ")

            db.add_subject(name, teacher)

        case "3":
            student_id = int(input("ID студента: "))
            subject_id = int(input("ID предмету: "))
            grade = int(input("Оцінка: "))

            db.add_grade(student_id, subject_id, grade)

        case "4":
            grade_id = int(input("ID оцінки: "))
            grade = int(input("Нова оцінка: "))

            db.update_grade(grade_id, grade)

        case "5":
            grade_id = int(input("ID оцінки: "))

            db.delete_grade(grade_id)

        case "6":
            student_id = int(input("ID студента: "))

            db.get_student(student_id)

        case "7":
            student_id = int(input("ID студента: "))

            db.get_avg_grade(student_id)

        case "8":
            break
