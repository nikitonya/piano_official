import tkinter
import pygame
import threading

class AudioButton(tkinter.Button):
    def __init__(self, frame: tkinter.Tk, name_button: str, path_sound: str, height: float, width: float, x: int,
                 y: int,
                 bg: str, fg: str, keyboard: str, anchor: str):
        super().__init__()
        self.frame = frame
        self.path_sound = path_sound
        self.sound = pygame.mixer.Sound(path_sound)
        self.name_button = name_button

        self.btn = tkinter.Button(self.frame, text=name_button, height=height, width=width,
                                  font=('arial', 18, 'bold'), bd=4, bg=bg, fg=fg,
                                  command=self.play_sound_click, anchor=anchor).place(x=x, y=y)

        self.frame.bind("<" + keyboard + ">", lambda event: self.play_sound(event))
        self.frame.focus_set()

    def change_volume(self, vol: float):
        self.sound.set_volume(vol)


    def play_sound(self, event) -> None:
        self.sound.play()

    def play_sound_click(self):
        self.sound.play()

    def get_name_btn(self) -> str:
        return self.name_button

    def set_path_sound(self, path):
        self.sound = pygame.mixer.Sound(
            "Music_Notes/" + path + '/' + self.get_name_btn() + '.wav')
