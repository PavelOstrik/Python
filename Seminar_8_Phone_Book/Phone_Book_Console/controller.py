import view, model

def start():
    while True:
        command = view.show_menu()
        match command:            
            case '1': 
                model.open_file()  
            case '2':                 
                try:
                    model.show_contacts(model.get_path())
                except:
                    print('!!!!!Сначала выполните первый пункт меню!!!!!')
            case '3': 
                model.create_new_file_with_contacts()
            case '4': 
                try:
                    model.add_contact(model.get_path())    
                except:
                    print('!!!!!Сначала выполните первый пункт меню!!!!!')
            case '5': 
                try:
                    model.change_contact(model.get_path())   
                except:
                    print('!!!!!Сначала выполните первый пункт меню!!!!!')  
            case '6': 
                try:
                    model.delete_contact(model.get_path())    
                except:
                    print('!!!!!Сначала выполните первый пункт меню!!!!!')              
            case '0':
                break
        
