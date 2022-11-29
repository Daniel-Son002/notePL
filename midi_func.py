from midiutil.MidiFile import MIDIFile
from midiutil.MidiFile import *

keys = {'C': 0, 'G': 7, 'D': 2, 'A': 9, 'E': 4, 'B': 11}
MAJOR = 0
MINOR = 1
SHARPS = 1
FLATS = -1
__all__ = ['MIDIFile', 'MAJOR', 'MINOR', 'SHARPS', 'FLATS']

class global_funcs():
    global lst_to_mid
    def num(lst, name, start):
        if start % 12 == 0:
            key = 'C'
        elif start % 12 == 7:
            key = 'G'
        elif start % 12 == 2:
            key = 'D'
        elif start % 12 == 9:
            key = 'A'
        elif start % 12 == 4:
            key = 'E'
        elif start % 12 == 11:
            key = 'B'

        MyMIDI = MIDIFile(2) 
        upper = 0
        lower = 1
        time = 0
        MyMIDI.addTrackName(upper, time, "Counterpoint")
        MyMIDI.addTrackName(lower, time, "Cantus Firmus")
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
        MyMIDI = MIDIFile(1) 
        track = 0
        time = 0
        MyMIDI.addTrackName(track, time, "Sample Track")
        MyMIDI.addTempo(track, time, 120)
        MyMIDI.addKeySignature(track, time, 3, SHARPS, MINOR)
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
        MyMIDI = MIDIFile(1) 
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