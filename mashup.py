from midiutil.MidiFile import MIDIFile

mf = MIDIFile(1) 
track = 0
time = 0
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)
channel = 0
volume = 100
duration = 1
old_pitch = 0

sentence = 'Hello world! This my CS 252 project!'
lst = sentence.split(' ')

for word in lst:
    for char in word:
        curr_pitch = (ord(char) + 60) % 88
        if (curr_pitch <= 90 and curr_pitch >= 65) or (curr_pitch >= 97 and curr_pitch <= 122):
            pitch = old_pitch + (curr_pitch - old_pitch)
            mf.addNote(track, channel, pitch, time, duration, volume)
        elif curr_pitch >= 91:
            pitch1 = curr_pitch // 2 - 2
            mf.addNote(track, channel, pitch1, time, duration, volume)
            pitch2 = curr_pitch // 2 + 2
            mf.addNote(track, channel, pitch2, time, duration, volume)
        else:
            curr_pitch += 60
            pitch1 = curr_pitch // 2 - 2
            mf.addNote(track, channel, pitch1, time, duration, volume)
            pitch2 = curr_pitch // 2 + 2
            mf.addNote(track, channel, pitch2, time, duration, volume)
        time += 1
        old_pitch = curr_pitch

with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)