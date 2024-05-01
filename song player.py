import os
import pygame
from tkinter import *
from tkinter import filedialog

pygame.mixer.init()


music_dir = "C:/Users/YourUsername/Music"


def get_emoji(name):
    emojis = {
        "play": "Play",
        "pause": "Pause",
        "resume": "Resume",
        "stop": "Stop",
        "folder": ""
    }
    return emojis[name]


def browse_files():
    global music_dir
    music_dir = filedialog.askdirectory(initialdir=music_dir, title="Select Music Directory")
    load_playlist()


def load_playlist():
    global songs
    songs = [os.path.basename(f) for f in os.listdir(music_dir) if f.endswith(".mp3")]
    create_song_buttons(songs)


def play_song(song_index):
    song_path = os.path.join(music_dir, songs[song_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()


def create_song_buttons(songs):
    
    for widget in songs_frame.winfo_children():
        widget.destroy()

    
    for i, song in enumerate(songs):
        button_text = f"{get_emoji('play')} {song}"
        button = Button(songs_frame, text=button_text, command=lambda index=i: play_song(index), width=10, height=2, fg='white', bg='gray', font=('Arial', 12))
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)


def control_music(action):
    if action == "pause":
        pygame.mixer.music.pause()
    elif action == "resume":
        pygame.mixer.music.unpause()
    elif action == "stop":
        pygame.mixer.music.stop()


root = Tk()
root.title("Music Player")
root.configure(bg='darkgray')


control_frame = Frame(root, bg='black')  
control_frame.pack(pady=20, fill=X)  


button_width = 5
button_height = 2
button_font = ('Arial', 12)

play_button = Button(control_frame, text=get_emoji('play'), command=lambda: play_song(0), width=button_width, height=button_height, fg='white', bg='gray', font=button_font)
play_button.grid(row=0, column=0, padx=5)

pause_button = Button(control_frame, text=get_emoji('pause'), command=lambda: control_music("pause"), width=button_width, height=button_height, fg='white', bg='gray', font=button_font)
pause_button.grid(row=0, column=1, padx=5)

resume_button = Button(control_frame, text=get_emoji('resume'), command=lambda: control_music("resume"), width=button_width, height=button_height, fg='white', bg='gray', font=button_font)
resume_button.grid(row=0, column=2, padx=5)

stop_button = Button(control_frame, text=get_emoji('stop'), command=lambda: control_music("stop"), width=button_width, height=button_height, fg='white', bg='gray', font=button_font)
stop_button.grid(row=0, column=3, padx=5)


songs_frame = Frame(root, bg='darkgray')
songs_frame.pack(pady=20)


browse_button = Button(root, text=f"{get_emoji('folder')} Browse", command=browse_files, width=10, height=2, fg='white', bg='gray', font=('Arial', 12))
browse_button.pack(pady=10, fill=X)  

root.mainloop()
