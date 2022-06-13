from setuptools import setup
import os
import platform
from typing import Final

USER_PLATFORM: Final = platform.system()

setup()
os.system("pip install pyinstaller")

print("Download concluded!")

if USER_PLATFORM == "Windows":
    os.system("pyinstaller main.py")
elif USER_PLATFORM == "Linux":
    os.system('pyinstaller -D -F -n Universe_Simulator -c "main.py"')

