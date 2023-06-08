def transform_table(input_table):
    # Удаление пустых столбцов
    input_table = [list(filter(lambda x: x is not None, row))
                   for row in input_table]
    input_table = list(filter(lambda x: len(x) > 0, input_table))
    
      # Удаление дублей строк
    unique_rows = []
    for row in input_table:
        if row not in unique_rows:
            unique_rows.append(row)
    input_table = unique_rows
    
    # Удаление пустых строк
    input_table = list(filter(lambda x: None not in x, input_table))


    output_table = []
    for i in range(len(input_table)):
        new_row = []
        for j in range(len(input_table[i])):
            cell = input_table[i][j]
            if cell == 'Выполнено':
                new_row.append('true')
            elif cell == 'Не выполнено':
                 new_row.append('false')
            elif j == 1:
                date_parts = cell.split('/')
                d = int(date_parts[0])
                m = int(date_parts[1])
                y = int(date_parts[2])
                d_str = \
                    '{:02d}-{:02d}-{:02d}'.format(y % 100, m, d)
                new_row.append(d_str)
            elif j == 2:
                float_cell = float(cell)
                new_row.append(str(format(round(float_cell, 2), ".2f")))
            else:
                new_row.append(cell.replace('[at]', '@'))
        output_table.append(new_row)
    return output_table
    
    # Преобразование содержимого ячеек       
    '''for i in range(len(output_table)):
        for j in range(len(output_table[i])):
            cell = output_table[i][j]
            if cell == 'Выполнено':
                output_table[i][j] = 'true'
            elif cell == 'Не выполнено':
                output_table[i][j] = 'false'
            elif j == 1:
                date_parts = cell.split('/')
                d = int(date_parts[0])
                m = int(date_parts[1])
                y = int(date_parts[2])
                d_str = \
                    '{:02d}-{:02d}-{:02d}'.format(y % 100, m, d)
                output_table[i][j] = d_str
            elif j ==2:
                float_cell = float(cell)
                output_table[i][j] = round(float_cell, 2)
            else:
                output_table[i][j] = cell.replace('[at]', '@')
                      
    return output_table'''
print(transform_table([['Выполнено', '19/10/2002', '0.3923', 'zeremev58[at]rambler.ru'], ['Выполнено', '23/03/2004', '0.5329', 'zesimko70[at]mail.ru']]))

'''  # Преобразование содержимого ячеек
    output_table = []
    for row in input_table:
        new_row = []
        for cell in row:
            if cell == 'Выполнено':
                new_row.append('true')
            elif cell == 'Не выполнено':
                new_row.append('false')
            elif row == 1:
                date_parts = cell.split('/')
                d = int(date_parts[0])
                m = int(date_parts[1])
                y = int(date_parts[2])
                d_str = \
                    '{:02d}-{:02d}-{:02d}'.format(y % 100, m, d)
                output_table[i][j] = d_str
            elif type(cell) == float:
                new_row.append(round(cell, 2))
            else:
                new_row.append(cell.strftime('%y-%m-%d'))
        output_table.append(new_row)
    
    return output_table'''
