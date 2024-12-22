from datetime import datetime


# Функция ввода заголовков заметки и возврат ее результатом функции
def enter_note_titles():
    # Объявляем список для хранения заголовков заметки
    titles = list()
    # Запускаем цикл для ввода заголовков
    while True:
        title = input("Введите заголовок (напишите слово 'стоп' или оставьте пустым для завершения ввода заголовков): ")
        if title in ['', 'стоп']:
            break
        else:
            titles.append(title)
    return titles


# Функция ввода статуса заметки и возврат ее результатом функции
def enter_note_status(note_statuses_list):
    # Запуска цикл, с выводом текущего статуса заметки, и вопрос об изменения текущего статуса
    while True:
        # Выводим меню выбора статуса заметки
        print("Выберите статус заметки:")
        print("\t1. Выполнено")
        print("\t2. В процессе")
        print("\t3. Отложено")
        # Просим произвести выбор варианта
        # Введенные данные сразу преобразовываем в int
        try:
            variant = int(input("\nВаш вариант: "))
        except ValueError:
            input('ОШИБКА: Вы указали неправильный вариант статуса заметки!\nДля повтора нажмите Enter')
            continue
        # Проверяем если выбранный вариант у нас в списке ключей словаря с вариантами статуса
        # Если есть вариант в ключах
        if variant in note_statuses_list.keys():
            return variant
        # Если ключа нет либо неправильный ввод
        else:
            input('ОШИБКА: Вы указали неправильный вариант статуса заметки!\nДля повтора нажмите Enter')


# Функция ввода даты создания заметки и возврат ее результатом функции
def enter_created_date():
    # Создаем вечный цикл на проверку ввода правильной даты
    while True:
        # Дата создания заметки в формате "день-месяц-год", например "10-11-2024"
        temp_created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
        try:
            # Функцией strptime проверяем корректность ввода
            temp_created_date = datetime.strptime(temp_created_date, '%d-%m-%Y')
            # Возвращаем объект datetime
            return temp_created_date
        except ValueError:
            print('Вы указали дату в неправильной формате! Просим повторить ввод в таком формате "день-месяц-год"')


# Функция ввода даты когда заметка истекает (дедлайн) и возврат ее результатом функции
def enter_issue_date():
    # Создаем вечный цикл на проверку ввода правильной даты
    while True:
        # Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"
        temp_issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
        try:
            temp_issue_date = datetime.strptime(temp_issue_date, '%d-%m-%Y')
            # Возвращаем объект datetime
            return temp_issue_date
        except ValueError:
            print('Вы указали дату в неправильной формате! Просим повторить ввод в таком формате "день-месяц-год"')


# Функция вывода содержимого заметок
def print_notes(notes_list, note_statuses_list):
    if not notes_list:
        print("Список заметок пуст!")
        return
    print("\nСписок заметок:")
    print('-' * 100)
    for note_ in notes_list:
        print('Имя пользователя:', note_['username'])
        if len(note_['titles']) == 1:
            print('Заголовок:', note_['titles'][0])
        else:
            print('Заголовки:')
            for title in note_['titles']:
                print('\t-', title)
        print('Описание:', note_['content'])
        print('Статус:', note_statuses_list[note_['status']])
        # ВЫВОДИМ ДАТЫ СОЗДАНИЯ И ДЕДЛАЙНА В СОКРАЩЕННОМ ВИДЕ СОГЛАСНО РАНЕМУ ТЗ
        # print('Дата создания:',datetime.strptime(note_['created_date'], "%Y-%m-%d").strftime("%d-%m"))
        print('Дата создания:', datetime.date(note_['created_date']).strftime("%d-%m"))
        # print('Дедлайн:', datetime.strptime(note_['issue_date'], "%Y-%m-%d").strftime("%d-%m"))
        print('Дедлайн:', datetime.date(note_['issue_date']).strftime("%d-%m"))
        print('-' * 100)

# Функция получения максимального значения note_id словаря заметки в списке заметок
def get_max_note_id(notes):
    # Присваиваем переменной значение 0
    max_value = 0
    # С помощью функции max() ищем максимальное значение в сгенерированном списке из списка заметок
    max_value = max([n['note_id'] for n in notes])
    # Возвращаем значение
    return max_value


# Объявляем словарь с вариантами статусов заметок.
# Каждому варианту статус указываем свою цифру.
note_statuses = {1: 'Выполнено', 2: 'В процессе', 3: 'Отложено'}
# Объявляем словарь для хранения информации о заметке
note = dict()
notes = [
    {'username': 'Алексей', 'titles': ['Заголовок1'], 'content': 'Контент1', 'status': 2,
     'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 1},
    {'username': 'Антон', 'titles': ['Заголовок2', 'Заголовок21', 'Заголовок22', 'Заголовок23'], 'content': 'Контент2',
     'status': 2, 'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 2},
    {'username': 'Петр', 'titles': ['Заголовок3', 'Заголовок31'], 'content': 'Контент3', 'status': 2,
     'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 3},
    {'username': 'Петр', 'titles': ['Заголовок4', 'Заголовок41'], 'content': 'Контент4', 'status': 1,
     'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 4},
    {'username': 'Алексей', 'titles': ['Список покупок'], 'content': 'Купить продукты на неделю', 'status': 1,
     'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 5},
    {'username': 'Мария', 'titles': ['Учеба'], 'content': 'Подготовиться к экзамену', 'status': 1,
     'created_date': datetime(2024, 12, 10), 'issue_date': datetime(2024, 12, 10), 'note_id': 6}
]


#notes = []
print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')
while True:
    # Находим максимальное значение note_id и инкрементируем для получение уникального ID
    note["note_id"] = get_max_note_id(notes) + 1
    # Объявляем переменные и запрашиваем информацию у пользователя
    # Имя пользователя
    note["username"] = input("Введите имя пользователя: ")
    # Добавляем в словарь заметки заголовки, вызвавши функцию ввода заметок
    note["titles"] = enter_note_titles()
    # Описание заметки
    note["content"] = input("Введите описание заметки: ")
    # Присвоение статуса заметки, вызовом функции ввода статуса заметки
    note['status'] = enter_note_status(note_statuses)
    # Присвоение даты создания заметки, вызовом функцией ввода даты создания
    note["created_date"] = enter_created_date()
    # Присвоение даты когда истекает заметка, вызовом функции ввода даты истекания заметки
    note["issue_date"] = enter_issue_date()
    # Добавляем заметку в список заметок
    notes.append(note)
    while True:
        # Выводим текст с предложением о еще одной заметке
        result = input("Хотите добавить ещё одну заметку? (да/нет,стоп):").lower()
        # Делаем проверку ввода пользователя
        # Если пользователь ввел "нет", то выводим список заметок
        if result in ['нет', 'стоп']:
            print_notes(notes, note_statuses)
        # Если пользователь ввел "да", то начинаем добавлять новую заметку
        elif result in ['да']:
            break