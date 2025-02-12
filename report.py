from typing import Counter
import data
import pdb
import gui
import datetime


def to_time(text_time):
    hours, minutes, seconds = text_time.split(':')
    seconds, miliseconds = seconds.split('.')
    miliseconds = int(miliseconds) * 10

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    return datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds,microseconds=miliseconds)

def to_str(time):
    total_seconds = int(time.total_seconds())
    hours, remaind = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remaind, 60)
    miliseconds = int(time.microseconds/10000)

    return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

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

    if pos_mark == '' and pos_mark == '':
        filtred = table

    if type == "1":
        report.append(["Номер", "Фамилия", "Школа", "Время старта"])
        for row in filtred:
            report.append([row[0], row[1], row[2], row[3]])

    if type == "2":
        for row in filtred:
            report.append(  [row[2], to_time(row[5])])
        report = sorted(report, key=lambda x: (x[0], x[1]))

        first_c = [row[0] for row in report]
        count = Counter(first_c)
        report = [row for row in report if count[row[0]] >= 4]

        best = []
        cur_sh = ''
        count = 0
        
        for row in report:
            if row[0] != cur_sh:
                cur_sh = row[0]
                count = 0

            if count <= 3:
                best.append(row)

            count += 1

        cur_sh = ''
        sum_sh =[]

        for row in best:
            if cur_sh != row[0]:
                cur_sh = row[0]
                sum_sh.append(row)
            else:
                sum_sh[-1][1] += row[1]
        
        sum_sh = sorted(sum_sh, key=lambda x:(x[1]))

        report = [["Место", "Школа", "Результат"]]

        for i in range(len(sum_sh)):
            report.append([str(i + 1), sum_sh[i][0], to_str(sum_sh[i][1])])

    if type == "3":
        
        for row in filtred:
            row[5] = to_time(row[5])
        
        filtred = sorted(filtred, key=lambda x:(x[5]))

        for row in filtred:
            row[5] = to_str(row[5])

        report = [["Место", "Фамилия", "Номер", "Школа", "Результат"]]

        for i in range(len(filtred)):
            report.append([str(i+1), filtred[i][1], filtred[i][0], filtred[i][2], filtred[i][5]])


#   pdb.set_trace()
    file_name = gui.input_text("Введите название файла>>>")

    data.Set_table(report, file_name + ".csv")
