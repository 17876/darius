class Tc:
    def __init__(self, hmsf, fr=None):
        self._hmsf = hmsf # string hh:mm:ss.sss in hms-format, hh:mm:ss:fff with f at the end in smpte-format
        self._units = None
        self.units_extractor()
        if fr: # float
            self._fr = fr
        self.format()
        self._seconds = None
        self._frames = None
        self.call_seconds()
        self.call_frames()

    @property
    def hmsf(self):
        return self._hmsf

    @hmsf.setter
    def hmsf(self, val):
        self._hmsf = val
        self.units_extractor()
        self.format()
        self.call_seconds()
        self.call_frames()

    @property
    def fr(self):
        return self._fr

    @fr.setter
    def fr(self, val):
        self._fr = val
        self.call_seconds()
        self.call_frames()

    def units_extractor(self): # checks if the hmsf string has f at the end - then smpte
        if self._hmsf[-1] == 'f':
            self._units = 'smpte'
        else:
            self._units = 'hms'
        return self._units

    def format(self): # formats hmsf to hh:mm:ss:ff or hh:mm:ss.ms
        if self._units == 'smpte':
            hmsf_no_f = ''
            for i in self._hmsf:
                if i != 'f':
                    hmsf_no_f = hmsf_no_f + i
            hmsf_split = hmsf_no_f.split(':')
            hmsf_len = len(hmsf_split)
            if hmsf_len < 4:  # checck if i.e. hh and/or mm missing, just for example ss:ff there.
                for i in range(4 - hmsf_len):
                    hmsf_split.insert(0, 0)
            hh = int(hmsf_split[0])
            mm = int(hmsf_split[1])
            ss = int(hmsf_split[2])
            ff = int(hmsf_split[3])
            self._hmsf = '{:02d}:{:02d}:{:02d}:{:02d}'.format(hh, mm, ss, ff)
        else:
            hmsf_split = self._hmsf.split(':')
            hmsf_len = len(hmsf_split)
            if hmsf_len < 3:  # checck if i.e. hh and/or mm missing
                for i in range(3 - hmsf_len):
                    hmsf_split.insert(0, 0)
            hh = int(hmsf_split[0])
            mm = int(hmsf_split[1])
            ss = float(hmsf_split[2])
            self._hmsf = '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)

    def call_seconds(self): # calculates and outputs seconds
        self.format()
        hmsf_split = [float(i) for i in self._hmsf.split(':')]
        if self._units == 'smpte': # smpte -> sec
            hh = hmsf_split[0]
            mm = hmsf_split[1]
            ss = hmsf_split[2]
            ff = hmsf_split[3]
            secs = round(((hh * 60) + mm) * 60 + ss + ff * (1/self._fr), 3)
        else: # hms -> secs
            hh = hmsf_split[0]
            mm = hmsf_split[1]
            ss = hmsf_split[2]
            secs = round(((hh * 60) + mm) * 60 + ss, 3)
        self._seconds = secs
        return self._seconds

    def call_frames(self): # calculates and outputs frames
        self.format()
        hmsf_split = [float(i) for i in self._hmsf.split(':')]
        if self._units == 'smpte': # smpte -> frames
            hh = hmsf_split[0]
            mm = hmsf_split[1]
            ss = hmsf_split[2]
            ff = hmsf_split[3]
            frames = ((hh * 3600) + (mm * 60) + ss) * self._fr + ff
            self._frames = frames
            return self._frames

    def mutate(self, fr=None): # 3839.5
        if self._units == 'smpte':  # smpte -> hms
            hh = int(self._seconds / 3600) # 1
            secs_without_whole_hours = self._seconds % 3600 # 839.5
            mm = int(secs_without_whole_hours/60) # 13
            secs_without_whole_hours_minutes = secs_without_whole_hours%60 # 59.5
            ss = secs_without_whole_hours_minutes
            self.hmsf = '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)
        else: # hms -> smpte (hhmmssff)
            self._fr = fr
            hh = int(self._seconds / 3600)  # 1
            secs_without_whole_hours = self._seconds % 3600  # 839.5
            mm = int(secs_without_whole_hours / 60)  # 13
            secs_without_whole_hours_minutes = secs_without_whole_hours % 60  # 59.5
            ss = int(secs_without_whole_hours_minutes) # 59
            ff = round((secs_without_whole_hours_minutes - ss) * self._fr)
            self.hmsf = '{:02d}:{:02d}:{:02d}:{:02d}f'.format(hh, mm, ss, ff)

    def __str__(self):
        if self._units == 'smpte':
            line = '{:s}, fr: {:.02f} fps'.format(self._hmsf, self._fr)
        else:
            line = '{:s}'.format(self._hmsf)
        return line

