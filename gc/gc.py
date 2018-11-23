import sys
file = sys.argv[1]

#Modifies code from https://bioinformatics.stackexchange.com/a/2658 thanks to user Chris_Rands
from Bio import SeqIO
from Bio.SeqUtils import GC

for record in SeqIO.parse(file, 'fasta'):
    print('{}\t{}'.format(record.description, round(GC(record.seq), 2)))