import pygame
from pynput import keyboard
import os

pygame.mixer.init()
music_folder = "music"
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]

current_index = 0

def play_music():
    if playlist:
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        print(f"Playing: {os.path.basename(playlist[current_index])}")
    else:
        print("Playlist is empty.")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_track():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        play_music()

def prev_track():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        play_music()

def on_press(key):
    try:
        if key.char == ' ':
            play_music()
        elif key.char == 's':
            stop_music()
        elif key.char == 'n':
            next_track()
        elif key.char == 'p':
            prev_track()
    except AttributeError:
        pass
    
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Music player is running...\nControls:\nSPACE - Play\nS - Stop\nN - Next track\nP - Previous track") 