import pytest
import csv


@pytest.fixture
def csv_files(tmp_path):
    # Создаем два CSV-файла с тестовыми данными
    file1 = tmp_path / "students1.csv"
    file2 = tmp_path / "students2.csv"

    data1 = [
        ["student_name", "subject", "teacher_name", "date", "grade"],
        ["Иванов Иван", "Математика", "Петров Петр", "2023-09-01", "4"],
        ["Петрова Мария", "История", "Сидоров Сидор", "2023-09-02", "5"],
    ]
    data2 = [
        ["student_name", "subject", "teacher_name", "date", "grade"],
        [
            "Семенова Елена",
            "Английский язык",
            "Ковалева Анна",
            "2023-10-10",
            "5",
        ],
    ]

    # Записываем данные в CSV
    with open(file1, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data1)

    with open(file2, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data2)

    return [str(file1), str(file2)]


@pytest.fixture
def sample_rows():
    return [
        {
            "student_name": "Иванов Иван        ",
            "subject": "Математика",
            "teacher_name": "Петров",
            "date": "2023-09-01",
            "grade": "4",
        },
        {
            "student_name": "Иванов Иван   ",
            "subject": "Физика",
            "teacher_name": "Иванов",
            "date": "2023-09-02",
            "grade": "5",
        },
        {
            "student_name": "Иванов Иван",
            "subject": "Физика",
            "teacher_name": "Иванов",
            "date": "2023-09-02",
            "grade": "?",
        },
        {
            "student_name": "Петрова Мария",
            "subject": "История",
            "teacher_name": "Сидорова",
            "date": "2023-09-01",
            "grade": "3",
        },
        {
            "student_name": "Петрова Мария",
            "subject": "Литература",
            "teacher_name": "Иванова",
            "date": "2023-09-02",
            "grade": "4",
        },
        {
            "student_name": "Семенова Елена",
            "subject": "Английский",
            "teacher_name": "Ковалева",
            "date": "2023-09-01",
            "grade": "5",
        },
        {
            "student_name": "Пробелы",
            "subject": "Музыка",
            "teacher_name": "Орлов",
            "date": "2023-09-01",
            "grade": "",
        },
        {
            "student_name": "",
            "subject": "Химия",
            "teacher_name": "Ткаченко",
            "date": "2023-09-01",
            "grade": "5",
        },
        {
            "student_name": "Ошибки",
            "subject": "Биология",
            "teacher_name": "Орлов",
            "date": "2023-09-01",
            "grade": "abc",
        },
        {
            "student_name": " " * 3,
            "subject": "Биология",
            "teacher_name": "Орлов",
            "date": "2023-09-01",
            "grade": "3",
        },
    ]
