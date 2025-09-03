# API для Yatube

REST API для социальной платформы Yatube. Позволяет публиковать посты с изображениями, оставлять комментарии, объединять посты в группы и подписываться на авторов. Аутентификация по JWT-токенам. Неавторизованные пользователи имеют доступ только на чтение (кроме эндпоинта подписок — доступен только авторизованным).

## Стек
- Python 3.12+
- Django 4.x / DRF
- Simple JWT (djangorestframework-simplejwt)
- SQLite3 (по умолчанию) / PostgreSQL
- gunicorn (в продакшене)

## Установка и запуск локально

```bash
git clone https://github.com/harrows/api-final-yatube.git
cd api-final-yatube/yatube_api

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
