from timecode import Timecode

# Dash is a class for time-based objects
class Dash:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start # timecode
        self.end = end # timecode

    def __str__(self):
        line = 'Name: {:s}, Start: {:s}, End: {:s}'.format(self.name, self.start.__str__(), self.end.__str__())
        return line

class Layer:
    def __init__(self):
        self._dashes = {}

    def add_dash(self, *args):
        for arg in args:
            name = arg.name
            self._dashes[name] = arg

    def _print(self):
        for key, dash in self._dashes.items():
            dash_name = key
            dash_start = dash.start # timecode
            dash_end = dash.end # timecode
            print('=======================================')
            print('Dash Name:\t\t{}'.format(dash_name))
            print('Dash Start:\t\t{:s}'.format(dash_start.__str__()))
            print('Dash Dur:\t\t{:s}'.format(dash_end.__str__()))
        print('=======================================')

    def __str__(self):
        self._print()
        return 'Print Done'