from tkinter import *
from gif_animation import gif_animation
from PIL import ImageFont

class error_window(Toplevel):
    def __init__(self, msg: str, kind_notif: str):
        """
        Docstring для __init__\n
        :param msg: Текст окошка ошибки\n
        :type msg: str\n
        :param kind_notif: Тайтл окошка ошибки\n
        :type kind_notif: str\n
        """
        super().__init__()
        def finish(*args):
            self.grab_release()
            self.after_cancel(after_id)
            self.destroy()
        dir = r'C:\Users\Кирпич в 2.9\Desktop\яндекс\infa\ВС_КОД\proj\pict\Error_3'
        width, height, after_id = gif_animation(dir, self, 0, 0)
        label = Label(master=self, text=msg, font=('Magneto', 20), 
                      foreground='firebrick1', anchor=CENTER, bg='gray10', wraplength=width)
        self.title(kind_notif)
        self.grab_set()
        self.geometry(f"{width}x{int(height*0.98) + label.winfo_reqheight()}+800+300")
        self.iconbitmap(r'./pict/ICON.ico')
        self.resizable(0,0)
        self.title(kind_notif)
        label.place(x=0, rely=1, width=width, anchor=SW)
        self.bind('<Escape>', finish)
        self.protocol("WM_DELETE_WINDOW", finish)

class success_window(Toplevel):
    def __init__(self, msg: str, kind_notif: str):
        """
        Docstring для __init__\n
        :param msg: Текст окошка успеха\n
        :type msg: str\n
        :param kind_notif: Тайтл окошка успеха\n
        :type kind_notif: str\n
        """
        super().__init__()
        def finish(*args):
            self.grab_release()
            self.after_cancel(after_id)
            self.destroy()
        dir = r'C:\Users\Кирпич в 2.9\Desktop\яндекс\infa\ВС_КОД\proj\pict\Error_3'
        width, height, after_id = gif_animation(dir, self, 0, 0)
        label = Label(master=self, text=msg, font=('Magneto', 20),    
                      foreground='firebrick1', anchor=CENTER, bg='gray10', wraplength=width)
        self.title(kind_notif)
        self.grab_set()
        self.geometry(f"{width}x{int(height*0.98) + label.winfo_reqheight()}+800+300")
        self.iconbitmap(r'./pict/ICON.ico')
        self.resizable(0,0)
        self.title(kind_notif)
        label.place(x=0, rely=1, width=width, anchor=SW)
        self.bind('<Escape>', finish)
        self.protocol("WM_DELETE_WINDOW", finish)

if __name__=="__main__":
    error_window('ААААААА ОШИБОКА12313232321312312321132312231123!!', 'ААААААА ОШИБОКА!!1').mainloop()
    

