genome_path = 'test_genome.fasta'
genome_path = 'D:\Downloads\Ecoli.fasta'
genome_path = 'C:\GRCh38.p13.genome.fa'
genome_path = 'D:\Downloads\Arabidopsis.fasta'

file = open(genome_path, 'r')

# Нарезаем геном на фрагменты
def genome_splitting(mer):
    mer_set = set()
    double_line = ['', '']
    l = True
    file.seek(0)        # Передвигаем указатель в начало файла
    while l:            # Читаем файл построчно
        k = file.readline().replace('\n', '')
        if k.replace('N', '') != '':
            l = k.replace('N', '')
        elif k == '':
            break       # Прерываем цикл, если дошли до конца файла
        else:
            continue    # Пропускаем итерацию, если вся строка - это N

        if l and l[0] != '>':
            double_line[0], double_line[1] = double_line[1], l
            d_line_str = "".join(double_line) # Склеиваем две строки в одну
            for i in range(len(d_line_str)-mer+1):
                mer_set.add(d_line_str[i:i+mer])
        else:
            double_line = ['', '']

        if len(mer_set) >= 4 ** mer:
            break       # Прерывем цикл, если уже все возможные k-меры найдены
    return mer_set

mer = 3                 # Начинаем поиск с 3-меров, так как 1 и 2 наверняка есть в геноме
while True:
    mer_practical = genome_splitting(mer)   # Сколько k-меров найдено в геноме
    mer_theoretical = 4 ** mer              # Сколько k-меров существует
    print(len(mer_practical))
    print(mer_theoretical)
    if len(mer_practical) < mer_theoretical:
        break                               # Если найдены не все существующие фрагменты - прерываем цикл
    else:
        mer += 1
file.close()

print('\a', mer_theoretical-len(mer_practical), f"{mer}-mer'ов не встречаются \
в геноме")
