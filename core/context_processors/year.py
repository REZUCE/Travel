import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    now = datetime.datetime.now()
    years = now.year

    return {
        'year': years
    }
