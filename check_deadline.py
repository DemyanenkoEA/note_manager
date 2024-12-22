from datetime import datetime
from datetime import date


def print_current_date():
    # Вызываем функцию now(), получаем строку, и форматируем ее в необходимый вид
    cur_date = datetime.now().strftime("%d-%m-%Y")
    # Второй вариант решения данной задачи
    # now = datetime.now()
    # cur_date = "{}-{}-{}".format(now.day, now.month, now.year)
    print("Текущая дата:", cur_date)


# Функция определения текущей даты, и возвращение форматированной строки с текущей датой
def get_current_date():
    # Вызываем функцию now(), получаем строку, и форматируем ее в необходимый вид
    current_date = datetime.now().strftime("%d-%m-%Y")
    # Возвращаем текущую дату
    return current_date


# Функция запроса ввода даты дедлайна заметки, проверки правильности ввода даты
def enter_issue_date():
    # Создаем вечный цикл на проверку ввода правильной даты
    while True:
        # Запрашиваем ввода даты дедлайна
        temp_issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

        # С помощью блока try/except осуществляем корректность введенной
        try:
            # С помощью функции strptime() проверяем введенную дату на необходимый формат
            valid_date = datetime.strptime(temp_issue_date, '%d-%m-%Y')
            # Проверка даты на значение раньше чем сегодня
            # if valid_date <= datetime.now():
            # print("Дата истечения срока заметки не может быть раньше даты создания заметки")
            # continue
            # В случае корректного вода возвращаем стройку с датой из функции
            return valid_date.date()
        # В случае ошибки выводим сообщение и возвращаемся к началу цикла
        except ValueError:
            print('Вы указали дату в неправильной формате! Просим повторить ввод в таком формате "день-месяц-год"')


# Функция проверки переданной ей даты дедлайна с текущей датой, и возвратом разницы дней
# Параметр дата в виде переменной типа date()
def check_issue_date(issue_date):
    # Берем значение текущей даты и вычитаем от переданной даты дедлайна.
    # Получаем разницу количества дней, и далее на основе разницы выводим информацию
    difference_days = issue_date - date.today()
    # Если разница дней равна 0,
    if difference_days.days == 0:
        print("Дедлайн сегодня!")
    # Если разница дней равна 1, то дедлайн истекает завтра
    elif difference_days.days == 1:
        print("Дедлайн истекает завтра!")
    # Если разница дней равна -1, то дедлайн уже истек вчера
    elif difference_days.days == -1:
        print("Внимание! Дедлайн истек вчера!")
    # Если разница дней больше 1, то дедлайн истекает через n дней
    elif difference_days.days > 1:
        # Производим делением с остатком количества дней на 10, чтобы решить какое слово вставлять в предложение
        result = difference_days.days % 10
        # Если количество дней равно 2,3,4... 22,23,24,
        if 2 <= result <= 4:
            word = "дня!"
        else:
            word = "дней!"
        print("До дедлайна осталось ", difference_days.days, word)
    # Если разница дней равна меньше -1, то дедлайн уже истек n количества дней
    elif difference_days.days < -1:
        result = difference_days.days % 10
        if 2 <= result <= 4:
            word = "дня"
        else:
            word = "дней"
        print("Внимание! Дедлайн истёк", abs(difference_days.days), word, "назад!")


# ----------------------------------------------------------------------------------------
# Объявляем слова заметок
note = {'issue_date': datetime.now()}
# Присваиваем элементу issue_date, текущую дату в формате datetime
# Цикл для проверки работоспособности функций
print_current_date()
while True:
    # Вывод текущей даты
    note["issue_date"] = enter_issue_date()
    check_issue_date(note['issue_date'])
    input("Для продолжения проверки нажмите Enter")