import os,shutil
buildDir="build\\exe.win32-3.4\\"
buildZip="JPhotoSafeLight"
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
print("Copying extra files")
shutil.copy("op.py",buildDir+"op.py")
shutil.copy("DefaultImage.jpg",buildDir+"DefaultImage.jpg")
print("Creating Zip")
shutil.make_archive(buildZip, 'zip', buildDir)
print("\nDONE!")