import json

class Marker:
    def __init__(self, label, start, end=None):
        self.label = label
        self.start = start
        self.end = end

    def __str__(self):
        if self.end:
            line = 'Marker: {:s}\nStart: {:.03f}\nEnd: {:.03f}\n'.format(self.label, self.start, self.end)
        else:
            line = 'Marker: {:s}\nStart: {:.03f}\n'.format(self.label, self.start)
        return line

# Matter is the class for raw input materials like audios and videos
class Matter:
    def __init__(self, name, dur, markers=None):
        self.name = name
        self.dur = dur
        # markers is a dict
        if markers:
            self.markers = markers

# Loads and stores matters
class MatterDatabase:
    def __init__(self, database_filename):
        self.database_filename = database_filename
        self._matters = {}

        # Loading json to a dictionary
        with open(self.database_filename, 'r') as read_file:
            json_matters = json.load(read_file)

        for key, json_matter in json_matters.items():
            matter_name = key
            matter_dur = json_matter['dur']
            json_markers = json_matter['markers']
            matter_markers = {}

            for marker_key, json_marker in json_markers.items():
                marker_start = json_marker['start']
                marker_end = json_marker['end']
                matter_markers[marker_key] = Marker(marker_key, marker_start, marker_end)

            self._matters[key] = self._create_matter(matter_name, matter_dur, matter_markers)

    def _create_matter(self, name, dur, markers):
        return Matter(name, dur, markers)

    def _print(self):
        for key, matter in self._matters.items():
            matter_name = key
            matter_dur = matter.dur
            matter_markers = matter.markers # dict of objects
            print('=======================================')
            print('Name:\t\t{}'.format(matter_name))
            print('Dur:\t\t{:.03f}'.format(matter_dur))
            print('\n\nMarkers:\n')
            for marker_key, marker in matter_markers.items():
                print(marker)
        print('=======================================')

    def __str__(self):
        self._print()
        return 'Print Done'