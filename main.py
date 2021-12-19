from AudioButton import AudioButton
import tkinter as tk
import pygame


def create_win():
    w = 1280
    h = 720
    win = tk.Tk()
    pygame.init()

    icon = tk.PhotoImage(file='Icon.png')
    win.title('Piano')
    win.iconphoto(False, icon)
    win.config(bg='white')  # цвет бэкграунда
    win.geometry(f"{w}x{h}+170+50")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
    win.resizable(False, False)  # запрет расширения окна
    win.attributes('-fullscreen',
                   False)
    frame_top = tk.Frame(win)
    frame_top.grid()

    label_piano = tk.Label(frame_top, text='Piano!',
                           bg='red',
                           fg='black',
                           font=('Times new Roman', 40, 'bold'),
                           width = 40,
                           justify=tk.CENTER
                           )
    label_piano.grid()

    frame_notes = tk.Frame(win)
    frame_notes.grid()

    btn1 = AudioButton(frame_notes, 'Do',
                       6,5

                       ).grid(0,0)
    btn1.grid()


    win.mainloop()

if __name__ == '__main__':
    create_win()
