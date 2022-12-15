from midiutil.MidiFile import MIDIFile
from midiutil.MidiFile import *
# import sys
import random
# from io import parsefile, printfile

keys = {'C': 0, 'G': 7, 'D': 2, 'A': 9, 'E': 4, 'B': 11}
MAJOR = 0
MINOR = 1
SHARPS = 1
FLATS = -1
__all__ = ['MIDIFile', 'MAJOR', 'MINOR', 'SHARPS', 'FLATS']

KEY_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
KEY_NAMES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
KEY_SIG = {'C': 0, 'G': 1, 'D': 2, 'A': 3, 'E': 4, 'B': 5, 'F#': 6, 'C#': 7, 'Ab': 4, 'Eb': 3, 'Bb': 2, 'F': 1}

#        C  D  E  F  G  A  B
C_KEY = [0, 2, 4, 5, 7, 9, 11]
G_KEY = [0, 2, 4, 6, 7, 9, 11]
D_KEY = [1, 2, 4, 6, 7, 9, 11]
A_KEY = [1, 2, 4, 6, 8, 9, 11]
E_KEY = [1, 3, 4, 6, 8, 9, 11]
B_KEY = [1, 3, 4, 6, 8, 10, 11]
Fsharp_KEY = [1, 3, 5, 6, 8, 10, 11]
Csharp_KEY = [1, 3, 5, 6, 8, 10, 0]

Ab_KEY = [0, 1, 3, 5, 7, 8, 10]
Eb_KEY = [0, 2, 3, 5, 7, 8, 10]
Bb_KEY = [0, 2, 3, 5, 7, 9, 10]
F_KEY = [0, 2, 4, 5, 7, 9, 10]

SHARP_KEY = {0: C_KEY, 1: G_KEY, 2: D_KEY, 3: A_KEY, 4: E_KEY, 5: B_KEY, 6: Fsharp_KEY, 7: Csharp_KEY}
FLAT_KEY = {1: F_KEY, 2: Bb_KEY, 3: Eb_KEY, 4: Ab_KEY}

def rand_sign(x):
    return 1*x if random.random() < 0.5 else -1 * x


def find_key(start):
    if start % 12 == 0:
        key = 'C'
    elif start % 12 == 1:
        key = 'C#'
    elif start % 12 == 2:
        key = 'D'
    elif start % 12 == 3:
        key = 'Eb'
    elif start % 12 == 4:
        key = 'E'
    elif start % 12 == 5:
        key = 'F'
    elif start % 12 == 6:
        key = 'F#'
    elif start % 12 == 7:
        key = 'G'
    elif start % 12 == 8:
        key = 'Ab'
    elif start % 12 == 9:
        key = 'A'
    elif start % 12 == 10:
        key = 'Bb'
    elif start % 12 == 11:
        key = 'B'
    return key
    

