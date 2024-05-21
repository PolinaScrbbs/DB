# Проект "БД для Микро Пупсича"

## Описание

Проект "БД для Микро Пупсича" представляет собой программу, которая создает DB postgreSQL по models.

## Начало работы

1. Клонируйте репозиторий:

    ```
    git clone https://github.com/PolinaScrbbs/DB.git
    ```

2. Перейдите в каталог проекта:

    ```
    cd my-clinic
    ```

3. Создайте виртуальное окружение:

    ```
    py -m venv .venv
    ```

4. Активируйте виртуальное окружение:

    ```
    .venv/Scripts/Activate
    ```
> Если выдает ошибку, то сначала введите `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, а потом повторите прошлую команду
5. Установите необходимые зависимости:

    ```
    pip install -r requirements.txt
    ```

6. Создайте файл `.env` в корневой директории проекта и заполните его следующими данными:

    ```
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=my_clinic
    DB_USER=postgres
    DB_PASS=your_password
    ```

## Использование

В файле [commands.txt](https://github.com/PolinaScrbbs/DB/blob/master/commands.txt) вы найдете следующие команды:

- `alembic init migrations` - Эта команда создает структуру для управления миграциями в вашем проекте. Вам не нужно ее изменять.

- `alembic revision --autogenerate -m "DataBase creation"` - Создает миграцию в папке с миграциями. Эта команда инициирует создание миграции на основе текущего состояния базы данных.
> "DataBase creation" - это сообщение, описывающее содержимое миграции.

- `alembic upgrade 998d779619ad` - Создает или изменяет базу данных в соответствии с выбранной миграцией, идентифицированной по ее хешу.
>Посмотреть номер можно в названии файла с миграцией, либо внтури, он в самом начале под переменной `revision`

- `alembic upgrade head` - Создает или изменяет базу данных в соответствии с последней миграцией в вашем проекте.

- `uvicorn main:app --reload` - Эта команда запускает ваше приложение с помощью сервера Uvicorn. Вам не нужно ее изменять.

## Ссылки

- [Документация SQLAlchemy](https://docs.sqlalchemy.org/)
- [Документация Alembic](https://alembic.sqlalchemy.org/)
