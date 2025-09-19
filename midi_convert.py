import mido
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import os

def convert_midi(file_path):
    if file_path == "No file selected":
        showinfo("Error", "No file selected")
        return
    else:
        mid = mido.MidiFile(file_path, clip=True)
        newMid = mido.MidiFile()
        newTrack = mido.MidiTrack()
        for track in mid.tracks:
            for msg in track:
                if msg.type in 'set_tempo':
                    newTrack.append(msg)
                    # bpm = mido.tempo2bpm(msg.tempo)
                if msg.type in ['note_on', 'note_off'] and msg.channel == 9:
                    newTrack.append(msg)
        newMid.ticks_per_beat = mid.ticks_per_beat
        newMid.tracks.append(newTrack)

        save_path = os.path.expanduser(savefilepath().name)
        newMid.save(save_path)

def savefilepath():
    filetypes = (
        [("MIDI File", "*.mid")]
    )

    path = fd.asksaveasfile(
        mode='w',
        defaultextension='.mid',
        filetypes=filetypes
    )

    return path