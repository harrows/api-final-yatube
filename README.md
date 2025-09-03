
# 🧩 API для Yatube

Социальная сеть: посты, комментарии, подписки.  
Удобный REST API для мобильных приложений и фронтенда.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-0C4B33.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-ff1709.svg)](https://www.django-rest-framework.org/)
[![Auth](https://img.shields.io/badge/Auth-Simple%20JWT-8A2BE2.svg)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-informational.svg)](#-лицензия)

---

## 🗺️ Навигация

- [Возможности](#-возможности)
- [Стек](#-стек)
- [Быстрый старт](#-быстрый-старт)
- [Примеры запросов](#-примеры-запросов)
- [Автор](#-автор)
---

## ✨ Возможности

- Посты с датой публикации и авторством  
- Комментарии к постам  
- Подписки / «читатели»  
- Аутентификация по **JWT** (access/refresh)  
- Пагинация, поиск и фильтры (DRF)  
- Чёткие коды ошибок и стабильные контракты API

> Документация OpenAPI (если включена): `/redoc/` или `/swagger/`.

---

## 🧱 Стек

- **Python** 3.12  
- **Django** 5.1  
- **Django REST Framework** 3.15  
- **Simple JWT**  
- **Pillow**

---

## ⚡ Быстрый старт

```bash
# 1) Клонируйте репозиторий
git clone git@github.com:harrows/api-final-yatube.git
cd api-final-yatube

# 2) Создайте и активируйте виртуальное окружение
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3) Установите зависимости
pip install -r requirements.txt

# 4) Примените миграции и при необходимости создайте суперпользователя
python manage.py migrate
python manage.py createsuperuser

# 5) Запустите сервер разработки
python manage.py runserver
```

Сервер по умолчанию: `http://127.0.0.1:8000/`

---

## 📬 Примеры запросов

### Получить список постов
```http
GET /api/v1/posts/
```

Ответ:
```json
[
  {
    "id": 1,
    "text": "Первый пост!",
    "author": "user1",
    "pub_date": "2025-09-03T12:00:00Z"
  }
]
```

### Создать комментарий к посту
```http
POST /api/v1/posts/1/comments/
Authorization: Bearer <access_token>
Content-Type: application/json
```

Тело:
```json
{ "text": "Отличный пост!" }
```

Ответ:
```json
{
  "id": 42,
  "post": 1,
  "author": "user1",
  "text": "Отличный пост!",
  "created": "2025-09-03T12:30:00Z"
}
```

### Подписаться на пользователя
```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json
```

Тело:
```json
{ "following": "user2" }
```

Ответ:
```json
{
  "user": "user1",
  "following": "user2"
}
```

---


## 👤 Автор

**Дмитрий**  
Если проект понравился — звезда репозиторию всегда к месту ⭐

---
