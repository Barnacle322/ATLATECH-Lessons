# Проект: Каталог фильмов 🎬

Мини-веб-приложение на Flask, в котором можно смотреть список фильмов, открывать страницу каждого фильма и добавлять новые через форму.

Проект построен так, чтобы ты использовал то, что уже знаешь (роуты, `render_template`, передача аргументов, базовый Jinja, HTML+CSS), и заодно освоил несколько новых, но несложных вещей.

---

## Что нового ты узнаешь

1. **Наследование шаблонов** (`extends`, `block`) — чтобы не копипастить шапку на каждой странице.
2. **Динамические URL** (`<int:movie_id>`) — чтобы один роут обслуживал страницы всех фильмов.
3. **Обработка POST-форм** — приём данных от пользователя через `request.form`.
4. **`redirect` и `url_for`** — правильное перенаправление и генерация ссылок.
5. **Подключение CSS из папки `static/`**.
6. **Простая валидация ввода**.

---

## Описание

Нужно сделать каталог фильмов. На главной видно список всех фильмов, можно кликнуть на любой и попасть на страницу с подробностями. Также есть форма, через которую можно добавить новый фильм.

Базы данных пока никакой не будет — все фильмы хранятся в обычном списке Python прямо в `app.py`. После перезапуска сервера добавленные фильмы исчезнут, и это нормально.

---

## Функциональные требования

### `/` — Главная

- Заголовок «Мой каталог фильмов».
- Список всех фильмов: название и год.
- Каждое название — ссылка на страницу деталей фильма.
- В шапке ссылки: «Главная», «Добавить фильм».

### `/movie/<int:movie_id>` — Страница фильма

- Поля: название, год, режиссёр, жанр, рейтинг (1–10), описание.
- Кнопка «Назад к списку».
- Если фильма с таким id нет — показать страницу «Фильм не найден» (или вернуть 404).

### `/add` — Добавление фильма

- При GET — показать форму.
- При POST — провалидировать данные, добавить фильм в список, сделать `redirect` на главную.
- Валидация: название обязательно, год и рейтинг — числа, рейтинг от 1 до 10.

### `/delete/<int:movie_id>` — (необязательно)

- Удалить фильм из списка, сделать `redirect` на главную.

---

## Структура проекта

```
movie_catalog/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── movie.html
    ├── add.html
    └── not_found.html
```

---

## «База данных»

Просто список словарей в `app.py`:

```python
movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "director": "Кристофер Нолан",
        "genre": "Научная фантастика",
        "rating": 9,
        "description": "Команда исследователей отправляется через червоточину в поисках нового дома для человечества."
    },
    {
        "id": 2,
        "title": "Лицо со шрамом",
        "year": 1983,
        "director": "Брайан Де Пальма",
        "genre": "Криминал",
        "rating": 8,
        "description": "История кубинского эмигранта, ставшего наркобароном Майами."
    },
]
```

Чтобы новый фильм получал уникальный id:

```python
new_id = max([m["id"] for m in movies], default=0) + 1
```

---

## Стартовый код

`app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movies = [
    # ... твои стартовые фильмы ...
]


@app.route("/")
def index():
    return render_template("index.html", movies=movies)


# Здесь должны быть остальные роуты: /movie/<int:movie_id>, /add, и т.д.


if __name__ == "__main__":
    app.run(debug=True)
```

---

# Справочник

Если что-то из нового непонятно — смотри сюда.

## 1. Наследование шаблонов

Чтобы не повторять шапку, подвал и подключение CSS в каждом файле, делаем базовый шаблон `base.html`:

```html
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <title>{% block title %}Мой сайт{% endblock %}</title>
        <link
            rel="stylesheet"
            href="{{ url_for('static', filename='style.css') }}"
        />
    </head>
    <body>
        <header>
            <a href="{{ url_for('index') }}">Главная</a>
            <a href="{{ url_for('add') }}">Добавить фильм</a>
        </header>
        <main>{% block content %}{% endblock %}</main>
    </body>
</html>
```

