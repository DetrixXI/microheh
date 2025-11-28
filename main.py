from tkinter import *
from tkinter import messagebox
import hashlib
import re
import json
from notification_windows import error_window
from buttons import reg_btn_command
root = Tk()
                
img_reg = PhotoImage(file=r'pict\pngs\reg.png')
img_log = PhotoImage(file=r'pict\pngs\log.png')

#reg_canv = Canvas(bg='red')
#log_canv = Canvas(bg='red')
with open('users.txt', 'r') as f:
    keys = json.load(f).keys()

def is_valid(data):
    print(data)
    err_msg.set('Z A N Y A T O' if data in keys else '')
    return not(data in keys)

check = (root.register(is_valid),'%P')
err_msg = StringVar()
err=Label(textvariable= err_msg, foreground='firebrick1', bg='gray11',
                   font='Magneto')
field_log = Entry(foreground='firebrick1', bg='skyblue4', name='login field',
                   font='Magneto', relief=RIDGE, validate='key', validatecommand=check)

entry_log = StringVar(master=field_log)


#log_canv.create_window(10, 20, window=field_log)
#log_canv.grid(row=0, column = 1, columnspan=1, pady=10, padx=10)

label_log = Label(text='Enter Login:', foreground='firebrick1', bg='skyblue4',
                   font='Magneto')

field_pass = Entry(foreground='firebrick1', name='password field',
                   bg='skyblue4', font='Magneto', readonlybackground='red', relief=RIDGE)
entry_passw = StringVar(master=field_pass)

label_reg = Label(text='Enter Password:', foreground='firebrick1',
                  bg='skyblue4', font='Magneto')

btn_reg = Button(image=img_reg, relief=RIDGE, bg='gray11', activebackground='red4',
                 command=reg_btn_command(field_log, field_pass))

btn_login = Button(image=img_log, relief=RIDGE, bg='gray11', activebackground='red4')

btn_login.grid(row=0, column=3, padx=0, pady=5, rowspan=2)
label_log.grid(row=0, column=1, sticky=E)
field_log.grid(row=0, column=2, columnspan=1, pady=0, padx=10, sticky='')
field_pass.grid(row=1, column=2, columnspan=1, pady=0, padx=10)
label_reg.grid(row=1, column=1)
btn_reg.grid(row=0, column=0, padx=10, pady=5, rowspan=2)

err.grid(row=0, column=2, sticky=S)

r_width, r_height = 755, 180
root.geometry("0x0+800+300")
root.minsize(r_width, r_height)
root.config(bg='gray11')
root.iconbitmap(r'./pict/ICON.ico')
root.title(":JGF")

root.mainloop()