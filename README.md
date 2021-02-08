# skillfactory-module-d7-asemochkin
Практика D7

Для разворачивания проекта на локальном сервере:
1. Скачайте репозиторий на локальный диск и разархивируйте
2. Через командную строку перейдите в текущий каталог проекта (куда разархивировали репозиторий)
3. Установите все зависимости:
```
% pip3 install -r requirements.txt
```
4. Запустите локальный сервер:
```
% python3 manage.py runserver
```
5. Перейдите по адресу http://127.0.0.1:8000 для проверки функциональности

В приложении представлены 4 блока работы с данными: список книг, список авторов, список издательств, список друзей. Для перехода между разделами используйте верхнее меню. Каждый раздел представлен в виде таблицы со списком соответствующих данных. Для добавления записей в таблицу используется кнопка "Добавить .." под таблицей. Для изменения и удаления конкретных записей используются соответствующие пиктограммы справа от полей записи. В таблице списка книг добавлена кнопка удаления должника конкретной книги (очищает соответствующее поле). Для просмотра подробных сведений о книге нужно щёлкнуть по её названию. Добавление изображения к книге возможно только из под администраторского раздела приложения.

В приложении реализована система регистрации и авторизации пользователей как с помощью простого ввода логина и пароля, так и через github. Зарегистрированным пользователям доступно изменение таблиц. Данные обычного пользователя: логин test_users, пароль pass12345. 

6. Для входа в администраторский раздел приложения необходимо в строке браузера ввести:
```
http://127.0.0.1:8000/admin
```
Для входа с учётной записи суперпользователя введите логин admin и пароль 12345