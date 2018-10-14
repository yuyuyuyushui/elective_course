import os, sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

from core import main

if __name__ == '__main__':
    main.run()