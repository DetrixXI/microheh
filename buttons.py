import hashlib, json
from notification_windows import error_window, success_window
from tkinter import *

def check_for_fulness(table: list[Entry]) -> list: 
    """
    Фнк принимает Entrys, проверяет, везде ли есть данные,\n возвращает имена тех, кто пустой.\n
    :param table: набор Entry, которые могли соснуть
    :type table: list[Entry]
    :return: мЭCCив поименный, кто где соснул
    :rtype: list
    """
    kit = list()
    for el in table:
        if el.get() == '':
            kit.append(str(el._name))
    return(kit)

    
#КНОПКА РЕГИСТРАЦИИ
def reg_btn_command(entry_log: Entry, entry_passw: Entry):
    """
    Команда для кнопки\n
    Пытается зарегестрировать пользователя.\n
    -Отказы:\n
    1. Уже сущ.данный логин\n
    2. Не введен логин или пароль или оба\n
    -Если всё ок:\n
    Открывается окно с регистрацией, данные грузятся в users\n
    :param entery_log: энтри с логином
    :param entry_pasw: энтри с паролем
    """
    def helper():

        log, passw = entry_log.get(), entry_passw.get()
        passw = hashlib.sha256(passw.encode('utf-8')).hexdigest()

        if kit := check_for_fulness([entry_log, entry_passw]):
            error_window (f'ZERO info in {", ".join(kit)}!!', "АААУУЭЭАЭАО(")
            return
        
        with open('users.txt', 'r') as file:
            usr_dict = json.load(file)  
        #print(usr_dict)

        if usr_dict.get(log, False):
            error_window("THIS LOGIN  IS  ALREADY  IN  USE1", "неповезло.....")
            return
        
        root = Toplevel()
        root.grab_set()
        txt_font = ('Magneto', 16)
        #labels_conf = {'master': f'{root}'}
        name_label = Label(master=root, text='Enter your name:', font=txt_font,
                                 bg='gray11', foreground='red4')
        name_label.config()
        patronymic_label = Label(master=root, text='Enter your patronymic:', font=txt_font,
                                 bg='gray11', foreground='red4')
        surname_label = Label(master=root, text='Enter your surname:', font=txt_font,
                                 bg='gray11', foreground='red4')
        position_label = Label(master=root, text='Enter your position:', font=txt_font,
                                 bg='gray11', foreground='red4')
        
        name_entry = Entry(master=root, font=txt_font, bg='skyblue4', relief=RIDGE, foreground='red4', name='name field')
        name_var = StringVar(master=name_entry)
        patronymic_entry = Entry(master=root, font=txt_font, bg='skyblue4', relief=RIDGE, foreground='red4', name='patronymic field')
        patronymic_var = StringVar(master=patronymic_entry)
        surname_entry = Entry(master=root, font=txt_font, bg='skyblue4', relief=RIDGE, foreground='red4', name='surname field')
        surname_var = StringVar(master=surname_entry)
        postion_entry = Entry(master=root, font=txt_font, bg='skyblue4', relief=RIDGE, foreground='red4', name='postion field')
        position_var = StringVar(master=postion_entry)

        surname_label.grid(row=0, column=0, sticky=E, pady=3, padx=3)
        name_label.grid(row=1, column=0, sticky=E, padx=3)
        patronymic_label.grid(row=2, column=0, sticky=E, padx=3)
        position_label.grid(row=3, column=0, sticky=E, padx=3)

        surname_entry.grid(row=0, column=1, sticky=S)
        name_entry.grid(row=1, column=1, sticky=S)
        patronymic_entry.grid(row=2, column=1, sticky=S)
        postion_entry.grid(row=3, column=1, sticky=S)
        
        def ins_d_into_users():
            if (kit := check_for_fulness(for_check)):
                error_window (f'ZERO info in {",".join(kit)}!! Ur STUPID??', "АААУУЭЭАЭАО(")
                return
            
            usr_dict[log] = {
                'passw': passw,
                'surname': surname_entry.get(),
                'name': name_entry.get(),
                'patronymic': patronymic_entry.get(),
                'position': postion_entry.get()
                }
            with open('users.txt', 'w') as f:
                json.dump(usr_dict, f, indent=4)
            success_window('CONGRATULATIONS <SLAVE>!', 'Еще пока не смешарик....ы')
            
            root.grab_release()
            root.destroy()

        for_check = [name_entry, patronymic_entry, surname_entry, postion_entry]
        end_of_reg_btn = Button(master=root, text="Все данные введены", command=ins_d_into_users)
        end_of_reg_btn.grid(row=4, columnspan=2, pady=5)

        root.config(bg='gray11')
        root.title("Регисрация))")
        root.iconbitmap(r'./pict/ICON.ico')
        root.geometry(f'{patronymic_label.winfo_reqwidth()+surname_entry.winfo_reqwidth()+10}x{patronymic_label.winfo_reqheight()*5+10}+500+500')
        root.mainloop()
    return helper



if __name__=='__main__':
    log = '1231213'
    passw = '123123'
    a, b = Entry(), Entry()
    a.insert(0, a)
    b.insert(0, passw)
    reg_btn_command(a, b)()

    
    

