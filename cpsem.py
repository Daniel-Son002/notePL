from mido import MidiFile
import mido


mid = MidiFile('InvalidCounterpoint.mid', clip=True)

track1 = []
track2 = []
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if type(msg) == mido.messages.messages.Message:
            try:
                # print(msg.note)
                if i == 1:
                    track1.append(msg.note)
                else:
                    track2.append(msg.note)
            except:
                print(msg)
        else:
            continue
    print('\n')
   
def  fourths(note1, note2):
    if (note1 % 12) - (note2 % 12) == 4:
        return False
    else:
        return True

def validIntervals(note1, note2):
    valid = [0, 4, 5, 7, 9, 12]
    if (note2 - note1) % 12 in valid:
        return True
    else:
        return False
    
def start(notes):
    if ((notes[0][1] - notes[0][0]) % 12 == 0) or ((notes[0][1] - notes[0][0]) % 12 == 7):
        return True
    else:
        return False
    
def end(notes):
    if ((notes[-1][1] - notes[-1][0]) % 12 == 0) or ((notes[-1][1] - notes[-1][0]) % 12 == 7):
        return True
    else:
        return False
    
    
temp = []
for i in range(0,len(track1),2):
    temp.append(track1[i])

track1 = temp
    
temp = []
for i in range(0, len(track2),2):
    temp.append(track2[i])

track2 = temp


notes = []
for a,b in zip(track1, track2):
    notes.append((a,b))
    
for i in range(len(track1)-1):
    if fourths(track1[i], track1[i+1]):
        continue
    else:
        print('This is not a valid counterpoint \n')
        print('Reason: There is a fourth between two notes on the same line')
        exit()
        
for i in range(len(track2)-1):
    if fourths(track2[i], track2[i+1]):
        continue
    else:
        print('This is not a valid counterpoint \n')
        print('Reason: There is a fourth between two notes on the same line')
        exit()

if ((notes[0][1] - notes[0][0]) % 12 == 0) or ((notes[0][1] - notes[0][0]) % 12 == 7):
    pass
else:
    print('This is not a valid counterpoint \n')
    print('Reason: Does not start on a perfect unison/octave or fifth')
    exit()

 
if ((notes[-1][1] - notes[-1][0]) % 12 != 0) or ((notes[-1][1] - notes[-1][0]) % 12 == 7):
    pass
else:
    print('This is not a valid counterpoint \n')
    print('Reason: Does not end on a perfect unison/octave or fifth')
    exit()


for a,b in notes:    
    if validIntervals(a,b):
        continue   
    else:
        print('This is not a valid counterpoint \n')
        print('Reason: Interval between notes have dissonance')
        exit()

print('This is a valid counterpoint')