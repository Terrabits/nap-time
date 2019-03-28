from   pathlib import Path
import subprocess

bins_path = Path(__file__).parent / 'bin' / 'smart_plug'

class SmartPlug(object):
    def __init__(self):
        project_root = Path(__file__).parent.parent.parent
        state_path   =  project_root / 'temp' / 'smart-plug' / 'state'
        self.led_filename    = str(state_path / 'led')
        self.output_filename = str(state_path / 'output')
    @property
    def led(self):
        with open(self.led_filename, 'r') as f:
            return f.read().strip()
    @property
    def output(self):
        with open(self.output_filename, 'r') as f:
            return f.read().strip()

    def reset(self):
        filename = str(bins_path / 'reset')
        process  = subprocess.Popen([filename])
        assert process.wait(1) == 0
