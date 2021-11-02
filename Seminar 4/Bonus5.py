mers = [i for i in range(8, 10+1)] # Вводим желаемый размер фрагментов
corona_file = 'coronavirus_proteome.fasta' # Вводим пути к протеомам
human_file = 'human_proteome.fasta'

# Читаем файл в переменную, каждый белок - элемент списка
def reading_file(input_path, output_variable):
    file = open(input_path, 'r')
    i = 0
    output_variable.append('')
    for line in file:
        if line[0] != '>':
            output_variable[i] += line.replace('\n', '')
        elif output_variable[i] != '':
            output_variable.append('')
            i += 1
    file.close()

# Дробим белки на фрагменты
def x_mers(input, output, mers):
    for mer in mers:
        for protein in cov_proteins:
            for i in range(len(protein)-mer+1):
                cov_mers.append(protein[i:i+mer])


cov_proteins = []
cov_mers = []
human_proteome = []
result = []

reading_file(corona_file, cov_proteins)
reading_file(human_file, human_proteome)
human_proteome = " ☠ ".join(human_proteome) # Пробразуем список в строку
x_mers(cov_proteins, cov_mers, mers)

# Сравниваем фрагменты с человеческим протеомом
counter = 0
for cov_mer in cov_mers:
    if cov_mer in human_proteome:
        counter += 1
        result.append(cov_mer)
result = list(set(result))

# Считаем число фрагментов
mer8, mer9, mer10 = 0, 0, 0
for match in result:
    mer8 += 1 if len(match) == 8 else 0
    mer9 += 1 if len(match) == 9 else 0
    mer10 += 1 if len(match) == 10 else 0

print('Найденные фрагменты:\n', result)
print('8-mer: ', mer8)
print('9-mer: ', mer9)
print('10-mer: ', mer10)
