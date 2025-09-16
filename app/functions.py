from app.reports import REPORTS


def register_report(name: str) -> callable:
    """Декоратор для регистрации класса отчета в словаре REPORTS."""

    def decorator(cls: type) -> type:
        REPORTS[name] = cls
        return cls

    return decorator
