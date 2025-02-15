"""
Этот модуль предназначен для вывода псевдографики в терминале для программы ski-py.
"""
from rich import console, table
import pdb
from rich.console import Console
from rich.table import Table
import data

class GUI_status:
    """
        Класс предназначен для изменения состояния интерфейса. 
        При измении полей для отображения экземпляр этого класса передается функции GUI_show
    """
    title = "Главный протокол" #Заголовок таблицы
    sh_list = [] #Список школ
    table = [] #Таблица содержащая все данные
    frame_table = []#Часть таблицы, начинающаяся с переменной frame_set и величиной 10 элементов
    frame_set = 0
    curX = 0 #Позиция указателя
    curY = 0
    hint1 = "[green]A[white]: Создать запись.\n[green]D[white]:удалить запись.\n[green]G[white]: создать протокол"
    hint2 = ""
    buf = ""
    time_buf = "00000000"
    contextHint = [
            "[green]N[white]:начать нумерацию с этой точки",
            "[green]Enter[white]: для редактирования фамилий.",
     "[green]S[white]:Редактор списка школ.\n[green]Enter[white]:добавить школу из списка.",
     "[green]T[white]:начать просчет стартового времени с текущей позиции.",
     "[green]Enter[white]:ввести время финиша.",
     "[green]Enter[white]:Просчитать чистое время",
     "[green]Enter[white]:редактировать метку\n[green]C[white]:скопировать метку в буфер\n[green]V[white]:вставить метку в буфер"
            ]
    def __init__(self) -> None:
        self.sh_list = data.Get_sh_list()
        self.table = data.Get_table()
        self.set_frame()
        self.hint2 = self.contextHint[0]
        
    
    def set_frame(self,frame = 0):
        """
        Метод смещает начало списка к указанной позиции.

        """
        self.frame_set = frame
        self.frame_table = []
        for i in range(frame, frame + 10):
            if(i > (len(self.table) - 1)):
                break
            self.frame_table.append(self.table[i])


console = Console()

def GUI_show(status: GUI_status,):
    """
    Функция отображает интерфейс программы в зависимости от объекта переменной GUI_status
    """
    console.clear()
    status.set_frame(status.frame_set)
    table = Table(title=status.title)


    table.add_column("Номер")
    table.add_column("Фамилия")
    table.add_column("Школа")
    table.add_column("Время старта")
    table.add_column("Время финиша")
    table.add_column("Чистое время")
    table.add_column("Метка")

    
    for j, v in enumerate(status.frame_table):
        list = []
        temp = ""
        for i, x in enumerate(v):
            temp = "[white on black]"
            if(j == status.curY):
                if i == status.curX:
                    temp = "[black on white]"
                else:
                    temp = "[black on light_green]"
            list.append(temp + x)

        table.add_row(list[0], list[1],list[2],list[3],list[4],list[5],list[6])

    console.print(status.hint1)
    console.print(table)
    console.print(status.hint2)
    
def input_text(text):
    return console.input("[green]" + text)


