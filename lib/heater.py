from   pathlib import Path
import subprocess

bins_path = Path(__file__).parent / 'bin' / 'smart_plug'

class Heater(object):
    def __init__(self, bins_path=bins_path):
        self.bins_path = bins_path
    def on(self):
        return self._send('outlet-on')  and self._send('led-on')
    def off(self):
        return self._send('outlet-off') and self._send('led-off')
    def _send(self, action):
        action_bin = str(self.bins_path / action)
        process    = subprocess.Popen(action_bin)
        try:
            return process.wait(0.5) == 0
        except subprocess.TimeoutExpired:
            return False
