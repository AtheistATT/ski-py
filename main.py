from getkey import getkey, keynames, keys
import gui
import core
from rich import console

console = console.Console()
core = core.Core()

while True:
    key = getkey() 
    core.OnKeyPressed(key)
