#ЧТО ТО ПРО КНОПКИ 
from tkinter import *

class entry_button(Entry, Button):
    '''
    pos_x - по иксу\n
    pos_y - по игрек\n
    text_but - текст в кнопке\n
    proc_func - функция кнопки
    '''
    def _proc_func(self):
        def helper():
            add_to_table(self.line.get())
            print(self.line.get())
            print(table)
            self.line.delete(0, END)
        return helper
        
    def __init__(self, pos_x: int, pos_y: int, text_but: str, proc_func = _proc_func):
        self.line = Entry()
        self.btn = Button(text=text_but, command=proc_func(self))
        self.line.pack(ipadx=pos_x, ipady=pos_y)
        self.btn.pack(ipadx=pos_x+10, ipady=pos_y+10)
    


table = list()
def add_to_table(data):
    table.append(data)


root = Tk()
a = entry_button(10, 10,'Ввести пароль')
b = entry_button(30, 30,'ЖОПА')

root.minsize(500, 200)
root.mainloop()


class notification_window(Tk):
    def __init__(self, msg: str, kind_notif: str):
        """
        Docstring для __init__\n
        :param msg: Текст окошка оповещения\n
        :type msg: str\n
        :param kind_notif: Тайтл окошка опопвещения\n
        :type kind_notif: str\n
        """
        super().__init__()
        dir = r'C:\Users\Кирпич в 2.9\Desktop\яндекс\infa\ВС_КОД\proj\pict\Error_3'
        width, height = 0, 0
        files = os.listdir(dir)
        gif_frames = []
        for el in files:
            if re.search('\.png$', el):
                gif_frames.append(PhotoImage(file=f'{dir}\{el}'))  
                if width == 0:
                    _ = Image.open(f'{dir}\{el}')
                    width, height = _.size   
        count = 0
        def animation(count=0):
            print(count)
            frame=gif_frames[count]    
            gif_label.config(image=frame)
            gif_label.image=frame
            count += 1
            if count == len(gif_frames):
                count = 0     
            self.after(10, lambda: animation(count))
        
        gif_label = Label(text='ERROR', image='')
        animation(count)
        gif_label.place(x=0, y=0)

        self.title(kind_notif)
        self.geometry(f"{width}x{height}+800+150")
        self.iconbitmap(r'./pict/ICON.ico')
        self.resizable(0,0)


#========================
        line = 1
        usr_dict = {log:hash_passw}
        if line=='':#Если еще никого нет 
            with open('users.txt', 'w') as f:
                json.dump(usr_dict, f, indent=4, sort_keys=True)
                print('теперь зареган')
                return
        if line.get(log, False):#Если уже зареган
            notif_wind = error_window('Name is already in use', 'ОШИБОКА')
            print('уже зареган')
            return
        line[log]=passw
        with open('users.txt', 'w') as f:
            json.dump(line, f, indent=4, sort_keys=True)
            print('теперь зареган')
            return