class global_funcs():
    global nums
    def nums(lst, name, start):

        MyMIDI = MIDIFile(numTracks=2) 
        upper = 0
        lower = 1
        time = 0
        MyMIDI.addTrackName(upper, time, "Counterpoint")
        MyMIDI.addTrackName(lower, time, "Cantus Firmus")
        MyMIDI.addKeySignature(upper, time, KEY_SIG[find_key(start)], SHARPS, MAJOR)
        if 'b' in find_key(start) or find_key(start) == 'F':
            notes = FLAT_KEY[KEY_SIG[find_key(start)]]
        else:
            notes = SHARP_KEY[KEY_SIG[find_key(start)]]
        print(find_key(start), notes)
        channel = 0
        volume = 100
        duration = 1
        upper_start = start + 12
        lower_start = start - 12
        MyMIDI.addNote(upper, channel, upper_start, time, duration, volume)
        MyMIDI.addNote(lower, channel, lower_start, time, duration, volume)
        time = 1
        upper_old = upper_start
        lower_old = lower_start
        # old_pitch = curr_pitch = start
        for word in lst:
            for char in word:
                diff = ord(char) % 12
                for i in range(diff):
                    move = rand_sign(1)
                    if 88 - upper_old > 2 and upper_old - 60 > 2: 
                        if (upper_old + move) % 12 in notes:
                            MyMIDI.addNote(upper, channel, upper_old + move, time, duration, volume)
                            upper_old += move
                        else:
                            MyMIDI.addNote(upper, channel, upper_old + 2 * move, time, duration, volume)
                            upper_old += 2 * move
                    else:
                        if 88 - upper_old > upper_old - 60:
                            move = 1
                        else:
                            move = -1
                        # within upper and lower range
                        if (upper_old + move) % 12 in notes:
                            MyMIDI.addNote(upper, channel, upper_old + move, time, duration, volume)
                            upper_old += move
                        else:
                            MyMIDI.addNote(upper, channel, upper_old + 2 * move, time, duration, volume)
                            upper_old += 2 * move
                    # C2 = 36 and C4 = 60
                    if 60 - lower_old > 2 and lower_old - 36 > 2:
                        if (lower_old + -1 * move) % 12 in notes:
                            MyMIDI.addNote(lower, channel, lower_old + -1 * move, time, duration, volume)
                            lower_old += move
                        else:
                            MyMIDI.addNote(lower, channel, lower_old + -2 * move, time, duration, volume)
                            lower_old += 2 * move
                    else:
                        if 64 - lower_old > lower_old - 36:
                            move = 1
                        else:
                            move = -1
                        # within upper and lower range
                        if (lower_old + move) % 12 in notes:
                            MyMIDI.addNote(lower, channel, lower_old + move, time, duration, volume)
                            lower_old += move
                        else:
                            MyMIDI.addNote(lower, channel, lower_old + 2 * move, time, duration, volume)
                            lower_old += 2 * move
                    time += 1
                        

        with open("%s.mid" % name, 'wb') as outf:
            MyMIDI.writeFile(outf)

    global lst_to_mid
    def lst_to_mid(lst, name, start):
        if start % 12 == 0:
            key = 'C'
        elif start % 12 == 1:
            key = 'C#'
        elif start % 12 == 2:
            key = 'D'
        elif start % 12 == 3:
            key = 'Eb'
        elif start % 12 == 4:
            key = 'E'
        elif start % 12 == 5:
            key = 'F'
        elif start % 12 == 6:
            key = 'F#'
        elif start % 12 == 7:
            key = 'G'
        elif start % 12 == 8:
            key = 'Ab'
        elif start % 12 == 9:
            key = 'A'
        elif start % 12 == 10:
            key = 'Bb'
        elif start % 12 == 11:
            key = 'B'
            
        MyMIDI = MIDIFile(numTracks=2) 
        track = 0
        time = 0
        MyMIDI.addTrackName(track, time, "Sample Track")
        MyMIDI.addTempo(track, time, 120)
        MyMIDI.addKeySignature(track, time, KEY_SIG[key], SHARPS, MINOR)
        channel = 0
        volume = 100
        duration = 1
        old_pitch = start
        MyMIDI.addNote(track, channel, start, time, duration, volume)
        MyMIDI.addNote(track, channel, start - 12, time, duration, volume)
        for word in lst:
            for char in word:
                curr_pitch = (ord(char) + 60) % 88
                if (curr_pitch <= 90 and curr_pitch >= 65) or (curr_pitch >= 97 and curr_pitch <= 122):
                    pitch = old_pitch + (curr_pitch - old_pitch)
                    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
                elif curr_pitch >= 91:
                    pitch1 = curr_pitch // 2 - 2
                    MyMIDI.addNote(track, channel, pitch1, time, duration, volume)
                    pitch2 = curr_pitch // 2 + 2
                    MyMIDI.addNote(track, channel, pitch2, time, duration, volume)
                else:
                    curr_pitch += 60
                    pitch1 = curr_pitch // 2 - 2
                    MyMIDI.addNote(track, channel, pitch1, time, duration, volume)
                    pitch2 = curr_pitch // 2 + 2
                    MyMIDI.addNote(track, channel, pitch2, time, duration, volume)
                time += 1
                old_pitch = curr_pitch

        with open("%s.mid" % name, 'wb') as outf:
            MyMIDI.writeFile(outf)