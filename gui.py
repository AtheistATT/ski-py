"""
Этот модуль предназначен для вывода псевдографики в терминале для программы ski-py.
"""
from rich import console, table
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
    hint1 = "Глобальный контекст"
    hint2 = ""
    contextHint = [
            "Хоткеи Номера",
     "Хоткеи Фамилии",
     "Хоткеи Школа",
     "Хоткеи время старта",
     "Хоткеи время финиша",
     "Хоткеи чистое время",
     "Хоткеи метка"
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

def GUI_show(status: GUI_status):
    """
    Функция отображает интерфейс программы в зависимости от объекта переменной GUI_status
    """
    console.clear()
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
            if(j == status.curY and i == status.curX):
                temp = "[black on white]"
            list.append(temp + x)

        table.add_row(list[0], list[1],list[2],list[3],list[4],list[5],list[6])

    console.print(status.hint1)
    console.print(table)
    console.print(status.hint2)
