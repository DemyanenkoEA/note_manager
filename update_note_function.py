from datetime import datetime
from datetime import timedelta
# Импортирование своих функции
from utils_function import is_valid_date
from utils_function import confirm


#  Функция обновления данных заметки
# Аргумент:
#   note : Словарь с элементами данных заметки
def update_note(note: {}):
    # Список разрешенных полей для редактирования
    allow_keys = ['username', 'title', 'content', 'status', 'issue_date']
    # Цикл повторения изменений значений словаря заметки
    while True:
        # Вводим название элемента для редактирования. Обрезаем лишние пробелы, устанавливаем нижний регистр
        key_name = input(
            'Какие данные вы хотите обновить? (username, title, content, status, issue_date): ').strip().lower()
        # Проверяем есть ли указанный элемент в списке разрешенных
        if key_name in allow_keys:
            # Запрашиваем ввод нового значения. Обрезаем лишние пробелы.
            new_value = input(
                f'Введите новое значение для {key_name} (пустая строка - оставить данные без изменений):').strip()
            # Проверка пустой строки
            if not new_value:
                input("Вы оставили данные без изменений! Для продолжения нажмите Enter")
            # Если ввели новые данные
            else:
                # Если элемент даты дедлайна
                if key_name == 'issue_date':
                    # Цикл проверки и ввода даты
                    while True:
                        # Проверяем на корректную дату или пустую строку после повторного ввода
                        if is_valid_date(new_value) or not new_value:
                            break
                        else:
                            print('Вы указали неверные данные для поля "issue_date"!', end=" ")
                            print("Данные укажите в формате 'день-месяц-год'")
                            new_value = input(
                                f'Введите новое значение для {key_name} (пустая строка - оставить данные без изменений):').strip()
                if new_value:
                    print(f'Вы указали новые данные "{new_value}" для поля "{key_name}"')
                    if confirm('Вы уверены, что хотите обновить данные?', [['да', 'д'], ['нет', 'н']]):
                        note[key_name] = new_value
        if confirm('Желаете еще изменить данные о заметки?', [['да', 'д'], ['нет', 'н']]):
            continue
        else:
            return note


if __name__ == "__main__":
    # Создание списка словарей заметок для отладки
    notes = [{'username': 'Алексей', 'title': 'Список покупок',
              'content': 'Купить продукты на неделю', 'status': 'Новая',
              'created_date': datetime.now().strftime('%d-%m-%Y'),
              'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')}]
    print("Текущие данные заметки:\n", notes[0])

    notes[0] = update_note(notes[0])

    print('Заметка обновлена:\n', notes[0])
