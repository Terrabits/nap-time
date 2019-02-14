from   ddt             import ddt, data
from   lib.temperature import DS18B20Sensor
from   pathlib         import Path
import unittest

root_path     = Path(__file__).parent
fixtures_path = root_path / 'fixtures'
w1_slave_path = fixtures_path / 'w1_slave'

@ddt
class TestDS18B20Sensor(unittest.TestCase):
    @data({'w1_slave_path': str(w1_slave_path / 't_21500'), 'temp_c': 21.5})
    def test_read_c(self, data):
        w1_slave_path = data['w1_slave_path']
        temp_c        = data['temp_c']
        sensor = DS18B20Sensor(w1_slave_path)
        self.assertEqual(sensor.read_c(), temp_c)
