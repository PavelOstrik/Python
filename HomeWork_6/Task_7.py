# Функция принимает в качестве аргументов строки в формате "Имя Фамилия",
# возвращает словарь, ключи - первые буквы фамилий, значения - словари,
# реализованные по схеме предыдущего задания.

myList = ['Иван Сергеев', 'Инна Серова', 'Пётр Алексеев', 'Илья Иванов', 'Анна Савельева',
'Юнона Ветрякова', 'Борис Аркадьев', 'Антон Серов', 'Павел Анисимов', ]

key_name = [i[0] for i in myList]
surname_list = [i[1] for i in (i.split() for i in myList)]
key_surname = [i[0] for i in surname_list]
print(key_name)
print(key_surname)

name_dict = {key_name[0] : [name[0] if key_surname[0] and key_name[0] in name else 0] for name in myList}
# surname_dict = {key_surname[0]: 

# for i in myList:
#     if key_name[i] not in name_dict:
#         name_dict[key_name[i]] = []  
#     if key_name[i] + key_surname[i] == key_name[i+1] + key_surname[i+1]:
#         name_dict[key_name[i]].append(i)
    




print(name_dict)

# surname_dict = {}
# print(surname_dict)

 





















