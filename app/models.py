import csv
from abc import ABC, abstractmethod
from typing import Any

from tabulate import tabulate

from app.functions import register_report


class RowsInfo:
    def __init__(self, files: list[str]):
        """Инициализация объекта RowsInfo, загрузка данных из файлов."""
        self.rows: list[dict[str, str]] = self.row_list(files)

    def row_list(self, files: list[str]) -> list[dict[str, str]] | list:
        """Объединяет данные из нескольких CSV файлов в один список."""
        students_info = []

        for file_path in files:
            students_list_form_file = self.read_file(file_path)
            if students_list_form_file:
                students_info.extend(students_list_form_file)
            else:
                print(
                    f"Внимание: данные из файла '{file_path}' не были получены или файл отсутствует."
                )

        return students_info

    @staticmethod
    def read_file(file: str) -> list[dict[str, str]] | list:
        """Читает CSV файл и возвращает список словарей."""
        try:
            with open(file, "r", encoding="utf8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            return []


class Report(ABC):
    def __init__(self, headers: list[str], data_files: list[dict[str, str]]):
        """Базовый класс отчета."""
        self.headers: list[str] = headers
        self.data: list[dict[str, str]] = data_files
        self.report_data: list[list[Any]] = self.create_report_data()

    @abstractmethod
    def create_report_data(self) -> list[list]:
        """Создает данные для отчета."""
        pass

    def report(self) -> str:
        """Форматирует отчет в виде строки с помощью библиотеки tabulate."""
        tabulate_obj = tabulate(
            self.report_data,
            headers=self.headers,
            tablefmt="grid",
            floatfmt=".1f",
        )
        return tabulate_obj


@register_report("student-performance")
class StudentPerformance(Report):
    def __init__(self, data_files: list[dict[str, str]]):
        """Отчет с информацией о среднем балле каждого студента."""
        super().__init__(
            headers=["student_name", "grade"], data_files=data_files
        )

    def create_report_data(self) -> list[list]:
        """Создает список данных для отчета: имя студента и средний балл."""
        students: dict[str, list[float]] = {}

        for row in self.data:
            student_name: str = row["student_name"].strip()
            if not student_name:
                continue
            try:
                grade: float = float(row["grade"])
            except (ValueError, TypeError):
                continue

            students.setdefault(student_name, []).append(grade)

        report_data = [
            [student_name, self.get_avg(grades)]
            for student_name, grades in students.items()
        ]
        report_data.sort(key=lambda x: (-float(x[1]), x[0]))

        return report_data

    @staticmethod
    def get_avg(grades: list[float]) -> float:
        """Вычисляет средний балл"""
        return round(sum(grades) / len(grades), 1)
