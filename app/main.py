import argparse
import sys

from app.models import RowsInfo
from app.reports import REPORTS


class CustomArgumentParser(argparse.ArgumentParser):
    """Чтобы изменить описание ошибок"""

    def error(self, message):
        if "required: --report" in message:
            sys.stderr.write(
                "Ошибка: Необходимо указать параметр --report с названием отчёта."
            )
        elif "required: --files" in message or "argument --files" in message:
            sys.stderr.write(
                "Ошибка: Необходимо указать параметр --files где указать путь к файлу/файлам через пробел."
            )
        elif "argument --report" in message:
            sys.stderr.write(
                f"Ошибка: в --report указать один из отчетов {list(REPORTS.keys())}."
            )
        else:
            sys.stderr.write(f"Ошибка: {message}\n\n")

        sys.exit(2)  # 2 ошибка при разборе аргументов командной строки


def main():
    """Главная функция, запускающая обработку данных и вывод отчета."""
    parser = CustomArgumentParser(description="Анализ успеваемости студентов")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV файлам"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORTS.keys()),
        help="Название отчёта",
    )

    args = parser.parse_args()

    data = RowsInfo(args.files)

    if data.rows:
        rep = REPORTS[args.report](data.rows)
        print(rep.report())
    else:
        print("Данные для отчёта отсутствуют или файлы не были прочитаны.")


if __name__ == "__main__":
    main()
