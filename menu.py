"""
Grade 1. Этап 3: Задание 5
Задание: Создание меню действий
Описание задания
1. Создайте программу, которая выводит интерактивное текстовое меню, позволяющее пользователю выбирать действия.
2. Меню должно:
Отображать список доступных действий.
Выполнять выбранное пользователем действие, вызывая соответствующую функцию.
Повторно показывать меню после завершения действия, пока пользователь не выберет выход.
"""


# Импорт модуля для работы с ОС
import os
from datetime import datetime
from datetime import timedelta
from display_notes_function import display_notes
from create_note_function import create_note
from search_notes_function import search_notes
from utils_function import validate_status
from delete_note import delete_note
from update_note_function import update_note


# Функция отображения пунктов меню
def print_menu():
	# Очистка экрана консоли
	os.system('cls' if os.name == 'nt' else 'clear')
	# Вывод производим построчно, ибо если использовать многострочный вариант пункты меню смещаются с центру экрана
	print('Меню действий:')
	print('1. Создать новую заметку.')
	print('2. Показать все заметки.')
	print('3. Обновить заметку.')
	print('4. Удалить заметку. ')
	print('5. Найти заметки.')
	print('6. Выйти из программы.')


# Проверка запуска локального файла
if __name__ == "__main__":
	# Создание списка словарей заметок для отладки
	notes = [{'username': 'Алексей', 'title': 'Список покупок',
			  'content': 'Купить продукты на неделю', 'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Алексей', 'title': 'Заголовок1', 'content': 'Контент1', 'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Антон', 'title': 'Заголовок2', 'content': 'Контент2',
			  'status': 'новая', 'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Петр', 'title': 'Заголовок3', 'content': 'Контент3', 'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Петр', 'title': 'Заголовок4', 'content': 'Контент4', 'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
			  'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')},
			 {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'новая',
			  'created_date': datetime.today().strftime('%d-%m-%Y'),
			  'issue_date': (datetime.now() + timedelta(days=7)).strftime('%d-%m-%Y')}
			 ]
	# Создание пустого списка заметок
	# notes = []
	while True:
		# Выводим меню
		print_menu()
		# Просим произвести ввод пункта меню, преобразовываем в целочисленную переменную
		try:
			# В случае если не число, вызываем ValueError
			choice = int(input("Ваш выбор: "))
			if choice == 1:
				# Пользователь выбрал "Создать новую заметку"
				# Вызываем функцию создания новой заметки и ее результат в виде словаря добавляем в список заметок
				notes.append(create_note())
				print("Новая заметка создана!\nДля продолжения нажмите Enter")
			elif choice == 2:
				# Пользователь выбрал "Показать все заметки"
				display_notes(notes)
				input("Для продолжения нажмите Enter")
			elif choice == 3:
				# Пользователь выбрал "Обновить заметку"
				if not notes:
					# Выводим сообщение об отсутствии заметок и выходим из функции
					print('У вас нет сохранённых заметок.')
					input('Для продолжения нажмите Enter')
					continue
				else:
					display_notes(notes)
					note_idx = 0
					while True:
						try:
							note_idx = int(input("Введите номер заметки для обновления: ")) - 1
							notes[note_idx] = update_note(notes[note_idx])
							break
						except ValueError:
							input("Неверный ввод.\nДля продолжения Enter.")
							continue
						except IndexError:
							input("Неверный номер заметки.\nДля продолжения нажмите Enter")
							continue
			elif choice == 4:
				# Пользователь выбрал "Удалить заметку"
				display_notes(notes)
				delete_note(notes)
				input("Для продолжения нажмите Enter")
			elif choice == 5:
				# Пользователь выбрал "Найти заметки"
				keyword = input("Введите ключевое слово для поиска: ").strip().lower()
				while True:
					status = input("Введите статус для поиска (или оставьте пустым): ").strip().lower()
					if status and not validate_status(status):
						input(
							"Неправильный ввод статус для поиска.\nВарианты статуса: новая, в процессе, выполнена.\nДля продолжения нажмите Enter")
						continue
					break
				found_notes = search_notes(notes, keyword, status)
				if found_notes:
					display_notes(found_notes)
					input("Для продолжения нажмите Enter")
			elif choice == 6:
				# Пользователь выбрал "Выйти из программы"
				print("Программа завершена. Спасибо за использование!")
				break
			else:
				pause = input("Неверный выбор. Пожалуйста, выберите действие из списка.\nДля продолжения Enter.")
		except ValueError:
			pause = input("Неверный ввод. Пожалуйста, выберите действие из списка.\nДля продолжения Enter.")
			continue
