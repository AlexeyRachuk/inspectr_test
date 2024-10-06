<h1>Тестовое задание inspectr</h1>

Автор: Алексей Рачук

Email: alexeyrachuk94@gmail.com

Телефон: +7 933 200 56 75

Tg: @raccoon_meh

Стек: python 3.11, django 4.2.16, drf 3.15.2, PostgresQl 14, docker остальные зависимости в requirements.txt

Установлен swagger: /swagger-ui/

.env добавлен специально для корректной сборки на локале.l

<h2>Запуск</h2>

Проект на докере для запуска необходимо выполнить следующее

1) Перейти в корень проекта;
2) Выполнить docker-compose build для сборки;
3) Выполнить docker-compose run --rm back sh -c "python manage.py migrate" для миграций;
4) Есть простая админка, при необходимости нужно завести суперюзера docker-compose run --rm back sh -c "python manage.py createsuperuser"
5) Выполнить сбор статики docker-compose run --rm back sh -c "python manage.py collectstatic", при ошибке изменить конфигурацию в config/settings

На:
```
STATIC_URL = "/static/"
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Пересобрать статику и вернуть:
```
STATIC_URL = "/static/"
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

6) Выполнить docker-compose up для запуска, url проекта на локале: http://localhost:8003/

7) Тестовый файл при необходимости: https://docs.google.com/spreadsheets/d/1vSQZV8qsy0aHLpDbeQGtCTdJ2SbNL3KWDhY6Ul3960k/edit?usp=sharing