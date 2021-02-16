f = open("annotation.gff")   # Открываем файлик с аннотацией
lines = f.readlines()        # Читаем файл построчно (на выходе список из строк)
f.close()

f = open("coverage.tsv")   # Открываем файлик с аннотацией
reads = f.readlines()        # Читаем файл построчно (на выходе список из строк)
f.close()

out_annot = list()
out_cover = list()

for line in lines:
    if line[0] != '#':           # Пропускаем строки, начинаюющиеся на "#"
        line = line.split('\t')  # Делим строки таблицы на столбцы (получаем список)
        if line[2] == 'gene':    # Берём только гены
            name_pos = line[8].find('Name')+5   # Находим позицию начала гена
            name = line[8][name_pos:line[8].find(';', name_pos)] # Выделяем из строчки название гена
            out_annot.append([int(line[4]) - int(line[3]) + 1, name])

for read in reads:
    read = read.replace('\n', '').split('\t') # Убираем символ переноса строки и делим по табам
    out_cover.append([int(read[1]), read[0]])

# Перебираем списки, находим соотвествующие строки для каждого гена и считаем покрытие
for gene in out_annot:
    for cov in out_cover:
        if gene[1] == cov[1]:
            print('Gene: ', gene[1], '; Coverage: ', round(cov[0]/gene[0], 3), sep='')
