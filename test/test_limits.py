from   ddt             import ddt, data
from   lib.temperature import Limits
import unittest

@ddt
class TestLimits(unittest.TestCase):
    @data({'max': 100, 'min':  0, 'limit units': 'c', 'temp':   0, 'temp units': 'c', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':   1, 'temp units': 'c', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  50, 'temp units': 'c', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  99, 'temp units': 'c', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp': 100, 'temp units': 'c', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  -1, 'temp units': 'c', 'is acceptable': False},
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp': 101, 'temp units': 'c', 'is acceptable': False},
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  32, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  72, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp': 212, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  31, 'temp units': 'f', 'is acceptable': False},
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  32, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':  72, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp': 212, 'temp units': 'f', 'is acceptable': True },
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp': 213, 'temp units': 'f', 'is acceptable': False},
          {'max': 100, 'min':  0, 'limit units': 'c', 'temp':   0, 'temp units': 'c', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':   1, 'temp units': 'c', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  50, 'temp units': 'c', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  99, 'temp units': 'c', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp': 100, 'temp units': 'c', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  -1, 'temp units': 'c', 'is acceptable': False},
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp': 101, 'temp units': 'c', 'is acceptable': False},
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  32, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  72, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp': 212, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  31, 'temp units': 'f', 'is acceptable': False},
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  32, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp':  72, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp': 212, 'temp units': 'f', 'is acceptable': True },
          {'max': 212, 'min': 32, 'limit units': 'f', 'temp': 213, 'temp units': 'f', 'is acceptable': False})
    def test_limits(self, data):
        min           = data['min']
        max           = data['max']
        limit_units   = data['limit units']
        temp          = data['temp']
        temp_units    = data['temp units']
        is_acceptable = data['is acceptable']
        limits        = Limits(min, max, limit_units)
        self.assertEqual(limits.is_acceptable(temp, temp_units), is_acceptable)
