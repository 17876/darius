from timecode import Timecode

tc = Timecode('0:12:12f', 25)
print(tc.timecode)
print(tc._seconds)
print('')

# tc.fps = 30
# print(tc.timecode)
# print(tc._seconds)
# print('')
#
# tc.mutate()
# print(tc.timecode)
# print(tc._seconds)
# print(tc)
# print('')
#
# tc.mutate()
# print(tc.timecode)
# print(tc._seconds)
#
# print(tc)