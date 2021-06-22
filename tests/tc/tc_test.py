from tc import Tc

t = Tc('0:12:12f', 25)
print(t.hmsf)
print(t._seconds)
print(t)
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