![yamdb_workflow](https://github.com/KrisNovi/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
### Описание
Проект собирает отзывы пользователей на произведения. Сами произведения в проекте не хранятся,
здесь нельзя посмотреть фильм или послушать музыку.
Посмотреть пример развернутого проекта можно тут:
http://51.250.65.210/api/v1/
### Технологии
См. requirements.txt
### Репозиторий
https://github.com/KrisNovi/yamdb_final

### Для запуска приложения в контейнерах
- клонировать проект из репозитория на github (ссылка выше)
```
git clone git@github.com:KrisNovi/yamdb_final.git
```
- в директории /infra создать файл .env и прописать там следующие переменные окружения:
```
- DB_ENGINE # указываем БД, с которой работаем
- DB_NAME # имя БД
- POSTGRES_USER=postgres # логин для подключения к базе данных
- POSTGRES_PASSWORD # пароль для подключения к БД (установите свой)
- DB_HOST # название сервиса (контейнера)
- DB_PORT # номер порта
```
- из директории /infra смонтировать и запустить контейнеры:
```
docker-compose up -d --build
``` 
- выполнить миграции внутри запущенного контейнера web:
```
docker-compose exec web python manage.py migrate
```
- создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
- собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
### Заполнение базы из .csv файлов
В директории /static/data есть образцы данных в формате .csv для заполнения таблиц базы данных. Отдельно можно заполнить таблицы с пользователями, жанрами, категориями, названиями произведений, ревью и комментариями.
Команды:
```
docker-compose exec web python manage.py import_users
docker-compose exec web python manage.py import_cat
docker-compose exec web python manage.py import_gen
docker-compose exec web python manage.py import_titles
docker-compose exec web python manage.py import_genre_title
docker-compose exec web python manage.py import_reviews
docker-compose exec web python manage.py import_comments
```
### Создание резервной копии базы данных
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

