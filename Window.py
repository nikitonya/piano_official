import pygame
import tkinter as tk
from AudioButton import AudioButton
import wave
import pyaudio
from threading import Thread

def recording():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 15
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

class Window():
    def __init__(self):
        w = 1280
        h = 720
        self.win = tk.Tk()
        pygame.init()
        icon = tk.PhotoImage(file='Icon.png')
        self.win.title('Piano')
        self.win.iconphoto(False, icon)
        self.win.config(bg='white')  # цвет бэкграунда
        self.win.geometry(f"{w}x{h}+170+50")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
        self.win.resizable(False, False)  # запрет расширения окна
        self.win.attributes('-fullscreen', False)

        self.frame_top = tk.Frame(self.win)
        self.frame_top.grid()

        self.frame_actions = tk.Frame(self.win)
        self.frame_actions.grid()

        self.label_piano = tk.Label(self.frame_top, text='Piano!',
                                    bg='red',
                                    fg='black',
                                    font=('Times new Roman', 40, 'bold'),
                                    width=40,
                                    height=4,
                                    justify=tk.CENTER
                                    )
        self.label_piano.grid()

        self.frame_notes = tk.Frame(self.win)
        self.frame_notes.grid(stick='w')

        self.frame_notes2 = tk.Frame(self.win)
        self.frame_notes2.grid()

        # frame_notes
        self.btnspace = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=27, bg='white', fg='white',
                                  relief=tk.FLAT)
        self.btnspace.grid(row=0, column=0)
        self.btn1 = AudioButton(self.frame_notes, 'Do Dies', "Music_Notes/Piano/C_s.wav", 6, 5, 0, 1, 'black', 'white')
        self.btn2 = AudioButton(self.frame_notes, 'Re Dies', "Music_Notes/Piano/D_s.wav", 6, 5, 0, 2, 'black', 'white')
        self.btnspace1 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=11, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace1.grid(row=0, column=3)
        self.btn3 = AudioButton(self.frame_notes, 'Fa', "Music_Notes/Piano/F_s.wav", 6, 5, 0, 4, 'black', 'white')
        self.btn4 = AudioButton(self.frame_notes, 'Sol', "Music_Notes/Piano/G_s.wav", 6, 5, 0, 5, 'black', 'white')
        self.btn5 = AudioButton(self.frame_notes, 'Lya', "Music_Notes/Piano/Bb.wav", 6, 5, 0, 6, 'black', 'white')
        self.btnspace2 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=11, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace2.grid(row=0, column=7)
        self.btn6 = AudioButton(self.frame_notes, 'Do', "Music_Notes/Piano/C_s1.wav", 6, 5, 0, 8, 'black', 'white')
        self.btn7 = AudioButton(self.frame_notes, 'Re', "Music_Notes/Piano/D_s1.wav", 6, 5, 0, 9, 'black', 'white')

        # frame_notes2
        self.Do = AudioButton(self.frame_notes2, 'Do', "Music_Notes/Piano/C.wav", 6, 5, 0, 1, 'white', 'black')
        self.Re = AudioButton(self.frame_notes2, 'Re', "Music_Notes/Piano/D.wav", 6, 5, 0, 2, 'white', 'black')
        self.Mi = AudioButton(self.frame_notes2, 'Mi', "Music_Notes/Piano/E.wav", 6, 5, 0, 3, 'white', 'black')
        self.Fa = AudioButton(self.frame_notes2, 'Fa', "Music_Notes/Piano/F.wav", 6, 5, 0, 4, 'white', 'black')
        self.Sol = AudioButton(self.frame_notes2, 'Sol', "Music_Notes/Piano/G.wav", 6, 5, 0, 5, 'white', 'black')
        self.Lya = AudioButton(self.frame_notes2, 'Lya', "Music_Notes/Piano/A.wav", 6, 5, 0, 6, 'white', 'black')
        self.Si = AudioButton(self.frame_notes2, 'Si', "Music_Notes/Piano/B.wav", 6, 5, 0, 7, 'white', 'black')
        self.Do1 = AudioButton(self.frame_notes2, 'Do', "Music_Notes/Piano/C1.wav", 6, 5, 0, 8, 'white', 'black')
        self.Re1 = AudioButton(self.frame_notes2, 'Re', "Music_Notes/Piano/D1.wav", 6, 5, 0, 9, 'white', 'black')
        self.Mi1 = AudioButton(self.frame_notes2, 'Mi', "Music_Notes/Piano/E1.wav", 6, 5, 0, 10, 'white', 'black')
        self.Fa1 = AudioButton(self.frame_notes2, 'Fa', "Music_Notes/Piano/F1.wav", 6, 5, 0, 11, 'white', 'black')
        #self.Fa2 = AudioButton(self.frame_notes2, 'Fa2', "Music_Notes/Piano/F2.wav", 6, 5, 0, 12, 'white', 'black')

        self.sound_list = ['Piano', 'Steel_Drum']

        # self.canvas = tk.Canvas(self.frame_actions, width=100, height=100)
        # self.canvas.grid(row=0, column=1)
        #
        # self.icon = tk.PhotoImage(file='IconRadio.png')
        # self.canvas.create_image(0, 0, anchor=tk.NW, image=self.icon)

        self.var = tk.IntVar()
        self.var.set(0)
        self.piano = tk.Radiobutton(self.frame_actions, text='Piano', variable=self.var, value=0, indicatoron=0,
                                    command=self.change, height=5, width=10)
        # self.piano.config(image=tk.PhotoImage(file='Icon.png'))
        self.steel_drum = tk.Radiobutton(self.frame_actions, text='Steel_Drum', variable=self.var, value=1,
                                         indicatoron=0, command=self.change, height=5, width=10,
                                         fg='blue')
        self.button_record = tk.Button(self.frame_actions, text='Включить запись', command=Thread(target=recording,daemon=True).start())

        self.piano.grid(stick='w', row=0, column=0)
        self.steel_drum.grid(stick='w', row=0, column=1)
        self.button_record.grid(stick='w', row=0, column=2)

        self.win.mainloop()

    def change(self):
        self.btn1.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C_s.wav")
        self.btn2.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D_s.wav")
        self.btn3.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/F_s.wav")
        self.btn4.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/G_s.wav")
        self.btn5.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/Bb.wav")
        self.btn6.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C_s1.wav")
        self.btn7.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D_s1.wav")

        self.Do.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C.wav")
        self.Re.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D.wav")
        self.Mi.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/E.wav")
        self.Fa.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/F.wav")
        self.Sol.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/G.wav")
        self.Lya.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/A.wav")
        self.Si.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/B.wav")
        self.Do1.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C1.wav")
        self.Re1.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D1.wav")
        self.Mi1.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/E1.wav")
        self.Fa1.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/F1.wav")
