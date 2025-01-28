from getkey import getkey, keynames, keys
from rich import table
from datetime import datetime, timedelta
import data
import gui

main_gui = gui.GUI_status()
gui.GUI_show(main_gui)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def sh_list_editor():

    while True:
        for index, value in enumerate(main_gui.sh_list):
            print(f"{index + 1}. {value}")
        u_input = input("Для добавление школы введите название.\nДля Удаление введитете порядковый номер.\nДля выхода введите 0\n>>>")
        if is_int(u_input):
            if int(u_input) == 0:
                break
            main_gui.sh_list.pop(int(u_input) - 1)
        else:
            main_gui.sh_list.append(u_input)

    gui.data.Set_sh_list(main_gui.sh_list)

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
                main_gui.hint2 = main_gui.contextHint[main_gui.curX]
            case keys.LEFT:
                if(main_gui.curX == 0):
                    return
                main_gui.curX -=1
                main_gui.hint2 = main_gui.contextHint[main_gui.curX]
            case keys.ENTER:
                if(main_gui.curX == 1):
                    n = gui.input_text("Введите Фамилию >>>")
                    main_gui.table[main_gui.curY + main_gui.frame_set][1] = n
                    gui.data.Set_table(main_gui.table)
                if main_gui.curX == 2:
                    for index, value in enumerate(main_gui.sh_list):
                        print(f"{index + 1}. {value}")
                    u_input  = gui.input_text("Для вставки введите порядковый номер школы\n>>>")
                    main_gui.table[main_gui.frame_set + main_gui.curY][2] = main_gui.sh_list[(int(u_input) - 1)]
                    gui.data.Set_table(main_gui.table)
                if main_gui.curX == 6:
                    n = gui.input_text("Введите текст метки>>>")
                    main_gui.table[main_gui.frame_set + main_gui.curY][6] = n
                    gui.data.Set_table(main_gui.table)
            case 's'|'ы':
                sh_list_editor()
            case 'n'|'т':
                first_num = int(gui.input_text("Введите начальное число>>>"))
                start_pos = main_gui.frame_set + main_gui.curY
                end_pos = len(main_gui.table)
                for index in range(start_pos, end_pos):
                    main_gui.table[index][0] = str(first_num)
                    first_num += 1
                gui.data.Set_table(main_gui.table)
            case 't'|'е':
               f_start = gui.input_text("введите 6 чисел:часы, минуты и секуды для формирования времени начала отсчета>>>")
               add_time = gui.input_text("Введите прибавляемое время в секундах>>>")
               time_format = "%H%M%S"
               time_f_start = datetime.strptime(f_start, time_format)
               start_pos = main_gui.frame_set + main_gui.curY
               end_pos = len(main_gui.table)
               for index in range(start_pos,end_pos):
                   main_gui.table[index][3] = time_f_start.strftime("%H:%M:%S")
                   time_f_start += timedelta(seconds=int(add_time))
               gui.data.Set_table(main_gui.table)



        
        gui.GUI_show(main_gui)
