import sys
import os


CURR_DIR = os.path.dirname(os.path.abspath('/home/ghazal/Documents/ProjFinalDB/tables/Customer.py'))
print(CURR_DIR)
sys.path.append(CURR_DIR)
for path in sys.path:
    print(path)