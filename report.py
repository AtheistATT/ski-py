import data
import pdb
import gui

def new_report(table, type, pos_mark, neg_mark):
    
    filtred = [] 
    report = []
    if pos_mark != '':
       for row in table:
            if pos_mark in row[6]:
                filtred.append(row)
    if neg_mark != '':
        i = len(filtred) - 1
        while i >= 0:
            if neg_mark in filtred[i][6]:
                del filtred[i]
            i -= 1

    if type == "1":
        report.append(["Номер", "Фамилия", "Школа", "Время старта"])
        for row in filtred:
            report.append([row[0], row[1], row[2], row[3]])


    file_name = gui.input_text("Введите название файла>>>")

    data.Set_table(report, file_name + ".csv")
