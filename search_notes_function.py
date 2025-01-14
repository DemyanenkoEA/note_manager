# Grade 1. Этап 3: Задание 4
# Задание: Функция поиска заметок
# Реализация функции поиска. Позволяет пользователю находить записи по ключевым словам или статусу.

# Заметки, соответствующие запросу, не найдены.


from utils_function import validate_status
from display_notes_function import display_notes


def search_notes(notes, keyword=None, status=None):
    # Проверка на пустой список заметок
    if not notes:
        # Выводим сообщение об отсутствии заметок и выходим из функции
        print('У вас нет сохранённых заметок.')
        input('Для продолжения нажмите Enter')
        return []
    # Проверка отсутствия ключевого слова и статуса для поиска
    if not keyword and not status:
        input("Вы не указали ключевое слово и статус для поиска!")
        # Выходим из функции и возвращаем пустой список
        return []
    # Объявляем пустой список найденных заметок
    found_notes = []
    # Цикл поиска по заданным ключам
    for idx, note in enumerate(notes):
        # Проверка на поиск только по ключевому слову
        if keyword and not status:
            # Если по ключевому слову находим совпадение в title, content, username, то добавляем в список найденных
            if (keyword in note['title'].lower() or keyword in note['content'].lower() or
                    keyword in note['username'].lower()):
                found_notes.append(note)
        # Проверка на поиск только по статусу
        elif not keyword and status:
            # Если указанный статус совпадает со статусом заметки, то добавляем в список найденных
            if status == note['status']:
                found_notes.append(note)
        # Проверка на поиск по ключевому слову и статусу
        elif keyword and status:
            # Если по ключевому слову находим совпадение в title, content, username,
            # или указанный статус совпадает со статусом заметки, то добавляем в список найденных
            if (keyword in note['title'].lower() or keyword in note['content'].lower() or
                    keyword in note['username'].lower() or status == note['status']):
                found_notes.append(note)

    if not found_notes:
        print("Заметки, соответствующие запросу, не найдены.")
        input("Для продолжения нажмите Enter")
    return found_notes


if __name__ == '__main__':
    keyword = input("Введите ключевое слово для поиска: ").strip().lower()
    while True:
        status = input("Введите статус для поиска (или оставьте пустым): ").strip().lower()
        if status and not validate_status(status):
            input(
                "Вы вели неправильный статус для поиска.\nВарианты статуса: новая, в процессе, выполнена.\nДля продолжения нажмите Enter")
            continue
        break
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнена',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    found_notes = search_notes(notes, keyword, status)
    display_notes(found_notes)
