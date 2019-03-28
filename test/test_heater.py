from   lib.heater import Heater
from   lib.test.heater import bins_path, SmartPlug
import unittest

class TestHeater(unittest.TestCase):
    def test_toggle(self):
        smart_plug = SmartPlug()
        smart_plug.reset()

        heater = Heater(bins_path)
        heater.on()
        self.assertEqual(smart_plug.led,    'on')
        self.assertEqual(smart_plug.output, 'on')

        heater.off()
        self.assertEqual(smart_plug.led,    'off')
        self.assertEqual(smart_plug.output, 'off')

        heater.off()
        self.assertEqual(smart_plug.led,    'off')
        self.assertEqual(smart_plug.output, 'off')

        heater.on()
        self.assertEqual(smart_plug.led,    'on')
        self.assertEqual(smart_plug.output, 'on')

        heater.on()
        self.assertEqual(smart_plug.led,    'on')
        self.assertEqual(smart_plug.output, 'on')
