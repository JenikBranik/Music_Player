import pygame
import hud
from tkinter import Tk, filedialog
import os
import shutil

# Complete player settings

pygame.init()
pygame.mixer.init()
choose_file = ""
actual_position = 0

'''
State of the music for function of programme
@:param hud.state if it is equal to any word (play,pause,continue)
@:return functions 
'''


def state_of_music():
    if hud.state == "Play":
        play_music()
    elif hud.state == "Pause":
        pause_music()
    elif hud.state == "Continue":
        continue_music()


'''
Play a music
@:return play music and string Pause
'''


def play_music():
    global actual_position
    global choose_file
    pygame.mixer.music.load(choose_file)
    pygame.mixer.music.play(start=actual_position)
    hud.button.configure(text="Pause")
    hud.state = "Pause"


'''
Pause music
@:return stop music and string Continue
'''


def pause_music():
    global actual_position
    pygame.mixer.music.pause()
    actual_position = pygame.mixer.music.get_pos()
    hud.button.configure(text="Continue")
    hud.state = "Continue"


'''
@:return continu in music
'''


def continue_music():
    pygame.mixer.music.unpause()
    hud.button.configure(text="Pause")
    hud.state = "Pause"


'''
Chose the music to play
@:return mp3 file to play
'''


def add_music():
    global choose_file
    root = Tk()
    root.withdraw()
    choose_file = filedialog.askopenfilename()


def loop():
    while True:
        play_music()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.wait()


'''
complete end of music
@:return End music and stirng play
'''


def end():
    global actual_position
    pygame.mixer.music.stop()
    actual_position = 0
    hud.state = "Play"
    hud.button.configure(text="Play")


