from Window import Window



# #def create_win():
#     w = 1280
#     h = 720
#     win = tk.Tk()
#     pygame.init()
#
#     icon = tk.PhotoImage(file='Icon.png')
#     win.title('Piano')
#     win.iconphoto(False, icon)
#     win.config(bg='white')  # цвет бэкграунда
#     win.geometry(f"{w}x{h}+170+50")  # значение в пикселях и запускать в 10 пикселях от левого верхнего края
#     win.resizable(False, False)  # запрет расширения окна
#     win.attributes('-fullscreen', False)
#
#     frame_top = tk.Frame(win)
#     frame_top.grid()
#
#     frame_actions = tk.Frame(win)
#     frame_actions.grid()
#
#     label_piano = tk.Label(frame_top, text='Piano!',
#                            bg='red',
#                            fg='black',
#                            font=('Times new Roman', 40, 'bold'),
#                            width=40,
#                            height=4,
#                            justify=tk.CENTER
#                            )
#     label_piano.grid()
#
#     frame_notes = tk.Frame(win)
#     frame_notes.grid(stick='w')
#
#     frame_notes2 = tk.Frame(win)
#     frame_notes2.grid()
#
#     # frame_notes
#     btnspace = tk.Button(frame_notes, state=tk.DISABLED, height=13, width=27, bg='white', fg='white', relief=tk.FLAT)
#     btnspace.grid(row=0, column=0)
#     btn1 = AudioButton(frame_notes, 'Do Dies', "Music_Notes/Piano/C_s.wav", 6, 5, 0, 1, 'black', 'white')
#     btn2 = AudioButton(frame_notes, 'Re Dies', "Music_Notes/Piano/D_s.wav", 6, 5, 0, 2, 'black', 'white')
#     btnspace1 = tk.Button(frame_notes, state=tk.DISABLED, height=13, width=11, bg='white', fg='white', relief=tk.FLAT)
#     btnspace1.grid(row=0, column=3)
#     btn3 = AudioButton(frame_notes, 'Fa', "Music_Notes/Piano/F_s.wav", 6, 5, 0, 4, 'black', 'white')
#     btn4 = AudioButton(frame_notes, 'Sol', "Music_Notes/Piano/G_s.wav", 6, 5, 0, 5, 'black', 'white')
#     btn5 = AudioButton(frame_notes, 'Lya', "Music_Notes/Piano/Bb.wav", 6, 5, 0, 6, 'black', 'white')
#     btnspace2 = tk.Button(frame_notes, state=tk.DISABLED, height=13, width=11, bg='white', fg='white', relief=tk.FLAT)
#     btnspace2.grid(row=0, column=7)
#     btn6 = AudioButton(frame_notes, 'Do', "Music_Notes/Piano/C_s1.wav", 6, 5, 0, 8, 'black', 'white')
#     btn7 = AudioButton(frame_notes, 'Re', "Music_Notes/Piano/D_s1.wav", 6, 5, 0, 9, 'black', 'white')
#
#     # frame_notes2
#     Do = AudioButton(frame_notes2, 'Do', "Music_Notes/Piano/C.wav", 6, 5, 0, 1, 'white', 'black')
#     Re = AudioButton(frame_notes2, 'Re', "Music_Notes/Piano/D.wav", 6, 5, 0, 2, 'white', 'black')
#     Mi = AudioButton(frame_notes2, 'Mi', "Music_Notes/Piano/E.wav", 6, 5, 0, 3, 'white', 'black')
#     Fa = AudioButton(frame_notes2, 'Fa', "Music_Notes/Piano/F.wav", 6, 5, 0, 4, 'white', 'black')
#     Sol = AudioButton(frame_notes2, 'Sol', "Music_Notes/Piano/G.wav", 6, 5, 0, 5, 'white', 'black')
#     Lya = AudioButton(frame_notes2, 'Lya', "Music_Notes/Piano/A.wav", 6, 5, 0, 6, 'white', 'black')
#     Si = AudioButton(frame_notes2, 'Si', "Music_Notes/Piano/B.wav", 6, 5, 0, 7, 'white', 'black')
#     Do1 = AudioButton(frame_notes2, 'Do', "Music_Notes/Piano/C1.wav", 6, 5, 0, 8, 'white', 'black')
#     Re1 = AudioButton(frame_notes2, 'Re', "Music_Notes/Piano/D1.wav", 6, 5, 0, 9, 'white', 'black')
#     Mi1 = AudioButton(frame_notes2, 'Mi', "Music_Notes/Piano/E1.wav", 6, 5, 0, 10, 'white', 'black')
#     Fa1 = AudioButton(frame_notes2, 'Fa', "Music_Notes/Piano/F1.wav", 6, 5, 0, 11, 'white', 'black')
#     Fa2 = AudioButton(frame_notes2, 'Fa2', "Music_Notes/Piano/F2.wav", 6, 5, 0, 12, 'white', 'black')
#
#     sound_list = ['Piano', 'Steel_Drum']
#
#     def change():
#         btn1.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/C_s.wav")
#         btn2.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/D_s.wav")
#         btn3.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/F_s.wav")
#         btn4.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/G_s.wav")
#         btn5.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/Bb.wav")
#         btn6.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/C_s1.wav")
#         btn7.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/D_s1.wav")
#
#         Do.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/C.wav")
#         Re.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/D.wav")
#         Mi.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/E.wav")
#         Fa.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/F.wav")
#         Sol.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/G.wav")
#         Lya.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/A.wav")
#         Si.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/B.wav")
#         Do1.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/C1.wav")
#         Re1.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/D1.wav")
#         Mi1.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/E1.wav")
#         Fa1.set_path_sound(f"Music_Notes/{sound_list[var.get()]}/F1.wav")
#
#     var = tk.IntVar()
#     var.set(0)
#     piano = tk.Radiobutton(frame_actions, text='Piano', variable=var, value=0)
#     steel_drum = tk.Radiobutton(frame_actions, text='Steel_Drum', variable=var, value=1)
#     button_change = tk.Button(frame_actions, text='Изменить', command=change)
#
#     piano.grid(stick='w', row=0, column=0)
#     steel_drum.grid(stick='w', row=1, column=0)
#     button_change.grid(stick='w', row=2, column=0)
#
#     win.mainloop()


# def recording():
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

# def getdevice():
#     p = pyaudio.PyAudio()
#
#     for i in range(p.get_device_count()):
#         print(i, p.get_device_info_by_index(i)['name'])





def main():
    app = Window()


if __name__ == '__main__':
    main()

