import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ojasvi/Desktop/eYRC2024LogisticCobot/install/ur5_control'
