import tkinter as tk
from tkinter import ttk
import mido

def convert_midi(file_path):
    midi_file = mido.MidiFile(file_path)