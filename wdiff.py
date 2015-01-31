#!/usr/bin/python

import sys
import os

os.system('wdiff -s3 "%s" "%s"' % (sys.argv[2], sys.argv[5]))
