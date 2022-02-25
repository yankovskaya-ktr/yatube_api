# YaTube-api

REST-api для базовой версии проекта [Yatube](https://github.com/yankovskaya-ktr/Yatube)

После запуска проекта документация доступна по адресу: http://localhost/redoc/

### Технологии:

Python 3.7, Django 2.2.6, Django REST framework 3.12.4, Simple JWT

### Локальный запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
> git clone https://github.com/yandex-praktikum/yatube_api.git
> cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
> python3 -m venv env
> source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
> python3 -m pip install --upgrade pip
> pip install -r requirements.txt
```

Выполнить миграции:

```
> python3 manage.py migrate
```

Запустить проект:

```
> python3 manage.py runserver
```

### Примеры:
Получение списка постов:
```
GET '/api/v1/posts/'
```
Получение информации о сообществе:
```
GET '/api/v1/groups/{id}/'
```
Добавление комментария к посту:
```
POST '/api/v1/posts/{post_id}/comments/'

Payload:
{
"text": "string"
}
```

