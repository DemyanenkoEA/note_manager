"""
Удаление заметок

Функциональность:
Удаляет заметку по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.
"""
from datetime import datetime, timedelta
from display_notes_function import display_notes

# Создаем список, с вложенными словарями хранящие данные о заметках
notes = [
    {'username': 'Алексей', 'title': 'Заголовок1', 'content': 'Контент1', 'status': 'Новая',
     'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
    {'username': 'Антон', 'title': 'Заголовок2', 'content': 'Контент2',
     'status': 'Новая', 'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
    {'username': 'Петр', 'title': 'Заголовок3', 'content': 'Контент3', 'status': 'Новая',
     'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
    {'username': 'Петр', 'title': 'Заголовок4', 'content': 'Контент4', 'status': 'Новая',
     'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'Новая',
     'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'Новая',
     'created_date': datetime.today().strftime('%d-%m-%Y'),
     'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')}
]


# Для отладки
# notes = list()


# Функция удаления заметки из списка заметок по имени пользователя или заголовку
def delete_note(notes_list):
    if not notes_list:
        print("Список заметок пуст!")
        input("Для продолжения нажмите Enter")
        return
    # Запускаем цикл ввода критерия поиска
    while True:
        # Запрашиваем ввод критерия поиска.
        # Преобразовываем строку в нижний регистр
        search_str = input("Введите имя пользователя или заголовок для удаления заметки:").strip().lower()
        # Проверка если пользователь ввел пустую строку
        if not search_str:
            # Пустая строка критерия, выводим предупреждение
            input("Вы не указали критерий для удаления!\nДля продолжения нажмите Enter")
            continue
        break
    # Переменная флаг указывающая что заметка(и) были найдены
    founded = False
    # Цикл прохождения по списку заметок
    for i, note in enumerate(notes_list):
        # Проверяем существует ли критерий поиска в элементе словаря заметки, а также
        # проверяем критерий поиска в списке заголовков, которые тоже преобразовываем в список с нижним регистром
        if (search_str == note['username'].lower()) or (search_str == note['title'].lower()):
            founded = True
            print("Найдена следующая заметка:")
            display_notes([note], clear=False)
            # Цикл выполнения запроса на удаление
            while True:
                # Запрашиваем строку, преобразовываем строку в нижний регистр
                result = input("Вы уверены, что хотите удалить заметку? (да/нет):").lower()
                # Если пользователь указал "да"
                if result == 'да':
                    # Удаляем заметку из списка словарей заметок занося ее в список на удаление
                    # notes_list.remove(note) - тут вылезет баг
                    notes_list.remove(note)
                    # Выводим сообщение об успешном удалении заметки
                    print("Заметка успешно удаленна!")
                # Если пользователь указал "нет"
                elif result == 'нет':
                    # Выводим сообщение о том что заметка не удалена
                    print('Заметка не удаленна!')
                    break
                # Если пользователь ввел иное, то повторяем цикл сначала
                else:
                    continue
                # После правильного данного ответа да/нет, выходим из цикла
                break
    if not founded:
        print("Заметок с таким именем пользователя или заголовком не найдено!")
    return notes


if __name__ == '__main__':
    # Цикл для проверки работоспособности кода
    while True:
        # Выводим список заметок
        display_notes(notes)
        # Удаляем из списка заметки которые не нужны
        delete_note(notes)
        input("Для продолжения нажмите Enter...")
