from datetime import datetime


# Функция проверки корректности даты
def is_valid_date(string: str) -> bool:
    try:
        datetime.strptime(string, '%d-%m-%Y')
        return True
    except ValueError:
        return False


# Функция запроса подтверждения у пользователя.
# С отображением вопроса из параметров функции и сравнение ответа со списком из параметров
def confirm(question: str, answers: []):
    while True:
        answer = input(f'{question} ({",".join(answers[0])}) или ({",".join(answers[1])})').strip()
        if answer in answers[0]:
            return True
        elif answer in answers[1]:
            return False


# Функция проверяет корректность статуса
def validate_status(status):
    return status in ['новая', 'в процессе', 'выполнена']


if __name__ == "__main__":
    if confirm("Test", [['да', 'д'], ['нет', 'н']]):
        print("confirm() return True")
    else:
        print("confirm() return False")

        # while True:
        #     try:
        #         keyword = input("Введите ключевое слово для поиска: ").strip().lower().split()[0]
        #         break
        #     except IndexError:
        #         input("Вы указали пустую строку! Для повторения ввода нажмите Enter")
        #         continue
