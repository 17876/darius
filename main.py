from matter import MatterDatabase
from util import range_scale
from dash import Dash, Layer


db = MatterDatabase('materia.json')
layer1 = Layer()
piece_dur = 3600

for matter_name, matter in db._matters.items():
    counter = 1
    matter_markers = matter.markers
    matter_dur = matter.dur

    for marker_label, matter_marker in matter_markers.items():
        marker_start = matter_marker.start
        marker_end = matter_marker.end
        dash_start = range_scale(marker_start, 0, matter_dur, 0, piece_dur)
        dash_name = '{:s}_{:02d}'.format(matter_name, counter)
        dash_dur = marker_end - marker_start
        dash_to_add = Dash(dash_name, dash_start, dash_dur)
        layer1.add_dash(dash_to_add)
        counter = counter + 1

print(layer1)
