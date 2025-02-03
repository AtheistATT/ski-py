import data
import pdb


def new_report(table, type, pos_mark, neg_mark):
    
    filtred = [] 

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

    pdb.set_trace()
