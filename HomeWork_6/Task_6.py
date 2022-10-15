# Написать функцию, аргументы - имена сотрудников, возвращает словарь, 
# ключи - первые буквы имен, значения списки, содержащие имена, начинающиеся
# с соответствующей буквы.

name_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(name_list)

name_dict = {}

for name in name_list:
    key = name[0]    

    if key not in name_dict:
        name_dict[key] = []        
    name_dict[key].append(name)

print (name_dict)


    




