import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import mido

def convert_midi(file_path):
    midi_file = mido.MidiFile(file_path)


root = tk.Tk()

root.title("DrumChart")
root.minsize(700, 700)
root.maxsize(900, 900)
root.geometry("700x700")

root.columnconfigure(0, weight=1)
path_var = tk.StringVar(value="No file selected")
top_bar = ttk.Frame(root, padding=(10, 10))
top_bar.grid(row=0, column=0, sticky="ew")
top_bar.columnconfigure(1, weight=1)

def select_midi():
    filetypes = (
        [("MIDI Files", "*.mid")]
    )

    filename = fd.askopenfilename(
        title="Select a MIDI file",
        initialdir="/",
        filetypes=filetypes
    )

    if filename:
        path_var.set(filename)

open_button = ttk.Button(
    top_bar,
    text="Select MIDI File",
    command=select_midi
)
open_button.grid(row=0, column=0, padx=(0, 10), sticky="w")

path_entry = ttk.Entry(top_bar, textvariable=path_var, state="readonly")
path_entry.grid(row=0, column=1, sticky="ew")

root.mainloop()
