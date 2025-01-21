#from getkey import getkey, keynames, keys
##from rich import console
#console = console.Console()
#while True:
#    key = getkey() 
#    console.print(f"[red]{key}")
import gui

status_gui = gui.GUI_status()
status_gui.curY = 5
status_gui.curX = 1
status_gui.set_frame(0)
gui.GUI_show(status_gui)
input()
