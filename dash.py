# Dash is a class for time-based objects
class Dash:
    def __init__(self, name, start, dur):
        self.name = name
        self.start = start
        self.dur = dur

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
            dash_start = dash.start
            dash_dur = dash.dur
            print('=======================================')
            print('Dash Name:\t\t{}'.format(dash_name))
            print('Dash Start:\t\t{}'.format(dash_start))
            print('Dash Dur:\t\t{}'.format(dash_dur))
        print('=======================================')

    def __str__(self):
        self._print()
        return 'Print Done'