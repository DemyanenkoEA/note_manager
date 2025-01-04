# Grade 1. Этап 3: Задание 3
# Задание: Функция отображения заметок.
# Отображает каждую заметку в удобном и понятном формате.


from datetime import datetime
from datetime import timedelta
from colorama import init, deinit
from colorama import Back, Style
import os


def display_notes(notes=None, clear=True):
    # Инициализация colorama
    init()
    # Проверка на пустой список заметок
    if not notes:
        # Выводим сообщение об отсутствии заметок и выходим из функции
        print('У вас нет сохранённых заметок.')
        input('Для продолжения нажмите Enter')
        return
    # Очистка экрана консоли
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    # Объявляем список с именами заголовков таблицы
    table_columns = ["Имя пользователя", "Заголовок", "Содержание", "Статус", "Дата создания", "Дедлайн"]
    # Список для хранения максимальной длинны колонок(столбцов)
    max_columns = []
    # Производим расчёт максимальной длинны колонок по заголовкам.
    # Проходимся циклом по списку заголовков. Определяем длину элемента, и записываем ее в добавляемый элемент списка
    for column in table_columns:
        max_columns.append(len(column))
    # Цикл прохождения по списку словарей заметок
    for idx, note in enumerate(notes):
        # Цикл прохождения по каждому значению словаря
        for x, val in enumerate(note.values()):
            # Проверяем максимальную длину значения элемента словаря и значение МАХ длины элемента словаря
            max_columns[x] = max(max_columns[x], len(val))
    # Подсчитываем количество символов.
    # Сумму элементов списка длин заголовков + (количество элементов заголовка умножаем на 2 символа(пробел+|)
    # + 4 символа вывод номера заметки
    amount_symbols = sum(max_columns) + (len(max_columns) * 2) + 4
    # Печатаем строку разделителей с необходимым количеством символов
    print("-" * amount_symbols)
    # Задаем стиль для вывода заголовков
    print(Back.GREEN, end="")
    print(" # |", end="")
    for i, column in enumerate(table_columns):
        print(f'{column:<{max_columns[i] + 1}}|', end="")
    # Сбрасываем стили вывода
    print(Style.RESET_ALL)
    # Печатаем строку разделителей с необходимым количеством символов
    print("-" * amount_symbols)
    # В цикле выводим информацию о заметках
    for i, note in enumerate(notes, start=1):
        print(f'{i:<3}', end='|')
        print(f'{note['username']:<{max_columns[0] + 1}}', end='|')
        print(f'{note['title']:<{max_columns[1] + 1}}', end='|')
        print(f'{note['content']:<{max_columns[2] + 1}}', end='|')
        lower_status = note['status'].lower()
        if lower_status == "новая":
            print(Back.YELLOW + f'{lower_status:<{max_columns[3] + 1}}' + Style.RESET_ALL, end='|')
        elif lower_status == "в процессе":
            print(Back.GREEN + f'{lower_status:<{max_columns[3] + 1}}' + Style.RESET_ALL, end='|')
        elif lower_status == "завершена" or lower_status == "выполнена":
            print(Back.MAGENTA + f'{lower_status:<{max_columns[3] + 1}}' + Style.RESET_ALL, end='|')
        else:
            print(Back.RED + f'{lower_status:<{max_columns[3] + 1}}' + Style.RESET_ALL, end='|')
        print(f'{note['created_date']:<{max_columns[4] + 1}}', end='|')
        print(f'{note['issue_date']:<{max_columns[5] + 1}}|')
        # Печатаем строку разделителей с необходимым количеством символов
        print("-" * amount_symbols)
    # Деинициализация colorama
    deinit()


if __name__ == '__main__':
    while True:
        # Очистка экрана консоли
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Тестирование программы:")
        print("1. Проверка работы функции с пустым списком.")
        print("2. Проверка работы функции с одной заметкой.")
        print("3. Проверка работы функции с несколькими заметками.")
        print("4. Выйти из программы")
        try:
            res = int(input("Сделайте выбор (1,2,3,4):"))
            if res not in [1, 2, 3, 4]:
                raise ValueError(1)
        except ValueError:
            input("Неправильный ввод! Для продолжения нажмите Enter")
            continue
        if res == 1:
            notes = []
            # Вызываем функцию отображение форматированного списка, передача списка аргументом
            display_notes(notes)
        elif res == 2:
            # Создание списка словарей заметок для отладки
            notes = [{'username': 'Алексей', 'title': 'Список покупок',
                      'content': 'Купить продукты на неделю', 'status': 'Новая',
                      'created_date': datetime.now().strftime('%d-%m-%Y'),
                      'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')}
                     ]
            # Вызываем функцию отображение форматированного списка, передача списка аргументом
            display_notes(notes)
            input("Для продолжения нажмите Enter")
        elif res == 3:
            # Создание списка словарей заметок для отладки
            notes = [{'username': 'Алексей', 'title': 'Список покупок',
                      'content': 'Купить продукты на неделю', 'status': 'Новая',
                      'created_date': datetime.now().strftime('%d-%m-%Y'),
                      'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
                     {'username': 'Алексей2', 'title': 'Список покупок тест',
                      'content': 'Купить продукты на неделю2', 'status': 'В процессе',
                      'created_date': datetime.now().strftime('%d-%m-%Y'),
                      'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')}
                     ]
            # Вызываем функцию отображение форматированного списка, передача списка аргументом
            display_notes(notes)
            input("Для продолжения нажмите Enter")
        elif res == 4:
            break
