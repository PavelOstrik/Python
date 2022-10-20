from tkinter import filedialog, Tk

contacts = []
path = ''

def get_path():
    global path
    return path

def get_contacts():
    global contacts
    return contacts

def open_file(): 
    global path
    root = Tk()
    root.attributes("-topmost", True) 
    root.lift()
    root.withdraw()
    input("\nНажмите любую клавишу ")
    fileName = filedialog.askopenfilename(filetypes=(('text files', 'txt'),))    
    path = str(fileName)
    print(path)
    return path    

def show_contacts(path: str):   
    global contacts             
    with open(path, encoding='UTF-8') as f:
        contacts = [i.strip().split(';') for i in f.readlines()]   
        print('id  |       ФИО        |    Телефон      | Комментарий') 
        print('-------------------------------------------------------')       
        [print(('   |   '.join(i))) for i in contacts]
    return contacts

def create_new_file_with_contacts():
    global contacts
    global path
    fileName = input('Введите название файла (пример: test): ')    
    path = f'{fileName}.txt'
    with open(path, 'w', encoding='UTF-8') as f:
        last_id = 0    
        while True:            
            question = '\
                \n1 - Добавить контакт\
                \n2 - Закончить работу с файлом\
                \n\
                \nВведите необходимую команду: \n'
            command = input(question)        
            match command:            
                case '1': 
                    id = str(last_id)                    
                    name = input(f'Введите name: ')
                    phone = input(f'Введите phone: ')
                    comment = input(f'Введите comment: ')
                    f.write((';'.join([id,name,phone,comment]) + '\n'))
                    print()
                    print(';'.join([id,name,phone,comment]) + '\n')
                    last_id += 1  
                case '2':                 
                    break

def add_contact(path:str):
    with open(path, 'r+', encoding='UTF-8') as f:    
        id_list = [i[0].strip().split(';') for i in f.readlines()]
        id_list = [i[0] for i in id_list]        
        id = len(id_list)
        while True:        
            if str(id) not in id_list:        
                id = str(id)
                name = input(f'Введите name: ')
                phone = input(f'Введите phone: ')
                comment = input(f'Введите comment: ')                
                f.write((';'.join([id,name,phone,comment]) + '\n'))
                print()
                print(';'.join([id,name,phone,comment]) + '\n')
                print('Контакт добавлен')
                break
            else:
                id += 1

def change_contact(path: str): 
    with open(path, 'r', encoding='UTF-8') as f:    
        contacts = [i.strip().split(';') for i in f.readlines()]
        print('id  |       ФИО        |    Телефон      | Комментарий') 
        print('-------------------------------------------------------')
        [print(('   |   '.join(i))) for i in contacts]
        id_list = [i[0] for i in contacts]
        print()
        while True:        
            id_contact = input('Введите индекс контакта для изменения: ')
            if id_contact in id_list:         
                for i in range(len(contacts)):
                    if id_contact == contacts[i][0]:
                        contact = contacts[i]
                        id_contacts = i 
                break   
            else:         
                print('Вы выбрали несуществующий индекс контакта')            
        
    while True:            
        question = '\
            \n1 - Изменить имя\
            \n2 - Изменить телефон\
            \n3 - Изменить Комментарий\
            \n4 - Закончить работу с файлом\
            \n\
            \nВведите необходимую команду: \n'
        command = input(question)        
        match command:            
            case '1': 
                contact[1] = input('Введите новое имя: ')
                contacts[id_contacts] = contact                
                contacts = [';'.join(i) for i in contacts] 
                                        
                with open(path, 'w', encoding='UTF-8') as f:  
                    f.write('\n'.join(str(i) for i in contacts))
                print('id  |       ФИО        |    Телефон      | Комментарий') 
                print('-------------------------------------------------------')   
                [print(str(i).replace(';', '    |   ')) for i in contacts]
                print('Контакт изменён') 
            case '2': 
                contact[2] = input('Введите новый телефон: ')
                contacts[id_contacts] = contact                
                contacts = [';'.join(i) for i in contacts] 
                                         
                with open(path, 'w', encoding='UTF-8') as f:  
                    f.write('\n'.join(str(i) for i in contacts))
                print('id  |       ФИО        |    Телефон      | Комментарий') 
                print('-------------------------------------------------------')   
                [print(str(i).replace(';', '    |   ')) for i in contacts]
                print('Контакт изменён')     
            case '3': 
                contact[3] = input('Введите новый комментарий: ')
                contacts[id_contacts] = contact                
                contacts = [';'.join(i) for i in contacts] 
                                        
                with open(path, 'w', encoding='UTF-8') as f:  
                    f.write('\n'.join(str(i) for i in contacts))
                print('id  |       ФИО        |    Телефон      | Комментарий') 
                print('-------------------------------------------------------')   
                [print(str(i).replace(';', '    |   ')) for i in contacts]
                print('Контакт изменён')                     
            case '4':                 
                break

def delete_contact(path:str):
    with open(path, 'r', encoding='UTF-8') as f:    
        contacts = [i.strip().split(';') for i in f.readlines()]
        print(contacts)  
        print('id  |       ФИО        |    Телефон      | Comment') 
        print('---------------------------------------------------')       
        [print(('   |   '.join(i))) for i in contacts]    
        id_list = [i[0] for i in contacts]

    while True:
        question = '\
            \n1 - Удалить контакт\
            \n2 - Закончить работу с файлом\
            \n\
            \nВведите необходимую команду: \n'
        command = input(question)        
        match command:            
            case '1':
                while True:             
                    id_contact = input('Введите индекс контакта для удаления: ')
                    
                    if id_contact in id_list:         
                        for i in range(len(contacts)):
                            if id_contact == contacts[i][0]:
                                contacts.pop(i)
                                break

                        contacts = [';'.join(i) for i in contacts]            
                        with open(path, 'w', encoding='UTF-8') as f:  
                            f.write('\n'.join(str(i) for i in contacts))
                            print('id  |       ФИО        |    Телефон      | Комментарий') 
                            print('-------------------------------------------------------')   
                            [print(str(i).replace(';', '    |   ')) for i in contacts]
                            print('Контакт удалён')
                            break 

                    else:           
                        print('Вы выбрали несуществующий индекс контакта')  
            case '2':                      
                break    


    
        
            

       