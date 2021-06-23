import json
from tc import Tc

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
    def __init__(self, name, filepath, filename, filedur, _in, _out, markers=None):
        self.name = name
        self.filepath = filepath
        self.filename = filename
        self.filedur = filedur
        self._in = _in # timecode, where to look in the file
        self._out = _out # timecode, where to look in the file
        self.markers = markers # dict

class VideoMatter(Matter):
    def __init__(self, name, filepath, filename, filedur, _in, _out, fr, markers=None):
        super().__init__(name, filepath, filename, filedur, _in, _out, markers)
        self._fr = fr

    def _print(self):
        print('Video Matter: {}'.format(self.name))
        print('Filepath: {}'.format(self.filepath))
        print('Filename: {}'.format(self.filename))
        print('Filedur: {}'.format(self.filedur))
        print('In: {}'.format(self._in))
        print('Out: {}'.format(self._out))
        print('Frame Rate: {}'.format(self._fr))
        if self.markers:
            print('\nMarkers:')
            for key, val in self.markers.items():
                print(val)

    def __str__(self):
        self._print()
        return 'Matter Print Done'

class AudioMatter(Matter):
    def __init__(self, name, filepath, filename, filedur, _in, _out, markers=None):
        super().__init__(name, filepath, filename, filedur, _in, _out, markers)

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
            json_matter_filepath = json_matter['filepath']
            json_matter_filename = json_matter['filename']
            json_matter_filedur = json_matter['filedur']
            json_matter_in = json_matter['in']
            json_matter_out = json_matter['out']
            json_markers = json_matter['markers']

            matter_filepath = json_matter_filepath
            matter_filename = json_matter_filename

            if json_matter_type == 'v':
                json_matter_fr = json_matter['fr']
                matter_in = Tc(json_matter_in, json_matter_fr)
                matter_out = Tc(json_matter_out, json_matter_fr)
                matter_filedur = Tc(json_matter_filedur, json_matter_fr)

                # markers
                matter_markers = {}
                for marker_key, json_marker in json_markers.items():
                    json_marker_start = json_marker['start']
                    json_marker_end = json_marker['end']
                    marker_start = Tc(json_marker_start, json_matter_fr)
                    marker_end = Tc(json_marker_end, json_matter_fr)
                    matter_markers[marker_key] = Marker(marker_key, marker_start, marker_end)

                cur_matter = self._create_video_matter(matter_name, matter_filepath, matter_filename,
                                                       matter_filedur, matter_in, matter_out,
                                                       json_matter_fr, matter_markers)

            else:
                matter_in = Tc(json_matter_in)
                matter_out = Tc(json_matter_out)
                matter_filedur = Tc(json_matter_filedur)

                # markers
                matter_markers = {}
                for marker_key, json_marker in json_markers.items():
                    json_marker_start = json_marker['start']
                    json_marker_end = json_marker['end']
                    marker_start = Tc(json_marker_start)
                    marker_end = Tc(json_marker_end)
                    matter_markers[marker_key] = Marker(marker_key, marker_start, marker_end)

                cur_matter = self._create_audio_matter(matter_name, matter_filepath, matter_filename,
                                                       matter_filedur, matter_in, matter_out,
                                                       matter_markers)
            self._matters[matter_name] = cur_matter

    def _create_video_matter(self, name, matter_filepath, matter_filename, matter_filedur, matter_in,
                             matter_out, fr, markers):
            return VideoMatter(name, matter_filepath, matter_filename, matter_filedur, matter_in,
                               matter_out, fr, markers)

    def _create_audio_matter(self, name, matter_filepath, matter_filename, matter_filedur, matter_in,
                             matter_out, markers):
        return VideoMatter(name, matter_filepath, matter_filename,
                           matter_filedur, matter_in, matter_out, markers)

    def _print(self):
        print('=======================================')
        print('Matter Database: {:s}'.format(self._database_name))
        for key, matter in self._matters.items():
            print(matter)

    def __str__(self):
        self._print()
        return 'Matter Database Print Done'