import os
from   pathlib import Path

def init_sensor():
    if not os.system('modprobe w1-gpio' ) == 0:
        return False
    if not os.system('modprobe w1-therm') == 0:
        return False
    return True

def find_w1_slave_path():
    w1_device_path = Path('/sys/bus/w1/devices')
    w1_slave_path  = [i for i in w1_device_path.iterdir() if i.name.startswith('28-')][0] / 'w1_slave'
    if not w1_slave_path.exists():
        return None
    return str(w1_slave_path)

def convert_c_to_f(temp_c):
    return (temp_c * 9.0/5.0) + 32.0
def convert_f_to_c(temp_f):
    return (temp_f - 32.0) * 5.0/9.0

class DS18B20Sensor:
    def __init__(self, w1_slave_path=None):
        if w1_slave_path:
            self.w1_slave_path = w1_slave_path
        else:
            self.w1_slave_path = find_w1_slave_path()
            assert self.w1_slave_path
    def _read(self):
        with open(self.w1_slave_path, 'r') as f:
            return f.read()
    def read_c(self):
        output = self._read()
        t_eq_pos  = output.find('t=')
        if t_eq_pos == -1:
            return None
        return int(output[t_eq_pos+2:].strip()) / 1000.0
    def read_f(self):
        temp_c = self.read_c()
        if not temp_c:
            return None
        return convert_c_to_f(temp_c)

class Limits:
    def __init__(self, min, max, units='c'):
        assert type(units) == str
        units = units.strip().lower()
        if units == 'c':
            self.min_c = min
            self.max_c = max
        elif units == 'f':
            self.min_c = convert_f_to_c(min)
            self.max_c = convert_f_to_c(max)
        else:
            raise ValueError(f'Do not understand temperature units: {units}')
    def is_acceptable(self, temp, units='c'):
        units = units.strip().lower()
        if units == 'c':
            pass
        elif units == 'f':
            temp = convert_f_to_c(temp)
        else:
            raise ValueError(f'Do not understand temperature units: {units}')
        return temp <= self.max_c and temp >= self.min_c
