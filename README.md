# API для Yatube

REST API социальной сети Yatube на Django REST Framework. Предоставляет endpoints для работы с публикациями, комментариями, сообществами и подписками. Аутентификация через JWT-токены.

## Установка

1. Клонируйте репозиторий:
```bash
git clone <ссылка_на_репозиторий>
cd api-final-yatube-ad
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
cd yatube_api
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```

## Документация API

Документация доступна по адресу: http://127.0.0.1:8000/redoc/

## Примеры запросов

### Получение токена
```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "testuser",
  "password": "password"
}
```

### Получение списка публикаций
```http
GET /api/v1/posts/
```

### Создание публикации
```http
POST /api/v1/posts/
Authorization: Bearer <token>
Content-Type: application/json

{
  "text": "Текст публикации",
  "group": 1
}
```

### Подписка на пользователя
```http
POST /api/v1/follow/
Authorization: Bearer <token>
Content-Type: application/json

{
  "following": "username"
}
```

## Тестирование

```bash
pytest
```

## Технологии

- Python 3.10
- Django 3.2.16
- Django REST Framework 3.12.4
- djangorestframework-simplejwt 4.7.2
- SQLite
