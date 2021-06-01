import json
from timecode import Timecode

# Marker class
class Marker:
    def __init__(self, label, start, end=None):
        self.label = label
        self.start = start # timecode
        self.end = end # timecode

    def __str__(self):
        if self.end:
            line = 'Marker:\t{}\nStart:\t{}\nEnd:\t{}\n'.format(self.label, self.start.__str__(), self.end.__str__())
        else:
            line = 'Marker:\t{}\nStart:\t{}\n'.format(self.label.__str__(), self.start.__str__())
        return line

# Matter is the class for raw input materials like audios and videos
class Matter:
    def __init__(self, name, dur, markers=None):
        self.name = name
        self.dur = dur # timecode
        # markers is a dict
        if markers:
            self.markers = markers

class VideoMatter(Matter):
    def __init__(self, name, dur, fr, markers=None):
        super().__init__(name, dur, markers)
        self._fr = fr

# Loads and stores matters
class MatterDatabase:
    def __init__(self, database_filename, database_name):
        self.database_filename = database_filename
        self._database_name = database_name
        self._matters = {} # here the matters are stored

        # Loading json to a dictionary
        with open(self.database_filename, 'r') as read_file:
            json_matters = json.load(read_file)

        for key, json_matter in json_matters.items():
            matter_name = key
            json_matter_type = json_matter['type']
            json_matter_dur = json_matter['dur']
            if json_matter_type == 'v':
                json_matter_fr = json_matter['fr']
                matter_dur = Timecode(json_matter_dur, json_matter_fr)
            else:
                matter_dur = Timecode(json_matter_dur)
            json_markers = json_matter['markers']
            matter_markers = {}
            for marker_key, json_marker in json_markers.items():
                json_marker_start = json_marker['start']
                json_marker_end = json_marker['end']
                if json_matter_type == 'v':
                    marker_start = Timecode(json_marker_start, json_matter_fr)
                    marker_end = Timecode(json_marker_end, json_matter_fr)
                else:
                    marker_start = Timecode(json_marker_start)
                    marker_end = Timecode(json_marker_end)
                matter_markers[marker_key] = Marker(marker_key, marker_start, marker_end)

            self._matters[matter_name] = self._create_video_matter(matter_name, matter_dur, json_matter_fr,
                                                                   matter_markers)

    def _create_video_matter(self, name, dur, fr, markers):
            return VideoMatter(name, dur, fr, markers)

    def _print(self):
        print('=======================================')
        print('Matter Database: {:s}'.format(self._database_name))
        for key, matter in self._matters.items():
            matter_name = key
            matter_dur = matter.dur # timecode
            matter_markers = matter.markers # dict of objects
            print('=======================================')
            print('Name:\t\t{}'.format(matter_name))
            print('Dur:\t\t{:s}'.format(matter_dur.__str__()))
            print('\nMarkers:\n')
            for marker_key, marker in matter_markers.items():
                print(marker)
        print('=======================================')

    def __str__(self):
        self._print()
        return 'Print Done'