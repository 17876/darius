# from darius.tc import Tc

def range_scale(x, x1, x2, y1, y2):
    return (y2-y1)*(x - x1)/(x2 - x1) + y1

def secs_to_tc(secs, units, fr=None):
    if units == 'hms':
        hh = int(secs / 3600)
        secs_without_whole_hours = secs % 3600
        mm = int(secs_without_whole_hours / 60)
        secs_without_whole_hours_minutes = secs_without_whole_hours % 60
        ss = secs_without_whole_hours_minutes
        tc = '{:02d}:{:02d}:{:.03f}'.format(hh, mm, ss)
    else:
        hh = int(secs / 3600)  # 1
        secs_without_whole_hours = secs % 3600
        mm = int(secs_without_whole_hours / 60)
        secs_without_whole_hours_minutes = secs_without_whole_hours % 60
        ss = int(secs_without_whole_hours_minutes)
        ff = round((secs_without_whole_hours_minutes - ss) * fr)
        tc = '{:02d}:{:02d}:{:02d}:{:02d}'.format(hh, mm, ss, ff)
    return tc