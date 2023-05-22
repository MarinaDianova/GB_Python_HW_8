import view, model


def start():
    # view.greetings() - ЛИБО просто пишем как в строке ниже
    print('1. вывод, 2. добавление, 3. поиск, 4. редактирование, 5. удаление, 6. выход') 

    if answer == '1':
        view.show()
    elif answer == '2':
        model.add_contact
    elif answer == '3':
        model.search()
    elif answer == '4':
        model.correction()
      
    elif answer == '5':
        model.delite()
        
        
    elif answer == '6':
        view.bye()
        break

    else:
        model.error()