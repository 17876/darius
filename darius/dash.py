# Dash is a class for time-based objects
import json
from darius.util import object_to_dict

class Dash:
    def __init__(self, name, start, end, content=None):
        self.name = name
        self.start = start # timecode in layer
        self.end = end # timecode in layer
        self.content = content # matter

    # def _print(self):
    #     print('Dash Name: {}'.format(self.name))
    #     print('Dash Start: {}'.format(self.start))
    #     print('Dash End: {}'.format(self.end))
    #     print('Dash Content:')
    #     print(self.content)

    def __str__(self):
        return json.dumps(object_to_dict(self), indent=4)
        # self._print()
        # return 'Dash Print Done'

# class Layer:
#     def __init__(self, name):
#         self.name = name
#         self._dashes = {}
#
#     def add_dash(self, *args):
#         for arg in args:
#             name = arg.name
#             self._dashes[name] = arg
#
#     def _print(self):
#         print('=======================================')
#         print('Layer Name:\t\t{}'.format(self.name))
#         for key, dash in self._dashes.items():
#             dash_name = key
#             dash_start = dash.start # timecode
#             dash_end = dash.end # timecode
#             print('=======================================')
#             print('Dash Name:\t\t{}'.format(dash_name))
#             print('Dash Start:\t\t{:s}'.format(dash_start.__str__()))
#             print('Dash Dur:\t\t{:s}'.format(dash_end.__str__()))
#         print('=======================================')
#
#     def __str__(self):
#         self._print()
#         return 'Layer Print Done'