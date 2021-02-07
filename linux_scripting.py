"""
    linux_scripting.py
    -------

    Esto es un module docstring
"""

__author__ = "Nicolás Roldán"

import subprocess

PL = subprocess.Popen(["ps", "-U", "0"], stdout=subprocess.PIPE).communicate()[0]
print(PL.decode("utf-8"))
