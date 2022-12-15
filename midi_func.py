from midiutil.MidiFile import MIDIFile
from midiutil.MidiFile import *
# import sys
# import random
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

def applyRules(note, previous):
    options = [3, 4, 7, 8, 9, 12]  # all intervals allowed in counterpoint
    if previous is None:
        options = [7, 12]
    else:
        prev_int = previous[1] - previous[0]
        print(prev_int)
        print(options)
        if prev_int == 3 or prev_int == 4:  # no consecutive thirds
            options.remove(3)
            options.remove(4)
        elif prev_int == 8 or prev_int == 9:  # no consecutive sixths
            options.remove(8)
            options.remove(9)
        else:
            options.remove(prev_int)  # no consecutive 5ths or octaves

        # if we would approach 5th by parallel motion
        if (note + 7) - previous[1] > 0 and (note - previous[0]) > 0:
            if 7 in options:
                options.remove(7)
        elif (note + 7) - previous[1] < 0 and (note - previous[0]) < 0:
            if 7 in options:
                options.remove(7)

        for n in options:
            if abs((note + n) - previous[1]) > 7:
                options.remove(n)

    return options


# def gen(begin):
    

class global_funcs():
    global lst_to_mid
    def num(lst, name, start):
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
        upper = 0
        lower = 1
        time = 0
        MyMIDI.addTrackName(upper, time, "Counterpoint")
        MyMIDI.addTrackName(lower, time, "Cantus Firmus")
        MyMIDI.addKeySignature(upper, time, KEY_SIG[key], SHARPS, MINOR)
        channel = 0
        volume = 100
        duration = 1
        MyMIDI.addNote(upper, channel, start, time, duration, volume)
        MyMIDI.addNote(lower, channel, start - 12, time, duration, volume)
        time = 1
        for word in lst:
            for char in word:
                curr_pitch = ord(char)

                time += 1
        
        with open("%s.mid" % name, 'wb') as outf:
            MyMIDI.writeFile(outf)

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

    global nums
    def nums(lst, name, start):
        MyMIDI = MIDIFile(numTracks=2) 
        track = 0
        time = 0
        MyMIDI.addKeySignature(track, time, 0, 0, 1)
        MyMIDI.addTrackName(track, time, "Sample Track")
        MyMIDI.addTempo(track, time, 120)
        channel = 0
        volume = 100
        duration = 1
        old_pitch = start
        start_pitch1 = start
        start_pitch2 = start - 12

        MyMIDI.addNote(track, channel, start_pitch1, time, duration, volume)
        MyMIDI.addNote(track, channel, start_pitch2, time, duration, volume)
        time = 1

        for word in lst:
            for char in word:
                curr_pitch = ord(char) 
                if curr_pitch >= 84:
                    MyMIDI.addNote(track, channel, curr_pitch, time, duration, volume)
                    MyMIDI.addNote(track, channel, curr_pitch - 4, time, duration, volume)
                else:
                    MyMIDI.addNote(track, channel, curr_pitch, time, duration, volume)
                    MyMIDI.addNote(track, channel, curr_pitch - 7, time, duration, volume)
                time += 1

        with open("%s.mid" % name, 'wb') as outf:
            MyMIDI.writeFile(outf)