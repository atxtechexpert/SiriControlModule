import os

moduleName = "sleep" 
commandWords = ["sleep","computer"]
 
def execute(command):    
    os.system(r"C:\Windows\System32\psshutdown.exe -d -t 0")