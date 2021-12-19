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
                           bg='white',
                           fg='black',
                           font=('Times new Roman', 40, 'bold'),
                           width=40,
                           height=5,
                           justify=tk.CENTER
                           )
    label_piano.grid()

    frame_notes = tk.Frame(win)
    frame_notes.grid()

    frame_notes2 = tk.Frame(win)
    frame_notes2.grid()

    btn1 = AudioButton(frame_notes, 'Do', "Music_Notes/Piano/D_s1.wav", 6, 5, 0, 0)
    btn1.grid()

    btn2 = AudioButton(frame_notes, 'So', "Music_Notes/Piano/C.wav", 6, 5, 0, 1)
    btn2.grid()

    btn3 = AudioButton(frame_notes2, 'Ko', "Music_Notes/Piano/D.wav", 6, 5, 0, 1)
    btn3.grid()

    win.mainloop()


if __name__ == '__main__':
    create_win()
