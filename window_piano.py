import tkinter as tk

class WindowPiano:

    def __init__(self):
        win = tk.Tk()
        win.title('Piano')
        win.geometry("1280x720+150+50")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
        win.resizable(False, False)

        win.mainloop()  # бесконечный цикл окна