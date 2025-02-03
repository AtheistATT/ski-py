def Get_sh_list():
    try:
        with open('data/sh_list.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except Exception as e:
                    print(e)

def Set_sh_list(sh_list = []):
    try:
        with open('data/sh_list.txt', 'w', encoding='utf=8') as file:
            for line in sh_list:
                file.write(line + '\n')
    except Exception as e:
        print(e)

def Get_table():
    main_table = []
    try:
        with open('data/data.txt', 'r', encoding='utf-8') as file:
            for line in file:
                main_table.append([item.strip() for item in line.split(',')])
    except Exception as e:
        print(e)

    return main_table

def Set_table(main_table = [], file_name = 'data/data.txt'):
    try:
        with open(file_name, 'w', encoding='utf=8') as file:
            for sublist in main_table:
                file.write(', '.join(sublist) + '\n')
    except Exception as e:
        print(e)
