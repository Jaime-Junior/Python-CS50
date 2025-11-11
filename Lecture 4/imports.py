#Run with "python say.py NAME"

import sys

from double_underscore import goodbye, hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

if len(sys.argv) == 2:
    goodbye(sys.argv[1])