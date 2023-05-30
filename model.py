"""Тут работа с файлами: чтение; запись"""

def contact_lst(): # преобразует строки содержащиеся в файле в список (массив), каждый элемент которого это тоже список длинной 2, на первом месте которого Имя_контакта, а на втором Номер_контакта. При вводе они разделялись функийей input_add_check() с помощью ' ; ', на этой основе они и сепарировались.
    cnt = 0 # счетчик, для определения количества вызова функции
    if cnt == 0: # эта функция вызывается впервые, файла еще нет, этим условием создаем его
        file = open('file.txt', 'a', encoding='utf-8')
        file.close()
    file = open('file.txt', 'r', encoding='utf-8')
    contact_lst = []
    for line in file:
        contact_lst.append(line[:-1].split(' ; ')) # [:-1] - для исключения переноса в файле во время формирования списка, 
    file.close()
    cnt += 1
    return contact_lst # возврат для передачи в принт



def add_contact(data: str): # добавляет строку с контактом в файл, в правильном формате, которую предварительно проверила функция input_add_check()
    file = open('file.txt', 'a', encoding='utf-8') # открывает файл, в режиме 'a' - для добавления нового содержимого. Создаст новый файл, если не найдет с указанным именем.
    file.write(f'{data}\n') # записывает строку data, которую предварительно проверила функция input_add_check()
    file.close() # закрывает
    
    """
    with open('file.txt', 'a', encoding='utf-8') as file: # второй способ реализации записи в файл
    file.write(data)
    """


def del_contact(select): # удаляет строку с контактом под номером select, наличие которой предварительно проверила функция input_del_check(text)
    with open('file.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    del lines[select - 1]
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)