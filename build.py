import os
script="""import sys

from cx_Freeze import setup, Executable
includes = ["re","atexit"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "JPhoto Safe Light",
        version = "2.0",
        description = "Interactive 2D filters",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable("PhotoSafeLight.py", base = base,icon="icon.ico")])"""

file=open("temp.py","wt")
file.write(script)
file.close()
os.system("python temp.py build")
os.remove("temp.py")
input("\nHECHO")