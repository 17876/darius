class Timecode:
    def __init__(self, timecode, fps=None):
        self._timecode = timecode # string hh:mm:ss.sss in hms-format, hh:mm:ss:fff with f at the end in smpte-format
        self._units = None
        self.units_extractor()
        if fps: # float
            self._fps = fps
        self.format()
        self._seconds = None
        self.seconds()

    @property
    def timecode(self):
        return self._timecode

    @timecode.setter
    def timecode(self, val):
        self._timecode = val
        self.units_extractor()
        self.format()
        self.seconds()

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, val):
        self._fps = val
        self.seconds()

    def units_extractor(self):
        if self._timecode[-1] == 'f':
            self._units = 'smpte'
        else:
            self._units = 'hms'

    def format(self):
        if self._units == 'smpte':
            tc_no_f = ''
            for i in self._timecode:
                if i != 'f':
                    tc_no_f = tc_no_f + i
            tc_split = tc_no_f.split(':')
            tc_len = len(tc_split)
            if tc_len < 4:  # check if it's in format hhmmssff
                for i in range(4 - tc_len):
                    tc_split.insert(0, 0)
            hh = int(tc_split[0])
            mm = int(tc_split[1])
            ss = int(tc_split[2])
            ff = int(tc_split[3])
            self._timecode = '{:02d}:{:02d}:{:02d}:{:02d}'.format(hh, mm, ss, ff)
        else:
            tc_split = self._timecode.split(':')
            tc_len = len(tc_split)
            if tc_len < 3:  # check if it's in format hms
                for i in range(3 - tc_len):
                    tc_split.insert(0, 0)
            hh = int(tc_split[0])
            mm = int(tc_split[1])
            ss = float(tc_split[2])
            self._timecode = '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)

    def seconds(self):
        self.format()
        tc_split = [float(i) for i in self._timecode.split(':')]
        if self._units == 'smpte': # smpte -> sec
            hh = tc_split[0]
            mm = tc_split[1]
            ss = tc_split[2]
            ff = tc_split[3]
            secs = round(((hh * 60) + mm) * 60 + ss + ff * (1/self._fps), 3)
        else: # hms -> secs
            hh = tc_split[0]
            mm = tc_split[1]
            ss = tc_split[2]
            secs = round(((hh * 60) + mm) * 60 + ss, 3)
        self._seconds = secs
        return

    def mutate(self): # 3839.5
        if self._units == 'smpte':  # smpte -> hms
            hh = int(self._seconds / 3600) # 1
            secs_without_whole_hours = self._seconds % 3600 # 839.5
            mm = int(secs_without_whole_hours/60) # 13
            secs_without_whole_hours_minutes = secs_without_whole_hours%60 # 59.5
            ss = secs_without_whole_hours_minutes
            self.timecode = '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)
        else: # hms -> smpte (hhmmssff)
            hh = int(self._seconds / 3600)  # 1
            secs_without_whole_hours = self._seconds % 3600  # 839.5
            mm = int(secs_without_whole_hours / 60)  # 13
            secs_without_whole_hours_minutes = secs_without_whole_hours % 60  # 59.5
            ss = int(secs_without_whole_hours_minutes) # 59
            ff = round((secs_without_whole_hours_minutes - ss) * self._fps)
            self.timecode = '{:02d}:{:02d}:{:02d}:{:02d}f'.format(hh, mm, ss, ff)

