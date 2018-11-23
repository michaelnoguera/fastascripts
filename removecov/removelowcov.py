import sys
from Bio import SeqIO

file = sys.argv[1]
threshold = float(sys.argv[2])

clean_filename = file + '.clean.fa'
lowcov_filename = file + '.lowcov.fa'

print('\nOpened file ' + file)
print('Removing low entries, exclusive, with threshold ' + str(threshold))

# Keeps entries above the threshold, inclusive

clean = open(clean_filename, 'w')
low = open(file + '.lowcov.fa', 'w')

for record in SeqIO.parse(file, 'fasta'):
    if float(record.description.split("cov_", 1)[1]) >= threshold:
        clean.write(record.format('fasta'))
    else:
        low.write(record.format('fasta'))

clean.close()
low.close()
