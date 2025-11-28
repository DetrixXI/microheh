from tkinter import *
from PIL import Image
import os, re

def gif_animation(path: str, root: Tk, x: int, y: int):
    """
    :x и y: Координаты отрисовки 
    :type: int
    :param path: Путь к директории с картинками формата .png, которые должны собраться в гифку
    :type: str
    :param root: Окно, в котором должна проигрываться гифка
    :type: Tk()
    :Return: ширину и высоту гифки, id для after-процесса

    """
    root = root
    dir = path
    width, height = 0, 0
    files = os.listdir(dir)
    gif_frames = []
    for el in files:
        if re.search('\.png$', el):
            gif_frames.append(PhotoImage(master = root, file=f'{dir}\{el}'))  
            if width == 0:
                _ = Image.open(f'{dir}\{el}')
                width, height = _.size   
    count = 0
    def animation(count=0):
        frame=gif_frames[count] 
        gif_label.image=frame
        gif_label.config(image=frame)
        count += 1
        if count == len(gif_frames):
            count = 0     
        return root.after(35,lambda: animation(count))
    
    gif_label = Label(master=root, text='ERROR', image='')
    after_id = animation(count)
    gif_label.place(x=x, y=y)
    return (width, height, after_id)