Дочерние шаблоны наследуют его:

```html
{% extends "base.html" %} {% block title %}Главная{% endblock %} {% block
content %}
<h1>Каталог фильмов</h1>
<ul>
    {% for movie in movies %}
    <li>
        <a href="{{ url_for('show_movie', movie_id=movie.id) }}">
            {{ movie.title }}
        </a>
        ({{ movie.year }})
    </li>
    {% endfor %}
</ul>
{% endblock %}
```

`{% block %}` в base — это «дырка», которую заполняет дочерний шаблон.

## 2. Динамические URL

```python
@app.route("/movie/<int:movie_id>")
def show_movie(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        return render_template("not_found.html"), 404
    return render_template("movie.html", movie=movie)
```

- `<int:movie_id>` — Flask сам приведёт часть URL к `int` и передаст в функцию под именем `movie_id`.
- Если хочешь строку — `<string:slug>`, если без указания типа — `<slug>` (по умолчанию строка).
- Альтернатива ручному 404: `from flask import abort` и `abort(404)`.

## 3. Обработка форм (POST)

```python
from flask import request, redirect, url_for

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        year = request.form.get("year", "").strip()
        director = request.form.get("director", "").strip()
        genre = request.form.get("genre", "").strip()
        rating = request.form.get("rating", "").strip()
        description = request.form.get("description", "").strip()

        # --- валидация ---
        errors = []
        if not title:
            errors.append("Название обязательно")
        try:
            year_int = int(year)
        except ValueError:
            errors.append("Год должен быть числом")
            year_int = None
        try:
            rating_int = int(rating)
            if not (1 <= rating_int <= 10):
                errors.append("Рейтинг должен быть от 1 до 10")
        except ValueError:
            errors.append("Рейтинг должен быть числом")
            rating_int = None

        if errors:
            # передаём ошибки И ранее введённые значения, чтобы юзер не вводил всё заново
            return render_template(
                "add.html",
                errors=errors,
                form={
                    "title": title, "year": year, "director": director,
                    "genre": genre, "rating": rating, "description": description,
                },
            )

        new_movie = {
            "id": max([m["id"] for m in movies], default=0) + 1,
            "title": title,
            "year": year_int,
            "director": director,
            "genre": genre,
            "rating": rating_int,
            "description": description,
        }
        movies.append(new_movie)
        return redirect(url_for("index"))

    return render_template("add.html")
```

HTML-форма:

```html
{% extends "base.html" %} {% block title %}Добавить фильм{% endblock %} {% block
content %}
<h1>Добавить фильм</h1>

{% if errors %}
<ul class="errors">
    {% for error in errors %}
    <li>{{ error }}</li>
    {% endfor %}
</ul>
{% endif %}

<form method="POST" action="{{ url_for('add') }}">
    <label
        >Название:
        <input
            type="text"
            name="title"
            value="{{ form.title if form else '' }}"
            required
        />
    </label>
    <label
        >Год:
        <input
            type="number"
            name="year"
            value="{{ form.year if form else '' }}"
            required
        />
    </label>
    <label
        >Режиссёр:
        <input
            type="text"
            name="director"
            value="{{ form.director if form else '' }}"
        />
    </label>
    <label
        >Жанр:
        <input
            type="text"
            name="genre"
            value="{{ form.genre if form else '' }}"
        />
    </label>
    <label
        >Рейтинг (1–10):
        <input
            type="number"
            name="rating"
            min="1"
            max="10"
            value="{{ form.rating if form else '' }}"
        />
    </label>
    <label
        >Описание:
        <textarea name="description">
{{ form.description if form else '' }}</textarea
        >
    </label>
    <button type="submit">Добавить</button>
</form>
{% endblock %}
```

Важные моменты:

- `methods=["GET", "POST"]` — без этого Flask не примет POST.
- `request.form.get("title", "")` — безопаснее, чем `request.form["title"]` (не упадёт, если поля нет).
- После успешной обработки POST — **всегда** делай `redirect`, а не `render_template`. Иначе пользователь обновит страницу — и форма отправится повторно.

