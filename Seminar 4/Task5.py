genome_path = 'SARS-CoV-2-without-poly-a.fasta'
genome_path = 'SARS-CoV-2.fasta'


def genome_splitting(mer):
    mer_dict = dict()
    for i in range(len(genome)-mer+1):
        if genome[i:i+mer] in mer_dict.keys():
            mer_dict[genome[i:i+mer]].append(i)
        else:
            mer_dict[genome[i:i+mer]] = [i]
    return mer_dict


file = open(genome_path, 'r')
genome = file.readlines()
for element in genome:
    if ">" in element:
        genome.remove(element)
genome = "".join(genome).replace('\n', '').replace('N', '')
file.close()

mer = 1
breaker = False

while True:
    print(mer)
    dictionary = genome_splitting(mer)
    for value in dictionary.values():
        if len(value) > 1:
            breaker = False
            break
    if breaker == True:
        break
    else:
        mer += 1
        breaker = True

print(f"При минимальном k = {mer} каждому фрагменту соответствует \
ровно одна позиция")
