from app.models import RowsInfo, StudentPerformance


def test_rows_info_read_and_combine(csv_files):
    rows_info = RowsInfo(csv_files)

    assert len(rows_info.rows) == 3  # Все записи из двух файлов

    student_names = {row["student_name"] for row in rows_info.rows}
    assert student_names == {"Иванов Иван", "Петрова Мария", "Семенова Елена"}


def test_rows_info_file_not_found(capfd):
    rows_info = RowsInfo(["no_such_file.csv"])
    assert rows_info.rows == []

    out, err = capfd.readouterr()
    assert (
        "Внимание: данные из файла 'no_such_file.csv' не были получены или файл отсутствует."
        in out
    )


def test_student_performance_report(sample_rows):
    report = StudentPerformance(sample_rows)
    data = report.report_data

    # Проверяем наличие студентов с корректными оценками
    names = [row[0] for row in data]
    assert "Иванов Иван" in names
    assert "Петрова Мария" in names
    assert "Семенова Елена" in names
    assert "Пробелы" not in names
    assert "" not in names
    assert "Ошибки" not in names
    assert " " * 3 not in names

    # Проверяем средние баллы
    assert data == [
        ["Семенова Елена", 5.0],  # 5 / 1
        ["Иванов Иван", 4.5],  # (4 + 5) / 2
        ["Петрова Мария", 3.5],  # (3 + 4) / 2
    ]

    # Проверка сортировки по среднему баллу и имени
    sorted_students = sorted(data, key=lambda student: student[0])  # по имени
    sorted_students.sort(
        key=lambda student: student[1], reverse=True
    )  # по среднему баллу
    assert sorted_students == data
