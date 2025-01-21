from rich import console, table
from rich.console import Console
from rich.table import Table

class GUI_status:
    title = ""
    sh_list = []
    table = []
    curX = 0
    curY = 0
    hint1 = ""
    hint2 = ""
    




console = Console()

def GUI_show(status: GUI_status):

    table = Table(title=status.title)

    table.add_column("Номер")
    table.add_column("Фамилия")
    table.add_column("Школа")
    table.add_column("Время старта")
    table.add_column("Время финиша")
    table.add_column("Чистое время")
    table.add_column("Метка")


    table.add_row("1","Иванов Иван" ,"Школа #0", "00:20'00" ,"00:34'26", "00:14'26", "М12")

    console.print(status.hint1)
    console.print(table)
    console.print(status.hint2)
