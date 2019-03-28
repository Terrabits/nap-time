from   ddt             import ddt, data
from   lib.temperature import DS18B20Sensor
from   pathlib         import Path
import unittest

root_path     = Path(__file__).parent
fixtures_path = root_path / 'fixtures'
w1_slave_path = fixtures_path / 'w1_slave'
def fixture_path(filename):
    return str(w1_slave_path / filename)

@ddt
class TestDS18B20Sensor(unittest.TestCase):
    @data({'w1_slave_path': fixture_path('t_00000'),  'temp_c':   0.0},
          {'w1_slave_path': fixture_path('t_21500'),  'temp_c':  21.5},
          {'w1_slave_path': fixture_path('t_100000'), 'temp_c': 100.0})
    def test_read_c(self, data):
        w1_slave_path = data['w1_slave_path']
        temp_c        = data['temp_c']
        sensor = DS18B20Sensor(w1_slave_path)
        self.assertEqual(sensor.read_c(), temp_c)

    @data({'w1_slave_path': fixture_path('t_00000'),  'temp_f':  32.0},
          {'w1_slave_path': fixture_path('t_21500'),  'temp_f':  70.7},
          {'w1_slave_path': fixture_path('t_100000'), 'temp_f': 212.0})
    def test_read_f(self, data):
        w1_slave_path = data['w1_slave_path']
        temp_f        = data['temp_f']
        sensor = DS18B20Sensor(w1_slave_path)
        self.assertEqual(sensor.read_f(), temp_f)
