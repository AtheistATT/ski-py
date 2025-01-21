#from getkey import getkey, keynames, keys
##from rich import console
#console = console.Console()
#while True:
#    key = getkey() 
#    console.print(f"[red]{key}")
import gui

status_gui = gui.GUI_status()
gui.GUI_show(status_gui)
input()
