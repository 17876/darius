from matter import Marker
from timecode import Timecode

start = Timecode('0:25:12f', 25)
end = Timecode('0:29:13f', 25)
ma = Marker('Marker_01', start, end)
print(ma)