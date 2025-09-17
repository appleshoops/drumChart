import mido
import tkinter
from tkinter.messagebox import showinfo

def convert_midi(file_path):
    if file_path == "No file selected":
        showinfo("Error", "No file selected")
        return
    else:
        mid = mido.MidiFile(file_path, clip=True)
        for track in mid.tracks:
            print(track)