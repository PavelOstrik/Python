path = r'test.txt'
with open(path, 'r', encoding='UTF-8') as f:    
        contacts = [i.strip().split(';') for i in f.readlines()]
        name_list = [i[1] for i in contacts]
        print(contacts)
        print(name_list)
        while True:
            question = '\
                \n1 - Найти контакт\
                \n2 - Закончить работу с файлом\
                \n\
                \nВведите необходимую команду: \n'
            print()
            command = input(question)        
            match command:            
                case '1':
                    while True:             
                        name_contact = input('Введите имя контакта: ')
                        if name_contact in name_list:
                            for i in contacts:
                                if name_contact in i:
                                    print(('   |   '.join(i)))
                            break
                        else:           
                            print('Вы выбрали несуществующий индекс контакта')

                case '2':                      
                        break    