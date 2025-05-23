# YatubeApi

## Основные возможности

- **Аутентификация**: Использование JWT-токенов для аутентификации.
- **Посты**: Создание, редактирование, удаление и просмотр постов.
- **Комментарии**: Добавление комментариев к постам.
- **Группы**: Просмотр и управление группами постов.
- **Подписки**: Подписка на других пользователей.

## Установка

1. Клонируйте репозиторий.

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте и примените миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Использование

### Аутентификация

Для работы с API необходимо получить JWT-токен. Используйте следующие эндпоинты:

- **Получение токена**:
  ```bash
  POST /v1/auth/jwt/create/
  Body: {"username": "str", "password": "str"}
  ```

  **Пример ответа**:
  ```json
  {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }
  ```

- **Обновление токена**:
  ```bash
  POST /v1/auth/jwt/refresh/
  Body: {"refresh": "your_refresh_token"}
  ```

  **Пример ответа**:
  ```json
  {
    "access": "your_new_access_token"
  }
  ```

### Примеры запросов и ответов

#### Посты

- **Получить список постов**:
  ```bash
  GET /v1/posts/
  ```

  **Пример ответа**:
  ```json
  [
    {
      "id": 1,
      "text": "Первый пост",
      "pub_date": "2023-10-01T12:00:00Z",
      "author": "user1",
      "group": 1,
      "image": null
    },
    {
      "id": 2,
      "text": "Второй пост",
      "pub_date": "2023-10-02T12:00:00Z",
      "author": "user2",
      "group": null,
      "image": "http://example.com/posts/image.jpg"
    }
  ]
  ```

- **Создать новый пост**:
  ```bash
  POST /v1/posts/
  Body: {"text": "Новый пост", "group": 1}
  ```

  **Пример ответа**:
  ```json
  {
    "id": 3,
    "text": "Новый пост",
    "pub_date": "2023-10-03T12:00:00Z",
    "author": "user1",
    "group": 1,
    "image": null
  }
  ```

- **Получить пост по ID**:
  ```bash
  GET /v1/posts/1/
  ```

  **Пример ответа**:
  ```json
  {
    "id": 1,
    "text": "Первый пост",
    "pub_date": "2023-10-01T12:00:00Z",
    "author": "user1",
    "group": 1,
    "image": null
  }
  ```

- **Обновить пост**:
  ```bash
  PUT /v1/posts/1/
  Body: {"text": "Обновленный пост", "group": 2}
  ```

  **Пример ответа**:
  ```json
  {
    "id": 1,
    "text": "Обновленный пост",
    "pub_date": "2023-10-01T12:00:00Z",
    "author": "user1",
    "group": 2,
    "image": null
  }
  ```

- **Удалить пост**:
  ```bash
  DELETE /v1/posts/1/
  ```

#### Комментарии

- **Получить комментарии к посту**:
  ```bash
  GET /v1/posts/1/comments/
  ```

  **Пример ответа**:
  ```json
  [
    {
      "id": 1,
      "text": "Первый комментарий",
      "created": "2023-10-01T12:00:00Z",
      "author": "user2",
      "post": 1
    }
  ]
  ```

- **Добавить комментарий**:
  ```bash
  POST /v1/posts/1/comments/
  Body: {"text": "Новый комментарий"}
  ```

  **Пример ответа**:
  ```json
  {
    "id": 2,
    "text": "Новый комментарий",
    "created": "2023-10-03T12:00:00Z",
    "author": "user1",
    "post": 1
  }
  ```

- **Обновить комментарий**:
  ```bash
  PUT /v1/posts/1/comments/1/
  Body: {"text": "Обновленный комментарий"}
  ```

  **Пример ответа**:
  ```json
  {
    "id": 1,
    "text": "Обновленный комментарий",
    "created": "2023-10-01T12:00:00Z",
    "author": "user2",
    "post": 1
  }
  ```

- **Удалить комментарий**:
  ```bash
  DELETE /v1/posts/1/comments/1/
  ```

#### Группы

- **Получить список групп**:
  ```bash
  GET /v1/groups/
  ```

  **Пример ответа**:
  ```json
  [
    {
      "id": 1,
      "title": "Группа 1",
      "slug": "group1",
      "description": "Описание группы 1"
    },
    {
      "id": 2,
      "title": "Группа 2",
      "slug": "group2",
      "description": "Описание группы 2"
    }
  ]
  ```

- **Получить группу по ID**:
  ```bash
  GET /v1/groups/1/
  ```

  **Пример ответа**:
  ```json
  {
    "id": 1,
    "title": "Группа 1",
    "slug": "group1",
    "description": "Описание группы 1"
  }
  ```

#### Подписки

- **Получить список подписок**:
  ```bash
  GET /v1/follow/
  ```

  **Пример ответа**:
  ```json
  [
    {
      "user": "user1",
      "following": "user2"
    }
  ]
  ```

- **Подписаться на пользователя**:
  ```bash
  POST /v1/follow/
  Body: {"following": "username"}
  ```

  **Пример ответа**:
  ```json
  {
    "user": "user1",
    "following": "username"
  }
  ```

## Настройки

### Права доступа

- **Посты и комментарии**: Только автор может редактировать или удалять свои посты и комментарии.
- **Подписки**: Пользователь может подписаться только на других пользователей, но не на самого себя.

### Лимиты запросов

- **Аутентифицированные пользователи**: 10,000 запросов в день.
- **Анонимные пользователи**: 1,000 запросов в день.

## Документация API

Документация API доступна по адресу:
- **Redoc**: `/redoc/`
