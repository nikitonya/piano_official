import tkinter as tk


class WindowPiano:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Piano')
        w = 1280
        h = 720
        icon = tk.PhotoImage(file='Icon.png')
        self.win.iconphoto(False, icon)
        self.win.config(bg='black')# цвет бэкграунда
        self.win.geometry(f"{w}x{h}+170+50")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
        self.win.resizable(False, False) # запрет расширения окна

        self.win.attributes('-fullscreen',False)  # устанавливает атрибуты, специфичные для платформы, в данном случае -fullscreen указывает, является ли окно полноэкранным или нет. Изначально - False.
        self.fullScreenState = False  # изначально флаг полноэкранного режима - False
        self.win.bind("<F11>", self.toggleFullScreen)
        self.win.bind("<Escape>", self.quitFullScreen)

        #Label Pian
        Label_Piano = tk.Label(self.win, text='Piano!',
                               bg='black',
                               fg='white',
                               font=('Times New Roman', 30, 'bold')
                               )

        Label_Piano.pack()



        self.win.mainloop()  # бесконечный цикл окна

    def toggleFullScreen(self, event):  # функция смены полноэкранного режима
        self.fullScreenState = not self.fullScreenState
        self.win.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):  # функция выхода из полноэкранного режима при нажатии на <Escape>
        self.fullScreenState = False
        self.win.attributes("-fullscreen", self.fullScreenState)
