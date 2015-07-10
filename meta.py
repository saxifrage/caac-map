#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals

from subprocess import PIPE, Popen

ntries = 10000
for i in range(ntries):
    print("\rTries: {:,} / {:,} ({:.1f}%)".format(i, ntries, i / ntries), end='')
    p = Popen('python genmap.py svg 1'.split(), stdout=open('www/map.svg', 'w+'), stderr=PIPE)
    err = p.stderr.read()
    if 'Traceback' not in err:
        if 'Remaining area: 0' in err:
            print("\nFound one!")
            print(err)
            break
