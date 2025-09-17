import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from midi_convert import convert_midi
import mido


root = tk.Tk()

root.title("DrumChart")
root.minsize(700, 700)
root.maxsize(900, 900)
root.geometry("700x700")
root.grid_columnconfigure(1, weight=3)
root.attributes('-topmost', True)
root.focus_force()

path_var = tk.StringVar(value="No file selected")

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
    root,
    text="Select MIDI File",
    command=select_midi
)
open_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

path_entry = ttk.Entry(
    root,
    textvariable=path_var, state="readonly"
    )
path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

start_button = ttk.Button(
    root,
    text="Start!!!",
    command=lambda: convert_midi(path_var.get())
)
start_button.grid(row=1, column=1, padx=10, pady=10, sticky="se")

root.lift()
root.attributes('-topmost', True)
root.attributes('-topmost', False)

root.mainloop()
