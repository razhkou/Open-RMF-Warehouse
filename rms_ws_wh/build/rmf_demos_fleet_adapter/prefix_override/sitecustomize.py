import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/daniele/rms_ws_wh/install/rmf_demos_fleet_adapter'
