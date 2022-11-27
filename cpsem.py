from mido import MidiFile
import mido

mid = MidiFile('midi_files/ValidCounterpoint.mid', clip=True)
print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

for msg in mid.play():
    port.send(msg)
# for track in mid.tracks:
#     print(track)

# print('this is track[0]')
# print(mid.tracks[0])
# print('msgs')
# for msg in mid.tracks[0]:
#     print(msg)

# print('here', mid.tracks)
# print('\n')
# for i in range(len(mid.tracks[0])):
#     print(mid.tracks[0][i])

# print('\n')
# for i in range(len(mid.tracks[1])):
#     print(mid.tracks[1][i])

# for msg in mid.tracks[1]:
#     print(msg)
#     break
# print('2:', mid.tracks)
# print('3:', mid.tracks[1])
# print('4:', mid.tracks[1][5])

# msg = mido.Message('note_on', note=60)
# print(msg)