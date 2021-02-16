f = open("annotation.gff")   # Открываем файлик с аннотацией
lines = f.readlines()        # Читаем файл построчно (на выходе список из строк)
f.close()

out = list()

for line in lines:
    if line[0] != '#':           # Пропускаем строки, начинаюющиеся на "#"
        line = line.split('\t')  # Делим строки таблицы на столбцы (получаем список)
        if line[2] == 'gene':    # Берём только гены
            name_pos = line[8].find('Name')+5   # Находим позицию начала гена
            name = line[8][name_pos:line[8].find(';', name_pos)] # Выделяем из строчки название гена
            out.append([int(line[4]) - int(line[3]) + 1, name])

for t in out:
    print('Gene: ', t[1], '; Length: ', t[0], sep='')
