"""

Entry point of this utility.

Copyright (C) 2019, Team RedLogic.
All rights reserved.

"""

import os.path as path
import sys


# If this module is not installed: push it to sys.path.
parent = path.realpath(path.join(path.dirname(__file__), ".."))

if not parent.lower().endswith("lib/site-packages"):
	sys.path.insert(0, parent)


# Now, launch the CLI.
from rlgen.main import main

if __name__ == "__main__":
    main()
