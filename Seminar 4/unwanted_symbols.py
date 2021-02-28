# Определяем, какие лишние символы есть

genome_path = 'C:\GRCh38.p13.genome.fa'
genome_path = 'D:\Downloads\Arabidopsis.fasta'

file = open(genome_path, 'r')
i = 0
l = True
while l:
    l = file.readline().replace('\n', '')
    k = l.replace('G', '').replace('C', '').replace('A', '').replace('T', '').replace('N', '')
    if k and k[0] != '>':
        print(k)
        print(i)
    i += 1
print(i)
