from mido import MidiFile

mid = MidiFile('canonpiano.mid', clip=True)
print(mid)

for track in mid.tracks:
    print(track)

# print('this is track[0]')
# print(mid.tracks[0])
# print('msgs')
# for msg in mid.tracks[0]:
#     print(msg)

print(len(mid.tracks[1]))
for i in range(1,10):
    print(mid.tracks[1][i])
for msg in mid.tracks[1]:
    print(msg)
    break