import csv

mers = [i for i in range(8, 10+1)] # Вводим желаемый размер фрагментов
corona_file = 'coronavirus_proteome.fasta' # Вводим пути к протеомам
human_file = 'human_proteome.fasta'

# Читаем файл в переменную, каждый белок - элемент списка
def reading_file(input_path, output_variable):
    file = open(input_path, 'r')
    i = -1
    #output_variable.append(['',''])
    for line in file:
        if line[0] != '>':
            output_variable[i][0] += line.replace('\n', '')
        elif line[0] == '>':
            i += 1
            output_variable.append(['',''])
            output_variable[i][1] += line[line.find('|'):line.find('OS=')-1]
    file.close()

# Дробим белки на фрагменты
def x_mers(input, output, mers):
    for mer in mers:
        for protein in input:
            if not(0 <= input.index(protein) < len(output)):
                output.append([[], ''])

            for i in range(len(protein[0])-mer+1):
                output[input.index(protein)][0].append(protein[0][i:i+mer])
            output[input.index(protein)][1] = protein[1]
    return output

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


cov_proteins = []
cov_mers = []
human_proteome = []
result = []

reading_file(corona_file, cov_proteins)
reading_file(human_file, human_proteome)
#human_proteome = " ☠ ".join(human_proteome) # Пробразуем список в строку
x_mers(cov_proteins, cov_mers, mers)
#print(human_proteome)

# Сравниваем фрагменты с человеческим протеомом
print('k-mer', 'SARS protein', 'Human protein', sep=' - ')
for h_prot in human_proteome:
    for cov_mer_name in cov_mers:
        for cov_mer in cov_mer_name[0]:
            if cov_mer in h_prot[0]:
                print(cov_mer, cov_mer_name[1], h_prot[1], sep=' - ')
                result.append([cov_mer, cov_mer_name[1], h_prot[1]])

csv_writer(result, 'sars_in_human.csv')
