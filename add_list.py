import datetime

# Объявляем переменные и запрашиваем информацию у пользователя
# Имя пользователя
username = input("Введите имя пользователя: ")
# Заголовок заметки
title = input("Введите заголовок заметки: ")
# Описание заметки
content = input("Введите описание заметки: ")
# Статус заметки
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
# Дата создания заметки в формате "день-месяц-год", например "10-11-2024"
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
# Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# ОбЪявляем список заголовком заметки
titles = []
# Начало цикла с выполнением три раза
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

# Получаем текущую дату+время
now = datetime.datetime.now()
# Полученную дату форматируем в необходимый формат
temp_created_date = "{}-{}".format(now.day, now.month)
temp_issue_date = issue_date[0:5]

# Вывод значений переменных
print("Имя пользователя:", username)
#print("Заголовок заметки:", title)
print("Заголовки заметки:", titles)

print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
print("Дата создания заметки (форматированная):", temp_created_date)
print("Дата истечения заметки (форматированная):", temp_issue_date)
