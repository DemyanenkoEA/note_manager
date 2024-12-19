
titles = []
while True:
    title = input("Введите заголовок (напишите слово 'стоп' или оставьте пустым для завершения ввода заголовков): ")
    if title == '' or title == 'стоп':
        break
    else:
        titles.append(title)

print('Заголовки заметки: ')
for value in titles:
    print(' - ', value)