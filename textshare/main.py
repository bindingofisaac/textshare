from __future__ import with_statement

def readfile(path):
    with open(path) as f:
        s = f.read()
    return s
