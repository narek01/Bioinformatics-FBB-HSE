genome_path = 'D:\Downloads\Arabidopsis.fasta'
genome_path = 'test_genome.fasta'
genome_path = 'D:\Downloads\Ecoli.fasta'
genome_path = 'C:\GRCh38.p13.genome.fa'


file = open(genome_path, 'r')
genome = file.readlines()
for element in genome:
    if ">" in element:
        genome.remove(element)
genome = "".join(genome).replace('\n', '').replace('N', '')
file.close()


def genome_splitting(mer):
    mer_set = set()
    for i in range(len(genome)-mer+1):
        mer_set.add(genome[i:i+mer])
        if len(mer_set) == 4 ** mer:
            break
    return mer_set


mer = 3 # Начинаем поиск с 3-меров, так как 1 и 2 наверняка есть в геноме
while True:
    mer_practical = genome_splitting(mer)
    mer_theoretical = 4 ** mer
    print(len(mer_practical))
    print(mer_theoretical)
    if len(mer_practical) < mer_theoretical:
        break
    else:
        mer += 1

print('\a', mer_theoretical-len(mer_practical), f"{mer}-mer'ов не встречаются в геноме")
