
from datetime import datetime
import time
# Объявляем словарь для хранения информации о заметке
note = {}
# Объявляем переменные и запрашиваем информацию у пользователя
# Имя пользователя
note ["username"] = input("Введите имя пользователя: ")
# Объявляем список для хранения заголовков заметки и вводим три заголовка с помощью цикла
titles = []
for i in range(3):
    # Вводим заголовок с указанием номера заголовка
    title = input(f"Введите заголовок заметки {i + 1}: ")
    # Добавляем в конец списка новый заголовок
    titles.append(title)
# Добавляем в словарь заметки
note ["titles"] = titles
# Описание заметки
note ["content"] = input("Введите описание заметки: ")
# Статус заметки
note ["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
# Дата создания заметки в формате "день-месяц-год", например "10-11-2024"
# Получаем текущую дату+время
now = datetime.now()
note ["created_date"] = datetime.strftime(now, "%d-%m")
#note ["created_date"] = "{}-{}".format(now.day, now.month) # Второй вариант
# Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"
# Создаем вечный цикл на проверку ввода правильной даты
while True:
    temp_issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
    try:
        valid_date = time.strptime(temp_issue_date, '%d-%m-%Y')
    except ValueError:
        print('Вы указали дату в неправильной формате! Просим повторить ввод в таком форматре "день-месяц-год"')
        continue
    note ["issue_date"] = temp_issue_date[0:5]
    break
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
