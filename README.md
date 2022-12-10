# Локальный запуск:
```
git clone https://github.com/qutoq/cardmanager.git
```
Перейти в cardmanager/

Установка используемых библиотек:
```
pip install -r requirements.txt
```
Запуск локального сервера:

```
python3 manage.py createsuperuser
python3 manage.py runserver
```
По умолчанию создана бд с тестовыми данными. 

----------

Но если они не нужны то можно удалить db.sqlite3 и выполнить: 

```
python3 manage.py migrate --run-syncdb
```
