import os

moduleName = "restart" 
commandWords = ["restart","computer"]
 
def execute(command):
    os.system("shutdown /r /t 1")
