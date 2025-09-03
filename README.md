# API для Yatube

Социальная сеть, в которой пользователи могут публиковать посты, комментировать записи и подписываться друг на друга.  
API позволяет работать с функционалом проекта через запросы.

## Стек технологий
- Python 3.12
- Django 5.1
- Django REST Framework 3.15
- Simple JWT (аутентификация по токенам)
- Pillow

## Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:harrows/api-final-yatube.git

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Выполните миграции:
    ```bash
    python manage.py migrate

5. Запустите сервер:
    ```bash
    python manage.py runserver


# Примеры запросов
## Получение списка постов

    GET /api/v1/posts/

    Ответ:

    [
    {
        "id": 1,
        "text": "Первый пост!",
        "author": "user1",
        "pub_date": "2025-09-03T12:00:00Z"
    }
    ]

## Создание комментария к посту

    POST /api/v1/posts/1/comments/

    Тело:

    {
    "text": "Отличный пост!"
    }

## Подписка на пользователя

    POST /api/v1/follow/

    Тело:

    {
    "following": "user2"
    }

## Автор

Автор проекта: Дмитрий