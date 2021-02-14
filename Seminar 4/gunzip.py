import gzip
ip = 'D:\Downloads\GRCh38.p13.genome.fa.gz'

#output file to be filled

op = open("D:\Downloads\GRCh38.p13.genome.fa","w")

with gzip.open(ip,"rb") as ip_byte:
    op.write(ip_byte.read().decode("utf-8"))
    #wf.close()
