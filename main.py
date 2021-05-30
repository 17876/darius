from matter import MatterDatabase

# Dash is a class for time-based objects
class Dash:
    def __init__(self, start, dur):
        self.start = start
        self.dur = dur




db = MatterDatabase('materia.json')
print(db._matters['otrivok_iz_filma'].subdiv)














'''
class TestClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


t = TestClass(1)
print(t._x)

print('setting attr to 2')
t._x = 2

print('printing attr')
print(t._x)

print('printing prop')
print(t.x)

print('setting prop to 3')
t.x = 3
print('printing prop')
print(t.x)
print('printing attr')
print(t._x)

'''





