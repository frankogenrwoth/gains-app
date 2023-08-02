import tkinter as tk
from tkinter import messagebox
import pygame

def update_push_ups():
    global push_ups_count
    push_ups_count += 1
    push_ups_label.config(text=f"Push-ups: {push_ups_count}")

    if push_ups_count == 1000:
        messagebox.showinfo("Congratulations!", "You've completed 1000 push-ups!")
        play_song()

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("path/to/your/song.mp3")
    pygame.mixer.music.play()

# Initialize the push-ups count
push_ups_count = 0

# Create the main tkinter window
root = tk.Tk()
root.title("Push-ups Tracker")

# Push-ups label
push_ups_label = tk.Label(root, text="Push-ups: 0", font=("Helvetica", 20))
push_ups_label.pack(pady=20)

# Add push-up button
add_button = tk.Button(root, text="Add Push-up", command=update_push_ups, font=("Helvetica", 14))
add_button.pack()

# Run the tkinter main loop
root.mainloop()
