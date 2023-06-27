# Travel
Учебный проект. В нем реализован поиск билетов на автобусы по дате, оформление этих билетов и отправка на почту билета.
![image](https://github.com/REZUCE/Travel/assets/94435629/29d5ea88-682b-4b24-bda0-88e2aab6a0ca)
![image](https://github.com/REZUCE/Travel/assets/94435629/f1e9cafb-9e6d-427d-bd7e-18fe406a605c)
Оформление билета, только если пользователь авторизирован.
![image](https://github.com/REZUCE/Travel/assets/94435629/1d85775b-1c8c-49c5-a174-51cbcc873560)
![image](https://github.com/REZUCE/Travel/assets/94435629/4ee523ed-668d-4571-95cb-989c2d0b602e)
![image](https://github.com/REZUCE/Travel/assets/94435629/4f80491c-6167-475e-98b0-f1df4ec64297)



## Технологии
- Python 3.11.3
- Django 4.2.1
- mysqlclient 2.1.1
- Bootstrap 5
- js чуть-чуть

## Запуск проекта в dev-режиме

1. Клонировать репозиторий и перейти в него в командной строке:

    ```bash
        git clone <ссылка с git-hub>
    ```

2. Cоздать виртуальное окружение:

    windows

    ```bash
        python -m venv venv
    ```

    linux

    ```bash
        python3 -m venv venv
    ```

3. Активируйте виртуальное окружение

    windows

    ```bash
          source venv/Scripts/activate
    ```

    linux

    ```bash
        source venv/bin/activate
    ```

4. Установите зависимости из файла requirements.txt

    ```bash
        pip install -r requirements.txt
    ```

5. Подключите бд MySQL в settings.py

   ![image](https://github.com/REZUCE/Travel/assets/94435629/84f66fed-c9d7-4fa0-9bd7-125940a16174)

   
7. В папке с файлом manage.py выполните миграции:
   windows

    ```bash
        python manage.py migrate
    ```

    linux
   
    ```bash
        python3 manage.py migrate
    ```

8. В папке с файлом manage.py выполните команду:

    windows

    ```bash
        python manage.py runserver
    ```

    linux
   
    ```bash
        python3 manage.py runserver
    ```
