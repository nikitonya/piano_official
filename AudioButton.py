import tkinter
import pygame


class AudioButton(tkinter.Button):
    def __init__(self, frame, name_button: str, path_sound: str, height: int, width: int, row:int, column:int):
        super().__init__()
        self.sound = pygame.mixer.Sound(path_sound)
        self.name_button = name_button

        self.btn = tkinter.Button(frame, text=name_button, height=height, width=width,
                                  font=('arial', 18, 'bold'), bd=4, bg='white', fg='black',
                                  command=self.play_sound).grid(row=row, column = column)

        # self.btn.grid(row = 15, column = 15)

    def play_sound(self) -> None:
        self.sound.play()

    def get_name_btn(self) -> str:
        return self.name_button
