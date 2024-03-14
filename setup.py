# import pyinstaller
# import sys
# import os
# base= None

# if sys.platform=='win32':
#     base="Win32GUI"

# os.environ['TCL_LIBRARY']=r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
# os.environ['TK_LIBRARY']=r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

# executables=[pyinstaller.Executable("project.py",base=base,icon="icon.ico")]

# pyinstaller.setup(
#     name="Text Editor",
#     options={"build_exe":{"package":["tkinter","os"],"include_files":["icon.ICO",'tc186t.dll','tk86t.dll','icons2']}},
#     verson='0.01',
#     discription="Tkinter Application",
#     executables=executables

# )
# import cx_Freeze
# import sys
# import os

# base = None

# if sys.platform == 'win32':
#     base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

# executables = [cx_Freeze.executable("project.py", base=None, icon="icon.ico")]

# cx.Freeze.setup(
#     name="Text Editor",
#     options={
#         "build_exe": {
# +            "packages": ["tkinter", "os"],
#             "include_files": ["icon.ico", 'tc186t.dll', 'tk86t.dll', 'icons2']
#         }
#     },
#     version='0.01',
#     description="Tkinter Application",
#     executables = executables
# )
# import sys
# import os
# from cx_Freeze import setup, Executable

# base = None

# if sys.platform == 'win32':
#     base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r"D:\python\project.py\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"D:\python\project.py\tcl\tk8.6"

# executables = [Executable("project.py", base=base, icon="icon.ico")]

# setup(
#     name="Text Editor",
#     options={
#         "build_exe": {
#             "packages": ["tkinter", "os"],
#             "include_files": ["icon.ico", 'tcl86t.dll', 'tk86t.dll', 'icons2']
#         }
#     },
#     version='0.01',
#     description="Tkinter Application",
#     executables=executables
# )
import sys
import os
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Anubhav\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [Executable("project.py", base=base, icon="icon.ico")]

setup(
    name="Text Editor",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": ["icon.ico", 'tcl86t.dll', 'tk86t.dll', 'icons2']   #'tc186t.dll', 'tk86t.dll',
        }
    },
    version='0.01',
    description="Tkinter Application",
    executables=executables
)
