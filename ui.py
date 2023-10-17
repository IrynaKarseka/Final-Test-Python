import Note

def menu():
    print("\nВведите цифру для выбора функции:\n",
          " 1 - Создать заметку\n",
          " 2 - Редактировать заметку\n",
          " 3 - Удалить заметку\n",
          " 4 - Вывод заметки по ID\n",
          " 5 - Выборка заметок по дате\n",
          " 6 - Вывод всех заметок\n",
          " 7 - Выход\n")

def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text

def goodbuy():
    print("")
