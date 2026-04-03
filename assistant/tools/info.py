from datetime import datetime


def greet(name: str) -> str:
    current_hour = datetime.now().hour

    if current_hour > 6 and current_hour < 12:
        return f"Доброе утро {name}"
    elif current_hour > 12 and current_hour < 18:
        return f"Добрый день {name}"
    elif current_hour > 18 and current_hour < 23:
        return f"Добрый вечер {name}"
    else:
        return f"Доброй ночи {name}"


def show_info() -> None:
    now = datetime.now()

    print(f"📅 Сегодня: {now.strftime('%d.%m.%Y')}")
    print(f"🕐 Время: {now.hour}:{now.minute}")
