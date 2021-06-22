from tc import Tc

def range_scale(x, x1, x2, y1, y2):
    return (y2-y1)*(x - x1)/(x2 - x1) + y1

def secs_to_tc(secs, units, fr=None):
    if units == 'hms':
        hh = int(secs / 3600)
        secs_without_whole_hours = secs % 3600
        mm = int(secs_without_whole_hours / 60)
        secs_without_whole_hours_minutes = secs_without_whole_hours % 60
        ss = secs_without_whole_hours_minutes
        tc =  '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)
    else:
        hh = int(secs / 3600)  # 1
        secs_without_whole_hours = secs % 3600
        mm = int(secs_without_whole_hours / 60)
        secs_without_whole_hours_minutes = secs_without_whole_hours % 60
        ss = int(secs_without_whole_hours_minutes)
        ff = round((secs_without_whole_hours_minutes - ss) * fr)
        tc =  '{:02d}:{:02d}:{:02d}:{:02d}f'.format(hh, mm, ss, ff)
    return tc

def add_tc(tc1, tc2, fr=None):
    sec1 = tc1._seconds
    sec2 = tc2._seconds
    output_sec = sec1 + sec2
    if fr: # smpte
        hmsf = secs_to_tc(output_sec, 'smpte', fr)
        output = Tc(hmsf, fr)
    else:
        hmsf = secs_to_tc(output_sec, 'hms')
        output = Tc(hmsf)
    return output

def subtr_tc(tc1, tc2, fr=None):
    sec1 = tc1._seconds
    sec2 = tc2._seconds
    output_sec = sec1 - sec2
    if fr: # smpte
        hmsf = secs_to_tc(output_sec, 'smpte', fr)
        output = Tc(hmsf, fr)
    else:
        hmsf = secs_to_tc(output_sec, 'hms')
        output = Tc(hmsf)
    return output