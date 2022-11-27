from mido import MidiFile

mid = MidiFile('haydn_sq6.mid', clip=True)
print(mid)

for track in mid.tracks:
    print(track)

# print('this is track[0]')
# print(mid.tracks[0])
# print('msgs')
# for msg in mid.tracks[0]:
#     print(msg)

print(len(mid.tracks[1]))
for i in range(1,20):
    print(mid.tracks[1][i])
# for msg in mid.tracks[1]:
#     print(msg)
#     break