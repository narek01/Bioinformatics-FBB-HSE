na = input("Enter the nucleotide sequence : ")
na = na.lower()

if 'u' in na and 't' in na:
    print('Check the sequence!')
elif 'u' in na:
    rna_c = na.replace('a', 'U').replace('g', 'C').replace('u', 'A').replace('c', 'G')
    print(rna_c[::-1])
else:
    dna_c = na.replace('a', 'T').replace('g', 'C').replace('t', 'A').replace('c', 'G')
    print(dna_c[::-1])
