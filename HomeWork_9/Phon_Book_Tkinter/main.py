from  tkinter import*


root = Tk()

root.title("PHONE BOOK") # заглавное название для окна
icon = PhotoImage(file = "icon.png") # иконка слева от названия
root.iconphoto(False, icon) # используется единожды, на другие окн не распространяется
root.geometry("600x350+650+250") # объявляем размер нашего окна
root.resizable(False, False) # делаем окно неизменяемым по размеру

# Information List
datas = []
path = 'PhonBook.txt'

# Add Information
def add():
    global datas    
    datas.append([Name.get(),Number.get(),Comment.get()])
    update_book()
  
# View Information
def view():
    # curselection(): возвращает набор индексов выделенных элементов
    # Текст в поле ввода обновляется автоматически при использовании метода set().
    Name.set(datas[int(select.curselection()[0])][0])
    Number.set(datas[int(select.curselection()[0])][1])
    Comment.set(datas[int(select.curselection()[0])][2])

    
  
# Delete Information
def delete():
    del datas[int(select.curselection()[0])]   
    update_book()
  
def reset():
    Name.set('')
    Number.set('')
    Comment.set('')
  
# Update Information
def update_book():
    global datas
    global path
    select.delete(0,END) # Это удалит весь контент с позиции "0" и до конца
    with open(path, 'w+', encoding='UTF-8') as file:        
        for index, item in enumerate(datas):
            datas[index] = ','.join(item)      
        file.write('\n'.join(datas))        
    with open(path, 'r', encoding='UTF-8') as file:
        datas = [i.strip().split(',') for i in file.readlines()]  
        # Заполняем список с конца, вторым аргументом передаем вставляемый элемент 
        for n,p,c in datas:
            select.insert(END, n)    

# Виджеты - кнопки, метки, поля ввода.
Name = StringVar() # тип переменной, которая хранит некоторую строку.
Number = StringVar()
Comment = StringVar()
  
# Фрейм - вспомогательный виджет, создание которого происходит при помощи класса Frame()
# Фреймы размещают на главном окне, а уже в фреймах – виджеты
frame = Frame()
frame.pack(padx=10,pady=10, anchor=NW)
# позиционирование, padx, padx внешние отступы от границ
# anchor - позиционирование по сторонам света
  
frame1 = Frame()
frame1.pack(padx=10,pady=10, anchor=NW)
  
frame2 = Frame()
frame2.pack(padx=10,pady=10, anchor=NW)

# Виджет Label представляет текстовую метку. Этот элемент позволяет выводить статический
# текст без возможности редактирования.  
# Указываем, что будет в frame, задаём шрифт и позиционирование
Label(frame, text = 'Name', font='arial 12 bold').pack(padx=21,side=LEFT)
Entry(frame, textvariable = Name,width=70).pack()
# Элемент Entry представляет поле для ввода текста.
# С помощью параметра textvariable эта переменная привязана к тексту поля Entry,
# а также к тексту кнопки и метки:
  
Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(padx=3,side=LEFT)
Entry(frame1, textvariable = Number,width=70).pack()
  
Label(frame2, text = 'Comment', font='arial 12 bold').pack(padx=6,side=LEFT)
Entry(frame2, textvariable = Comment,width=70).pack()

# Для создания кнопки используется конструктор Button().
# В этом конструкторе с помощью параметра text можно установить текст кнопки.
# Чтобы разместить виджет в контейнере (главном окне), у него вызывается метод pack()
Button(root,text="Add",font="arial 12 bold",command=add).place(x= 30, y=150,relwidth=0.10,relheight=0.10)
Button(root,text="View",font="arial 12 bold",command=view).place(x= 30, y=200,relwidth=0.10,relheight=0.10)
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 30, y=250,relwidth=0.10,relheight=0.10)
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 30, y=300,relwidth=0.10,relheight=0.10)

# Виджет Scrollbar позволяет прокручивать содержимое контейнера,
# которое больше размеров этого контейнера.  
scroll_bar = Scrollbar(root, orient=VERTICAL) # Вертикальная прокрутка
# Виджет Listbox в tkinter представляет список объектов
# height: высота элемента в строках. По умолчанию отображает 10 строк
# yscrollcommand: устанавливает вертикальную прокрутку
# метод set() отвечает за перемещение слайдера
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
# метод yview для прокрутки по вертикали  
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x= 100, y=145, width=429,height=190)


with open(path, 'r', encoding='UTF-8') as file:
    datas = [i.strip().split(',') for i in file.readlines()]   
    for n,p,c in datas:
        select.insert(END, n)

root.mainloop()