## 4. `url_for` вместо хардкода ссылок

❌ Плохо:

```html
<a href="/movie/1">Фильм</a>
```

✅ Хорошо:

```html
<a href="{{ url_for('show_movie', movie_id=movie.id) }}">{{ movie.title }}</a>
```

`url_for` принимает **имя функции** (а не путь) и параметры маршрута. Если потом переименуешь URL в `@app.route(...)` — все ссылки обновятся сами.

## 5. Static-файлы

Папка `static/` в корне проекта. Подключение CSS:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />
```

Картинки точно так же:

```html
<img
    src="{{ url_for('static', filename='posters/interstellar.jpg') }}"
    alt="Постер"
/>
```

## 6. Шаблон «фильм не найден»

`not_found.html`:

```html
{% extends "base.html" %} {% block title %}Не найдено{% endblock %} {% block
content %}
<h1>Фильм не найден 😢</h1>
<a href="{{ url_for('index') }}">Вернуться к списку</a>
{% endblock %}
```

---

## Шпаргалка по Jinja (на всякий случай)

Вывод переменной:

```html
{{ movie.title }}
```

Доступ к полю словаря (две формы, обе работают):

```html
{{ movie.title }} {{ movie["title"] }}
```

Цикл:

```html
{% for movie in movies %}
<li>{{ movie.title }} ({{ movie.year }})</li>
{% endfor %}
```

Условие:

```html
{% if movie.rating >= 8 %}
<span class="top">Топ!</span>
{% elif movie.rating >= 5 %}
<span>Норм</span>
{% else %}
<span>Слабо</span>
{% endif %}
```

Длина списка:

```html
Всего фильмов: {{ movies|length }}
```

---

## Минимальный CSS (если совсем не хочется заморачиваться)

`static/style.css`:

```css
body {
    font-family: system-ui, sans-serif;
    max-width: 720px;
    margin: 0 auto;
    padding: 20px;
    color: #222;
}

header {
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

header a {
    margin-right: 15px;
    text-decoration: none;
    color: #0066cc;
}

ul {
    list-style: none;
    padding: 0;
}
li {
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}

label {
    display: block;
    margin: 10px 0;
}

input,
textarea {
    display: block;
    width: 100%;
    padding: 6px;
    margin-top: 4px;
    box-sizing: border-box;
}

button {
    margin-top: 15px;
    padding: 8px 16px;
    background: #0066cc;
    color: white;
    border: none;
    cursor: pointer;
}

.errors {
    background: #ffe0e0;
    border: 1px solid #ff8080;
    padding: 10px;
    border-radius: 4px;
}
```

---

## Бонус (по желанию, для тех, кому скучно)

1. **Сортировка** списка по году или рейтингу — через query-параметр, например `/?sort=year`. Доступ: `request.args.get("sort")`.
2. **Поиск** по названию — поле ввода на главной, фильтрация списка.
3. **Редактирование** фильма — `/edit/<int:movie_id>` с такой же формой, как `/add`, но заполненной.
4. **Средний рейтинг** всех фильмов на главной.
5. **Постеры** — поле `poster` со ссылкой или путём к картинке в `static/posters/`.
6. **Фильтр по жанру** — например, `/?genre=Драма`.

---

## Критерии оценки

- ✅ Все обязательные роуты работают (`/`, `/movie/<id>`, `/add`).
- ✅ Используется наследование шаблонов (`base.html` + `extends`).
- ✅ В шаблонах нет хардкода ссылок — везде `url_for`.
- ✅ Форма корректно обрабатывает POST и делает `redirect` после успешного добавления.
- ✅ Есть базовая валидация ввода.
- ✅ Подключён CSS из `static/`, страницы выглядят аккуратно.
- ✅ Код читаемый, без бессмысленной копипасты.

---

## Сдача

1. Залей проект на GitHub.
2. В `README.md` укажи, как запустить:

    ```bash
    pip install flask
    python app.py
    ```

3. Скинь ссылку.
