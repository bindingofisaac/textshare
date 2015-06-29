import sys, os
import textshare

def main():
    print textshare.readfile(os.path.abspath('a.py'))
    print textshare.check_install()
    print sys.argv
