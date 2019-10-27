#You can import any modules required here 
import os

moduleName = "turnoff" 
commandWords = ["turn","off","computer"]
 
def execute(command):
    os.system("shutdown /s /t 1")
