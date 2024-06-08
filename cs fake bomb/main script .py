import random
import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import time

# Initialize pygame mixer
pygame.mixer.init()

# List of keypress sound effect files with full paths
keypress_sounds = [
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\1.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\2.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\3.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\4.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\5.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\6.wav",
    r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\keypress\7.wav"
]

# Function to play a random keypress sound
def play_random_keypress_sound():
    sound = random.choice(keypress_sounds)
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

def play_plant_sound(callback):
    pygame.mixer.music.load(r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\bomb\plant.wav")
    pygame.mixer.music.play()
    # Simulate the plant sound playing for 3 seconds
    time.sleep(3)
    callback()

def play_defuse_sound():
    pygame.mixer.music.load(r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\bomb\defuse.wav")
    pygame.mixer.music.play()

def play_bomb_beep_and_explosion():
    pygame.mixer.music.load(r"C:\Users\DJche\OneDrive\Documents\projects\cs fake bomb\sounds\bomb\bomb beep + explosion.wav")
    pygame.mixer.music.play()

def gen_code(length=5):
    return ''.join(random.choices('0123456789', k=length))

def start_arming():
    global arming_code, armed, countdown_active, arming_started
    arming_code = gen_code()
    code_label.config(text=f"Arming code: {arming_code}")
    countdown_label.config(text="")
    entry.delete(0, tk.END)
    entry.config(state="normal")
    armed = False
    countdown_active = False
    arming_started = True

def arm_bomb():
    global arming_code, armed
    if not arming_started:
        messagebox.showinfo("Result", "Please start arming first!")
        return
    
    user_input = entry.get()
    play_random_keypress_sound()  # Play sound when a key is pressed
    if user_input == arming_code:
        armed = True
        entry.delete(0, tk.END)
        start_countdown()
        threading.Thread(target=play_plant_sound, args=(play_bomb_beep_and_explosion,)).start()
    else:
        messagebox.showinfo("Result", "Incorrect arming code!")
        entry.delete(0, tk.END)

def start_countdown():
    global code, countdown_time, countdown_active
    if armed:
        code = gen_code()
        code_label.config(text=f"Your code is: {code}")
        countdown_time = 39
        countdown_label.config(text=str(countdown_time))
        entry.delete(0, tk.END)
        entry.config(state="normal")
        countdown_active = True
        root.after(1000, update_countdown)

def update_countdown():
    global countdown_time
    if countdown_time > 0 and countdown_active:
        countdown_time -= 1
        countdown_label.config(text=str(countdown_time))
        root.after(1000, update_countdown)
    elif countdown_time == 0:
        countdown_label.config(text="Time's up!")
        entry.config(state="normal")

def check_code():
    global countdown_active
    user_input = entry.get()
    play_random_keypress_sound()  # Play sound when a key is pressed
    if user_input == code:
        countdown_active = False
    else:
        messagebox.showinfo("Result", "Incorrect code!")

root = tk.Tk()
root.title("BOMB")

arming_code = ""
code = ""
countdown_time = 37
armed = False
countdown_active = False
arming_started = False

code_label = tk.Label(root, text="", font=("Helvetica", 16))
code_label.pack(pady=20)

countdown_label = tk.Label(root, text="", font=("Helvetica", 48))
countdown_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 16), justify='center')
entry.pack(pady=20)
entry.config(state="normal")

# Bind the keypress event to play the sound
def on_keypress(event):
    play_random_keypress_sound()

entry.bind("<KeyPress>", on_keypress)

submit_button = tk.Button(root, text="Submit Code", command=lambda: [check_code(), play_defuse_sound()], font=("Helvetica", 16))
submit_button.pack(pady=20)

arm_button = tk.Button(root, text="Arm Bomb", command=arm_bomb, font=("Helvetica", 16))
arm_button.pack(pady=20)

start_arming_button = tk.Button(root, text="Start Arming", command=lambda: [start_arming(), play_random_keypress_sound()], font=("Helvetica", 16))
start_arming_button.pack(pady=20)

root.mainloop()
