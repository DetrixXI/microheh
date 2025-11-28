from tkinter import *

root = Tk()
root.title(":JGF")
#root.geometry("50x50+800+50")
root.resizable(True, True)
label_2 = Label(text="hell0") #тут создаем лейбел
label_1 = Label(text="chort") #тут создаем лейбел
label_1.pack() #а тут размещаем его в окне
label_2.pack()

# минимальные и максимальные размеры
root.minsize(200,150)   
#root.maxsize(400,300)  #с этой штукой может конфликтовать -fullscreen

root.iconbitmap(r'C:\Users\Кирпич в 2.9\Desktop\яндекс\infa\ВС_КОД\proj\pict\icon.ico')
#C:\Users\Кирпич в 2.9\Desktop\яндекс\infa\ВС_КОД\proj\pict\icon.ico
#C:\Users\Кирпич в 2.9\Desktop\яндекс\игра\files\pictures\icon — копия.ico

#из названия понятно, каждый параметр - возможность растяжения по
#горизонтали и вертикали соответственно 

def finish(*args):
    root.destroy() #закрытие окна
    print('Zakrito')

def msg(a):
    print('fffffffff', a)

# привязка каких-то действий/клавиш к функциям каким либо (главное не вы
# зывать эти функции, а то будет жопа)
root.protocol("WM_DELETE_WINDOW", finish)
root.bind("<Key>", msg) #этот метод возвращает в фнк. данные о нажатии!!
root.bind("<Escape>", finish)

#root.attributes("-alpha", 0.01)#alpha = прозрачность 
#root.attributes("-fullscreen", True)
#root.attributes("-toolwindow", True)# отключена верхняя панелька (кроме креста)  

#строчка ниже заставляет применить все настройки к окну до того
#как будет заупщен мейнлуп
root.update_idletasks() 

def counter():
    print(btn['text'], type(btn['text']))
    if isinstance(btn['text'], str):
        btn["text"] = 0
    btn["text"] += 1
    if btn['text'] > 10:
        btn["text"] = "СЛОМАЛ КНОПКУ!1"
        btn['state'] = DISABLED
         

btn = Button(text="Click") # есть еще параметры разные там, чекни в доках
btn["text"] = 'NEW TEXT' # оьращаться к параметрам можно и вне конструктора
btn.config(text="SUPER NEW TEXT", command=counter) # так можно разом несколько задать 

# anchor - NW, W, S, E и т.д. установка виджета
# padx/pady - отступ от границы контейнера
btn.pack(expand=True, fill = X,) 

# для позиционирования виджета так же используется метод .place()
# height/weight - размер виджета в пкс
# relheight/relwidth - размер виджета в доле от родительского окна
# x/y - смещение в пкс от левого верхнего угла
# relx/rely - смещение в доле ...
# есть еще метод grid, там виртуальная сетка, но чот непонтное слегка...
# но вроде полезное
btn.place(x = 100, y = 100)

table_1 = Entry(background='red')
def func_1():
    print(table_1.get())
    table_1.delete(0, END)
btn_1 = Button(text='зарегестрироваться', command=func_1)
btn_1.pack()
table_1.pack()
print(root.children)
root.mainloop()

