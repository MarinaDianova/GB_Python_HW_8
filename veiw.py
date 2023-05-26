"""Логика отображения: что и в каком виде выводится в консоль"""

def clear_console(): # Очищаем консоль
    import os
    return os.system('cls')

def greetings(): # Приветствие
    print('Вас приветсвует телефонный справочник версии 1.1\n\n\t\t(◕‿◕ )')

def bye(): # Прощание
    print('Спасибо за использование справочника!\n\n\t\t(◕‿◕ )\n')
    
def formated_prnt(text): # форматируем текст
    print(f'\n{text}', end='')

def italic_txt(txt): # текст курсивом. Добавим красоты
    return f"\x1B[3m{txt}\x1B[0m"

def menu(): # Печать меню
    print(
        'МЕНЮ:\n'
        '1 - Вывод списка контактов\n'
        '2 - Добавить контакт\n'
        '3 - Удалить контакт\n'
        '4 - Выход\n'
    )


# #Тесты
# clear_console()
# greetings()
# bye()
# formated_prnt('Проверка связи')
# print()
# print(italic_txt('Проверка связи'))
# print(menu())

