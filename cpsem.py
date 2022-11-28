from mido import MidiFile
import mido


mid = MidiFile('midi_files/mary.mid', clip=True)
# print(type(mid))
# print(type(mid.tracks))
# print(type(mid.tracks[1]))
# print(type(mid.tracks[1][5]))


# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
#     print('\n')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if type(msg) == mido.messages.messages.Message:
            try:
                print(msg, msg.note)
            except:
                print(msg)
        else:
            print(msg)
    print('\n')
