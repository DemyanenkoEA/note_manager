"""
Удаление заметок

Функциональность:
Удаляет заметку по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.
"""
from datetime import datetime

# Создаем список, с вложенными словарями хранящие данные о заметках
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

# Для отладки
# notes = list()

# Функция вывода содержимого заметок
def print_notes(notes_list):
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
        print('Статус:', note_['status'])
        # ВЫВОДИМ ДАТЫ СОЗДАНИЯ И ДЕДЛАЙНА В СОКРАЩЕННОМ ВИДЕ СОГЛАСНО РАНЕМУ ТЗ
        # print('Дата создания:',datetime.strptime(note_['created_date'], "%Y-%m-%d").strftime("%d-%m"))
        print('Дата создания:', datetime.date(note_['created_date']).strftime("%d-%m"))
        # print('Дедлайн:', datetime.strptime(note_['issue_date'], "%Y-%m-%d").strftime("%d-%m"))
        print('Дедлайн:', datetime.date(note_['issue_date']).strftime("%d-%m"))
        print('-' * 100)

def print_note(note_):
    print('-' * 100)
    # print("Информация о заметке:")
    print('Имя пользователя:', note_['username'])
    if len(note_['titles']) == 1:
        print('Заголовок:', note_['titles'][0])
    else:
        print('Заголовки:')
        for title in note_['titles']:
            print('\t-', title)
    print('Описание:', note_['content'])
    print('Статус:', note_['status'])
    # ВЫВОДИМ ДАТЫ СОЗДАНИЯ И ДЕДЛАЙНА В СОКРАЩЕННОМ ВИДЕ СОГЛАСНО РАНЕМУ ТЗ
    # print('Дата создания:',datetime.strptime(note_['created_date'], "%Y-%m-%d").strftime("%d-%m"))
    print('Дата создания:', datetime.date(note_['created_date']).strftime("%d-%m"))
    # print('Дедлайн:', datetime.strptime(note_['issue_date'], "%Y-%m-%d").strftime("%d-%m"))
    print('Дедлайн:', datetime.date(note_['issue_date']).strftime("%d-%m"))
    print('-' * 100)
# Функция вывода информации о заметке


# Функция удаления заметки из списка заметок по имени пользователя или заголовку
def delete_note(notes_list):
    if not notes_list:
        print("Список заметок пуст!")
        return
    # Запускаем цикл ввода критерия поиска
    while True:
        # Запрашиваем ввод критерия поиска.
        # Преобразовываем строку в нижний регистр
        search_str = input("Введите имя пользователя или заголовок для удаления заметки:").lower()
        # Проверка если пользователь ввел пустую строку
        if not search_str:
            # Пустая строка критерия, выводим предупреждение
            print("Вы не указали критерий для удаления!")
            # Выходим из функции
            # return
            # Или повторяем ввода критерия
            continue
        # Если строка критерия поиска не пустая, выходим из цикла ввода критерия
        else:
            break
    # Переменная флаг указывающая что заметка(и) были найдены
    founded = False
    # Список для хранения заметок, которые мы нашли согласно критерия и необходимо удалить
    # Так как попался баг, после удаления элемента напрямую из списка во время цикла, пропускается одна строка из
    # смены индексов. В смысле если идут две строки на удаление, то одна удаляется, а следующая пропускается
    need_delete = list()
    # Цикл прохождения по списку заметок
    for note in notes_list:
        # Проверяем существует ли критерий поиска в элементе словаря заметки, а также
        # проверяем критерий поиска в списке заголовков, которые тоже преобразовываем в список с нижним регистром
        if search_str in note['username'].lower() or search_str in [x.lower() for x in note['titles']]:
            founded = True
            print("Найдена следующая заметка:")
            print_note(note)
            # Цикл выполнения запроса на удаление
            while True:
                # Запрашиваем строку, преобразовываем строку в нижний регистр
                result = input("Вы уверены, что хотите удалить заметку? (да/нет):").lower()
                # Если пользователь указал "да"
                if result == 'да':
                    # Удаляем заметку из списка словарей заметок занося ее в список на удаление
                    # notes_list.remove(note) - тут вылезет баг
                    need_delete.append(note)
                    # Выводим сообщение об успешном удалении заметки
                    print("Заметка успешно удаленна!")
                # Если пользователь указал "нет"
                elif result == 'нет':
                    # Выводим сообщение о том что заметка не удалена
                    print('Заметка не удаленна!')
                # Если пользователь ввел иное, то повторяем цикл сначала
                else:
                    continue
                # После правильного данного ответа да/нет, выходим из цикла
                break
    # Если есть что удалять, то удаляем по циклу
    if need_delete:
        for n in need_delete:
            notes.remove(n)
    need_delete.clear()
    if not founded:
        print("Заметок с таким именем пользователя или заголовком не найдено!")


# Цикл для проверки работоспособности кода
while True:
    # Выводим список заметок
    print_notes(notes)
    # Удаляем из списка заметки которые не нужны
    delete_note(notes)
    input("Для продолжения нажмите Enter...")
