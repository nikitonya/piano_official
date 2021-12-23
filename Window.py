import pygame
import tkinter as tk
from AudioButton import AudioButton
import wave
import pyaudio
import threading
import time


class Window():

    def __init__(self):
        w = 1280
        h = 760
        self.win = tk.Tk()
        pygame.init()
        icon = tk.PhotoImage(file='Icon.png')
        self.win.title('Piano')
        self.win.iconphoto(False, icon)
        self.win.config(bg='white')  # цвет бэкграунда
        self.win.geometry(f"{w}x{h}+155+40")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
        self.win.resizable(False, False)  # запрет расширения окна
        self.win.attributes('-fullscreen', False)
        self.vol = 1

        self.frame_top = tk.Frame(self.win)
        self.frame_top.grid()

        self.frame_space0 = tk.Frame(self.win, bg='white')
        self.frame_space0.grid()
        self.btnspace0 = tk.Button(self.frame_space0, state=tk.DISABLED, height=1, width=22, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace0.grid(row=0, column=0)

        self.frame_actions = tk.Frame(self.win, bg='white')
        self.frame_actions.grid()

        self.label_piano = tk.Label(self.frame_top, text='Piano!',
                                    bg='white',
                                    fg='black',
                                    font=('Times new Roman', 40, 'bold'),
                                    width=40,
                                    height=1,
                                    justify=tk.CENTER
                                    )
        self.label_piano.grid()

        self.frame_space = tk.Frame(self.win, bg='white')
        self.frame_space.grid()
        self.btnspace = tk.Button(self.frame_space, state=tk.DISABLED, height=1, width=22, bg='white', fg='white',
                                  relief=tk.FLAT)
        self.btnspace.grid(row=0, column=0)

        self.frame_notes = tk.Frame(self.win, bg='white')
        self.frame_notes.grid(stick='w')


        # frame_notes
        self.btnspace1 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=0, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace1.grid(row=0, column=0)
        self.C_d = AudioButton(self.frame_notes, 'C#', "Music_Notes/Piano_classic/C#.wav", 7, 4, 0, 1, 'black', 'white',
                               'q')
        self.D_d = AudioButton(self.frame_notes, 'D#', "Music_Notes/Piano_classic/D#.wav", 7, 4, 0, 2, 'black', 'white',
                               'w')
        self.btnspace2 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=9, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace2.grid(row=0, column=3)
        self.F_d = AudioButton(self.frame_notes, 'F#', "Music_Notes/Piano_classic/F#.wav", 7, 4, 0, 4, 'black', 'white',
                               'e')
        self.G_d = AudioButton(self.frame_notes, 'G#', "Music_Notes/Piano_classic/G#.wav", 7, 4, 0, 5, 'black', 'white',
                               'r')
        self.A_d = AudioButton(self.frame_notes, 'A#', "Music_Notes/Piano_classic/A#.wav", 7, 4, 0, 6, 'black', 'white',
                               't')
        self.btnspace3 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=9, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace3.grid(row=0, column=7)
        self.C1_d = AudioButton(self.frame_notes, 'C1#', "Music_Notes/Piano_classic/C1#.wav", 7, 4, 0, 8, 'black',
                                'white', 'y')
        self.D1_d = AudioButton(self.frame_notes, 'D1#', "Music_Notes/Piano_classic/D1#.wav", 7, 4, 0, 9, 'black',
                                'white', 'u')
        self.btnspace4 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=9, bg='white', fg='white',
                                   relief=tk.FLAT)
        self.btnspace4.grid(row=0, column=10)
        self.F1_d = AudioButton(self.frame_notes, 'F1#', "Music_Notes/Piano_classic/F1#.wav", 7, 4, 0, 11, 'black',
                                'white', 'i')
        self.G1_d = AudioButton(self.frame_notes, 'G1#', "Music_Notes/Piano_classic/G1#.wav", 7, 4, 0, 12, 'black',
                                'white', 'o')
        self.A1_d = AudioButton(self.frame_notes, 'A1#', "Music_Notes/Piano_classic/A1#.wav", 7, 4, 0, 13, 'black',
                                'white', 'p')

        # frame_notes2
        self.btnspace5 = tk.Button(self.frame_notes, state=tk.DISABLED, height=13, width=7, bg='black', fg='black',
                                   relief=tk.FLAT)
        self.btnspace5.grid(row=1, column=0)
        self.C = AudioButton(self.frame_notes, 'C', "Music_Notes/Piano_classic/C.wav", 7, 4, 1, 1, 'white', 'black',
                             '[')
        self.D = AudioButton(self.frame_notes, 'D', "Music_Notes/Piano_classic/D.wav", 7, 4, 1, 2, 'white', 'black',
                             ']')
        self.E = AudioButton(self.frame_notes, 'E', "Music_Notes/Piano_classic/E.wav", 7, 4, 1, 3, 'white', 'black',
                             'a')
        self.F = AudioButton(self.frame_notes, 'F', "Music_Notes/Piano_classic/F.wav", 7, 4, 1, 4, 'white', 'black',
                             's')
        self.G = AudioButton(self.frame_notes, 'G', "Music_Notes/Piano_classic/G.wav", 7, 4, 1, 5, 'white', 'black',
                             'd')
        self.A = AudioButton(self.frame_notes, 'A', "Music_Notes/Piano_classic/A.wav", 7, 4, 1, 6, 'white', 'black',
                             'f')
        self.B = AudioButton(self.frame_notes, 'B', "Music_Notes/Piano_classic/B.wav", 7, 4, 1, 7, 'white', 'black',
                             'g')
        self.C1 = AudioButton(self.frame_notes, 'C1', "Music_Notes/Piano_classic/C1.wav", 7, 4, 1, 8, 'white', 'black',
                              'h')
        self.D1 = AudioButton(self.frame_notes, 'D1', "Music_Notes/Piano_classic/D1.wav", 7, 4, 1, 9, 'white', 'black',
                              'j')
        self.E1 = AudioButton(self.frame_notes, 'E1', "Music_Notes/Piano_classic/E1.wav", 7, 4, 1, 10, 'white',
                              'black', 'k')
        self.F1 = AudioButton(self.frame_notes, 'F1', "Music_Notes/Piano_classic/F1.wav", 7, 4, 1, 11, 'white',
                              'black', 'l')
        self.G1 = AudioButton(self.frame_notes, 'G1', "Music_Notes/Piano_classic/G1.wav", 7, 4, 1, 12, 'white',
                              'black', ';')
        self.A1 = AudioButton(self.frame_notes, 'A1', "Music_Notes/Piano_classic/A1.wav", 7, 4, 1, 13, 'white',
                              'black', '1')
        self.B1 = AudioButton(self.frame_notes, 'B1', "Music_Notes/Piano_classic/B1.wav", 7, 4, 1, 14, 'white',
                              'black', 'Return')

        self.btns = [self.C, self.D, self.E, self.F, self.G, self.A, self.B, self.C1, self.D1, self.E1, self.F1,
                     self.G1, self.A1, self.B1, self.C_d, self.D_d, self.F_d, self.G_d, self.A_d, self.C1_d, self.D1_d,
                     self.F1_d, self.G1_d, self.A1_d]

        # self.frame_notes.bind('<q>', self.C_d.play_sound)
        # self.frame_notes.bind('<c>', self.C.play_sound)

        self.sound_list = ['Piano_classic']

        self.var = tk.IntVar()
        self.var.set(0)
        self.piano = tk.Radiobutton(self.frame_actions, text='Piano', variable=self.var, value=0, indicatoron=0,
                                    command=self.change, height=5, width=10)
        # self.piano.config(image=tk.PhotoImage(file='Icon.png'))
        self.steel_drum = tk.Radiobutton(self.frame_actions, text='Steel_Drum', variable=self.var, value=1,
                                         indicatoron=0, command=self.change, height=5, width=10,
                                         fg='blue')
        self.button_record = tk.Button(self.frame_actions, text='Start', command=self.main)

        self.piano.grid(stick='w', row=0, column=0)
        self.steel_drum.grid(stick='w', row=1, column=0)
        self.button_record.grid(stick='w', row=0, column=2)

        # VolumeFrame
        self.frame_volume = tk.LabelFrame(self.frame_actions, text='Volume', bg='white')
        self.frame_volume.grid(row=0, column=5, padx=40)

        # function for volume bar

        def volume(vol):
            for btn in self.btns:
                btn.change_volume(int(vol) / 100)

        # volume img
        self.volimg = tk.PhotoImage(file='vol.png')
        volimg = tk.Label(self.frame_volume, image=self.volimg).grid(row=0, column=3)

        # volume bar
        self.scale = tk.Scale(self.frame_volume, from_=0, to=100, orient=tk.HORIZONTAL, bg='cyan', length=120,
                              command=volume)
        self.scale.set(100)
        self.scale.grid(stick='e', row=0, column=5)

        self.win.mainloop()

    def change(self):

        # self.C_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C_d.wav")
        # self.D_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D_d.wav")
        # self.F_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/F_d.wav")
        # self.G_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/G_d.wav")
        # self.A_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/A_d.wav")
        # self.C1_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/C1_d.wav")
        # self.D1_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/D1_d.wav")
        # self.F1_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/F1_d.wav")
        # self.G1_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/G1_d.wav")
        # self.A1_d.set_path_sound(f"Music_Notes/{self.sound_list[self.var.get()]}/A1_d.wav")

        for btn in self.btns:
            btn.set_path_sound(self.sound_list[self.var.get()])

    def main(self):
        global thread_stop

        if self.button_record['text'] == 'Start':
            self.button_record['text'] = 'Stop'
            thread_stop = False  # Что-бы поток не остановился присваеваем False
            thread = threading.Thread(target=self.recording)
            thread.start()
        else:
            self.button_record['text'] = 'Start'
            thread_stop = True  # Присваеваем значение True и завершаем поток

    thread_stop = False

    def run(self):
        counter = 1
        while counter <= 5:
            if thread_stop == True: return  # Останавливаем цикл
            print(counter)
            counter += 1
            time.sleep(0.5)

    def recording(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 900
        WAVE_OUTPUT_FILENAME = "output.wav"

        index = self.check_index_device()
        # index2 = self.check_index_device()

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=index,
                        # output_device_index=index2,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            if self.button_record['text'] == 'Start':
                break

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

    def check_index_device(self):
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            if p.get_device_info_by_index(i)['name'] == 'Стерео микшер (Realtek(R) Audio':
                return i

    # def check_index_device2(self):
    #     p = pyaudio.PyAudio()
    #     for i in range(p.get_device_count()):
    #         if p.get_device_info_by_index(i)['name'] == 'Динамики (Realtek(R) Audio)':
    #             return i
