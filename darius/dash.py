# Dash is a class for time-based objects
import json
from darius.util import object_to_dict


class Container:
    def __init__(self, name=None, data=None):
        self.name = name
        if data:
            self.data = data
        else:
            self.data = []

    def __getitem__(self, index):
        if isinstance(index, (int, float)):
            return self.data[index]

        elif isinstance(index, str):
            output = []
            for item in self.data:
                if hasattr(item, 'name'):
                    if item.name == index:
                        output.append(item)
            if len(output) == 1:
                return output[0]
            else:
                return output

    def append(self, item):
        self.data.append(item)

    def __str__(self):
        return json.dumps(object_to_dict(self), indent=4)


class Dash:
    def __init__(self, name, start, end, content=None):
        self.name = name
        self._start = start # timecode in layer
        self._end = end # timecode in layer
        self._dur = self._end - self._start # duration
        self.content = content  # matter

    @property
    def dur(self):
        return self._dur

    @dur.setter
    def dur(self, val):
        self._dur = val
        self._end = self._start + val

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, val):
        self._start = val
        self._dur = self._end - self._start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, val):
        self._end = val
        self._dur = self._end - self._start

    def __str__(self):
        return json.dumps(object_to_dict(self), indent=4)


class Layer:
    def __init__(self, name, dashes = None):
        self.name = name
        if dashes:
            self._dashes = dashes
        else:
            self._dashes = []

    def add_dash(self, dash):
        self._dashes.append(dash)

    def __str__(self):
        return json.dumps(object_to_dict(self), indent=4)