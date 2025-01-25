from getkey import getkey, keynames, keys
from rich import table
import gui

main_gui = gui.GUI_status()
gui.GUI_show(main_gui)

class Core():
    def OnKeyPressed(self, key):
        
        
        match key:
            case keys.ESC:
                exit()
            case keys.DOWN:
                if(main_gui.frame_set + main_gui.curY == len(main_gui.table) - 1):
                  return 
                if(main_gui.curY == 9):
                   main_gui.set_frame(main_gui.frame_set + 1)
                   gui.GUI_show(main_gui)
                   return
                main_gui.curY +=1
            case keys.UP:
                if(main_gui.frame_set + main_gui.curY == 0):
                    return
                if(main_gui.curY == 0):
                    main_gui.set_frame(main_gui.frame_set - 1)
                    gui.GUI_show(main_gui)
                    return
                main_gui.curY -=1
                gui.GUI_show(main_gui)
            case keys.RIGHT:
                if(main_gui.curX == 6):
                    return
                main_gui.curX += 1
            case keys.LEFT:
                if(main_gui.curX == 0):
                    return
                main_gui.curX -=1



        
        gui.GUI_show(main_gui)
