# twich_parser
Данный скрипт предназначен для парсинга данных поиска с сайта twich.tv при помоши библиотеки Selenium.

При первом запуске необходимо запустить файл first_login_to_Twich.py для сохранения данных cookies и последующей упрощенной авторизации.

Файл auth_data.py нужен для хранения ваших логина и пароля для доступа к twich.tv.

После первой авторизации можно перейти к основному файлу tests.py, который и выполняет функцию парсинга данных. 
