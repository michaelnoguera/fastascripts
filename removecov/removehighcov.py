import sys
from Bio import SeqIO

file = sys.argv[1]
threshold = float(sys.argv[2])

clean_filename = file + '.clean.fa'
highcov_filename = file + '.highcov.fa'

print('\nOpened file ' + file)
print('Removing high entries, exclusive, with threshold ' + str(threshold))

# Keeps entries below the threshold, inclusive

clean = open(clean_filename, 'w')
high = open(file + '.highcov.fa', 'w')

for record in SeqIO.parse(file, 'fasta'):
    if float(record.description.split("cov_", 1)[1]) <= threshold:
        clean.write(record.format('fasta'))
    else:
        high.write(record.format('fasta'))

clean.close()
high.close()
