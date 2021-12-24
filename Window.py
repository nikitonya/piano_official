import pygame
import tkinter as tk
from AudioButton import AudioButton
import wave
import pyaudio
import threading
import time
import tkinter.messagebox as mb


class Window():

    def __init__(self):
        w = 1250
        h = 760
        self.win = tk.Tk()
        pygame.init()
        icon = tk.PhotoImage(file='Icon.png')
        self.win.title('Piano')
        self.win.iconphoto(False, icon)
        self.win.config(bg='MediumPurple1')  # цвет бэкграунда
        self.win.geometry(f"{w}x{h}+155+40")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
        self.win.resizable(False, False)  # запрет расширения окна
        self.win.attributes('-fullscreen', False)
        self.vol = 1

        self.help = tk.Button(self.win, bg='white', text='Help', height=2, width=10, command=self.show_readme,fg='SpringGreen4')
        self.help.place(x=1150, y=80)

        self.frame_top = tk.Frame(self.win)
        self.frame_top.grid()

        self.frame_space0 = tk.Frame(self.win, bg='MediumPurple1', background='MediumPurple1')
        self.frame_space0.grid()
        self.btnspace0 = tk.Button(self.frame_space0, state=tk.DISABLED, height=1, width=22, bg='MediumPurple1',
                                   fg='MediumPurple1',
                                   relief=tk.FLAT)
        self.btnspace0.grid(row=0, column=0)

        self.frame_actions = tk.Frame(self.win, bg='MediumPurple1')
        self.frame_actions.grid()

        self.label_piano = tk.Label(self.frame_top, text='Piano!',
                                    bg='MediumPurple1',
                                    fg='black',
                                    font=('Times new Roman', 40, 'bold'),
                                    width=40,
                                    height=1,
                                    justify=tk.CENTER
                                    )
        self.label_piano.grid()

        # piano_notes
        self.C = AudioButton(self.win, 't', "Music_Notes/Piano_classic/t.wav", 16, 4, 117, 240, 'white', 'black',
                             't', 's')
        self.D = AudioButton(self.win, 'y', "Music_Notes/Piano_classic/y.wav", 16, 4, 190, 240, 'white', 'black',
                             'y', 's')
        self.E = AudioButton(self.win, 'u', "Music_Notes/Piano_classic/u.wav", 16, 4, 263, 240, 'white', 'black',
                             'u', 's')
        self.F = AudioButton(self.win, 'i', "Music_Notes/Piano_classic/i.wav", 16, 4, 336, 240, 'white', 'black',
                             'i', 's')
        self.G = AudioButton(self.win, 'o', "Music_Notes/Piano_classic/o.wav", 16, 4, 409, 240, 'white', 'black',
                             'o', 's')
        self.A = AudioButton(self.win, 'p', "Music_Notes/Piano_classic/p.wav", 16, 4, 482, 240, 'white', 'black',
                             'p', 's')
        self.B = AudioButton(self.win, 'a', "Music_Notes/Piano_classic/a.wav", 16, 4, 555, 240, 'white', 'black',
                             'a', 's')
        self.C1 = AudioButton(self.win, 's', "Music_Notes/Piano_classic/s.wav", 16, 4, 628, 240, 'white', 'black',
                              's', 's')
        self.D1 = AudioButton(self.win, 'd', "Music_Notes/Piano_classic/d.wav", 16, 4, 701, 240, 'white', 'black',
                              'd', 's')
        self.E1 = AudioButton(self.win, 'f', "Music_Notes/Piano_classic/f.wav", 16, 4, 774, 240, 'white',
                              'black', 'f', 's')
        self.F1 = AudioButton(self.win, 'g', "Music_Notes/Piano_classic/g.wav", 16, 4, 847, 240, 'white',
                              'black', 'g', 's')
        self.G1 = AudioButton(self.win, 'h', "Music_Notes/Piano_classic/h.wav", 16, 4, 920, 240, 'white',
                              'black', 'h', 's')
        self.A1 = AudioButton(self.win, 'j', "Music_Notes/Piano_classic/j.wav", 16, 4, 993, 240, 'white',
                              'black', 'j', 's')
        self.B1 = AudioButton(self.win, 'k', "Music_Notes/Piano_classic/k.wav", 16, 4, 1066, 240, 'white',
                              'black', 'k', 's')
        # Dies-notes
        self.C_d = AudioButton(self.win, 'T_d', "Music_Notes/Piano_classic/T_d.wav", 10, 3, 160, 240, 'black', 'white',
                               'T', 's')
        self.D_d = AudioButton(self.win, 'Y_d', "Music_Notes/Piano_classic/Y_d.wav", 10, 3, 233, 240, 'black', 'white',
                               'Y', 's')
        self.F_d = AudioButton(self.win, 'I_d', "Music_Notes/Piano_classic/I_d.wav", 10, 3, 379, 240, 'black', 'white',
                               'I', 's')
        self.G_d = AudioButton(self.win, 'O_d', "Music_Notes/Piano_classic/O_d.wav", 10, 3, 452, 240, 'black', 'white',
                               'O', 's')
        self.A_d = AudioButton(self.win, 'P_d', "Music_Notes/Piano_classic/P_d.wav", 10, 3, 525, 240, 'black', 'white',
                               'P', 's')

        self.C1_d = AudioButton(self.win, 'S_d', "Music_Notes/Piano_classic/S_d.wav", 10, 3, 671, 240, 'black',
                                'white', 'S', 's')
        self.D1_d = AudioButton(self.win, 'D_d', "Music_Notes/Piano_classic/D_d.wav", 10, 3, 744, 240, 'black',
                                'white', 'D', 's')
        self.F1_d = AudioButton(self.win, 'G_d', "Music_Notes/Piano_classic/G_d.wav", 10, 3, 890, 240, 'black',
                                'white', 'G', 's')
        self.G1_d = AudioButton(self.win, 'H_d', "Music_Notes/Piano_classic/H_d.wav", 10, 3, 963, 240, 'black',
                                'white', 'H', 's')
        self.A1_d = AudioButton(self.win, 'J_d', "Music_Notes/Piano_classic/J_d.wav", 10, 3, 1036, 240, 'black',
                                'white', 'J', 's')

        self.btns = [self.C, self.D, self.E, self.F, self.G, self.A, self.B, self.C1, self.D1, self.E1, self.F1,
                     self.G1, self.A1, self.B1, self.C_d, self.D_d, self.F_d, self.G_d, self.A_d, self.C1_d, self.D1_d,
                     self.F1_d, self.G1_d, self.A1_d]

        self.sound_list = ['Piano_classic', 'Guitar']

        # button_space
        self.btnspace1 = tk.Button(self.frame_actions, state=tk.DISABLED, height=1, width=0, bg='MediumPurple1',
                                   fg='white',
                                   relief=tk.FLAT)
        self.btnspace1.grid(row=0, column=0)

        # frame_button_record
        self.frame_button_record = tk.LabelFrame(self.frame_actions, text='Record', bg='MediumPurple1')
        self.frame_button_record.grid(row=0, column=1)
        # button_record
        self.button_record = tk.Button(self.frame_button_record, text='Start', command=self.main, height=5, width=10,fg='SpringGreen4')
        self.button_record.grid(row=0, column=0)

        # button_space2
        self.btnspace2 = tk.Button(self.frame_actions, state=tk.DISABLED, height=1, width=16, bg='MediumPurple1',
                                   fg='white',
                                   relief=tk.FLAT)
        self.btnspace2.grid(row=0, column=2)

        # frame_radiobuttons
        self.frame_radio = tk.LabelFrame(self.frame_actions, text='Sound pack', bg='MediumPurple1')
        self.frame_radio.grid(row=0, column=3, stick='s')
        # RedioButtons
        self.var = tk.IntVar()
        self.var.set(0)
        self.piano = tk.Radiobutton(self.frame_radio, text='Piano', variable=self.var, value=0, indicatoron=0,
                                    command=self.change, height=5, width=10, fg='SpringGreen4')
        self.piano.grid(row=0, column=1)
        self.Guitar = tk.Radiobutton(self.frame_radio, text='Guitar', variable=self.var, value=1,
                                     indicatoron=0, command=self.change, height=5, width=10,
                                     fg='SpringGreen4')
        self.Guitar.grid(row=0, column=2)
        self.accordion = tk.Radiobutton(self.frame_radio, text='Accordion', variable=self.var, value=2,
                                        indicatoron=0, command=self.change, height=5, width=10,
                                        fg='SpringGreen4')
        self.accordion.grid(row=0, column=3)
        self.violin = tk.Radiobutton(self.frame_radio, text='Violin', variable=self.var, value=3,
                                     indicatoron=0, command=self.change, height=5, width=10,
                                     fg='SpringGreen4')
        self.violin.grid(row=0, column=4)

        # button_space
        self.btnspace3 = tk.Button(self.frame_actions, state=tk.DISABLED, height=1, width=15, bg='MediumPurple1',
                                   fg='white',
                                   relief=tk.FLAT)
        self.btnspace3.grid(row=0, column=4)

        # VolumeFrame
        self.frame_volume = tk.LabelFrame(self.frame_actions, text='Volume', bg='MediumPurple1')
        self.frame_volume.grid(row=0, column=5)

        # function for volume bar
        def volume(vol):
            for btn in self.btns:
                btn.change_volume(int(vol) / 100)

        # volume img
        self.volimg = tk.PhotoImage(file='vol.png')
        volimg = tk.Label(self.frame_volume, image=self.volimg).grid(row=0, column=3)

        # volume bar
        self.scale = tk.Scale(self.frame_volume, from_=0, to=100, orient=tk.HORIZONTAL, bg='MediumPurple1', length=200,
                              command=volume)
        self.scale.set(100)
        self.scale.grid(row=0, column=4)

        self.win.mainloop()

    def change(self):
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
        #index2 = self.check_index_device()

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=index,
                        #output_device_index=index2,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            if self.button_record['text'] == 'Start':
                break

        print("* done recording")
        self.show_info()

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
                print(i, p.get_device_info_by_index(i)['name'])
                return i

    # def check_index_device2(self):
    #     p = pyaudio.PyAudio()
    #     for i in range(p.get_device_count()):
    #         if p.get_device_info_by_index(i)['name'] == 'Динамики (Realtek(R) Audio)':
    #             return i

    def show_info(self):
        msg = 'Запись прошла успешно. Для прослушивания загляните в корневую папку и откройте файл "output.wav".'
        mb.showinfo('Внимание', msg)

    def show_readme(self):
        msg = 'Добро пожаловать в Виртуальное пианино!\n\n' \
              'В данном пианино вам предоставляется возможность поиграть ' \
              'в него как с мыши, так и с клавитуры. \n' \
              'Для игры при помощи клавитуры перейдите на английскую раскладку и воспользуйтесь клавишами:\n\n' \
              '\t T Y    I O P    S D  G H J \n' \
              '\tt y u i o p a s d f g h j k \n\n' \
              'Также вы можете записать свою проигранную мелодию. Для этого нажмите на клавишу "Start"' \
              'и когда вам нужно прекратить запись, нажмите клавишу "Stop".\n\n' \
              'И для разнообразия вы можете сменять наборы звуков над центральным пианино.\n\n' \
              'Удачи в изучении музыки!'
        mb.showinfo('Инструкция', msg)
