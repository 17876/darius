from matter import MatterDatabase
from util import range_scale, secs_to_timecode
from dash import Dash, Layer
from timecode import Timecode

db = MatterDatabase('materia.json', 'Videos')
layer1 = Layer()

projection_start_tc = Timecode('00:12:41:05f', 25)
projection_end_tc = Timecode('01:06:05:01f', 25)
projection_dur_sec = projection_end_tc._seconds - projection_start_tc._seconds

projection_dur_tc = Timecode(secs_to_timecode(projection_dur_sec, 'smpte', 25), 25)

for matter_name, matter in db._matters.items():
    counter = 1
    matter_markers = matter.markers
    matter_dur = matter.dur
    matter_dur_secs = matter.dur._seconds

    for marker_label, matter_marker in matter_markers.items():
        marker_start = matter_marker.start # timecode
        marker_end = matter_marker.end # timecode

        fr = matter_marker.start.fr

        marker_start_secs = marker_start._seconds
        marker_end_secs = marker_end._seconds
        marker_dur_secs = marker_end_secs - marker_start_secs

        dash_start_secs = range_scale(marker_start_secs, 0, matter_dur_secs, 0, projection_dur_sec)
        dash_end_secs = dash_start_secs + marker_dur_secs


        dash_start = Timecode(secs_to_timecode(dash_start_secs, 'smpte', fr), fr)
        dash_end = Timecode(secs_to_timecode(dash_end_secs, 'smpte', fr), fr)

        dash_name = '{:s}_{:02d}'.format(matter_name, counter)

        dash_to_add = Dash(dash_name, dash_start, dash_end)
        layer1.add_dash(dash_to_add)
        counter = counter + 1

print(layer1)
