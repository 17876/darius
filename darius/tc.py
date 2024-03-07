from darius.util import secs_to_tc

class Tc:
    def __init__(self, timecode, units, fr=None):
        # timecode – a string hh:mm:ss.sss in hms-format or hh:mm:ss:ff in smpte-format
        self._units = units # hms or smpte
        self._fr = fr
        self._timecode = self._calc_timecode(timecode)

    @property
    def timecode(self):
        return self._timecode

    @timecode.setter
    def timecode(self, timecode):
        self._timecode = self._calc_timecode(timecode)

    # formatting entered time code according to entered units and potentially frame rate
    def _calc_timecode(self, timecode):
        if self.units == 'smpte':
            timecode_split = timecode.split(':')
            timecode_len = len(timecode_split)
            if timecode_len < 4:  # checck if i.e. hh and/or mm missing, just for example ss:ff there.
                for i in range(4 - timecode_len):
                    timecode_split.insert(0, 0)
            hh = int(timecode_split[0])
            mm = int(timecode_split[1])
            ss = int(timecode_split[2])
            ff = int(timecode_split[3])
            return '{:02d}:{:02d}:{:02d}:{:02d}'.format(hh, mm, ss, ff)
        elif self.units == 'hms':
            timecode_split = timecode.split(':')
            timecode_len = len(timecode_split)
            if timecode_len < 3:  # checck if i.e. hh and/or mm missing
                for i in range(3 - timecode_len):
                    timecode_split.insert(0, 0)
            hh = int(timecode_split[0])
            mm = int(timecode_split[1])
            ss = float(timecode_split[2])
            return '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, val):
        self._units = val

    @property
    def fr(self):
        return self._fr

    @fr.setter
    def fr(self, val):
        self._fr = val

    @property
    def seconds(self): # calculates seconds
        timecode_split = [float(i) for i in self._timecode.split(':')]
        if self.units == 'smpte': # smpte -> sec
            hh = timecode_split[0]
            mm = timecode_split[1]
            ss = timecode_split[2]
            ff = timecode_split[3]
            secs = round(((hh * 60) + mm) * 60 + ss + ff * (1/self._fr), 3)
        else: # hms -> secs
            hh = timecode_split[0]
            mm = timecode_split[1]
            ss = timecode_split[2]
            secs = round(((hh * 60) + mm) * 60 + ss, 3)
        return secs

    @property
    def frames(self): # calculates and outputs frames
        timecode_split = [float(i) for i in self._timecode.split(':')]
        if self.units == 'smpte': # smpte -> frames
            hh = timecode_split[0]
            mm = timecode_split[1]
            ss = timecode_split[2]
            ff = timecode_split[3]
            frames_ = ((hh * 3600) + (mm * 60) + ss) * self.fr + ff
            return frames_

    def __eq__(self, other):
        if self.seconds == other.seconds and self.fr == other.fr and self.units == other.units:
            return True
        else:
            return False

    def __add__(self, other):
        sec1 = self.seconds
        sec2 = other.seconds
        output_sec = sec1 + sec2
        if self.units == other.units and self.fr == other.fr:
            hmsf = secs_to_tc(output_sec, 'smpte', self.fr)
            output = Tc(hmsf, 'smpte', self.fr)
            return output
        else:
            print('Cannot add')

    def __str__(self):
        if self.units == 'smpte':
            line = '{:s}, fr: {:.02f} fps'.format(self.timecode, self.fr)
        else:
            line = '{:s}'.format(self.hmsf)
        return line
