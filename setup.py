import py2exe, sys, os
from distutils.core import setup

sys.argv.append("py2exe")
setup(
    options = {'py2exe':{'bundle_files':1}},
    windows = [{'script':"Persistence.py"}],
    zipfile = None,
)
