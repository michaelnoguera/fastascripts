import sys
import numpy as np

# Sets the column headers to off by default.
t = False

# Sets the default delimiter to be tab.
delimiter = '\t'

# Instructs the program to read the first input filename at the second item in the arguments list.
arg_offset = 1

# Parses special arguments
if '-h' in sys.argv:
	# Help message
	print('\ncombinecsv.py by Michael Noguera')
	print('\nUsage:')
	print('\tpython combinetab.py [options] file1 file2 file3...')
	print('\tYou can have any number of files. Row headers will be taken from the first file specified.')
	print('\nOptions:')
	print('\t-t \tincludes column titles based on the file names of the various files')
	print('\t-d \tallows the use of delimeters other than tab. (-d "," or -d ".")')
	print('\t-h \tdisplays this message and exits\n')
	quit()

if '-t' in sys.argv:
	# If column headers were requested, this changes the variable t so that they will be included later on.
	if sys.argv[1] == '-t' or (sys.argv[3] == '-t' and sys.argv[1] == '-d'):
		t = True
		# Tells the program to read filenames from one argument farther right, so that it does not interpret -t as a file.
		arg_offset += 1

	else:
		# Reminds the user of the syntax if they attempt to call -t or -d where a file name should be.
		print('\nOops! Options, such as -t or -d, must be placed before the files to be combined when you run this command.')
		print('The correct syntax is:')
		print('\tpython combinetab.py [options] file1 file2 file3...\n')
		quit()

if '-d' in sys.argv:
	# If a custom delimiter was specified, this changes the delimeter variable.
	if sys.argv[1] == '-d':
		delimiter = sys.argv[2]
		# Tells the program to read filenames from two argument farther right, so that it does not interpret -d or the delimiter as a file.
		arg_offset += 2

	elif (sys.argv[2] == '-d' and sys.argv[1] == '-t'):
		delimiter = sys.argv[3]
		arg_offset += 2

	else:
		# Reminds the user of the syntax if they attempt to call -t or -d where a file name should be.
		print('\nOops! Options, such as -t or -d, must be placed before the files to be combined when you run this command.')
		print('The correct syntax is:')
		print('\tpython combinecsv.py [options] file1 file2 file3...\n')
		quit()


# This tells the program where to read input filenames from.
files = sys.argv[arg_offset:]

# Reads the first column of the first file provided and saves it in the variable row_headers.
row_headers = np.genfromtxt(
	files[0],
	skip_header = 0,
	delimiter = delimiter,
	dtype = 'str',
	filling_values = '',
	usecols = [0],
	)

# Defines the function read_second_column(). This takes a file argument as input, reads the
# file, and returns the second column.
def read_second_column(file):
	return np.genfromtxt(
		file,
		skip_header = 0,
		delimiter = delimiter,
		dtype = 'str',
		filling_values = '',
		usecols = [1],
	)

# Creates a new variable output. This varible will be used to put all the columns in the output
# before it is printed to the console.
output = row_headers

# Iterates through the file arguments, and adds the second column of each onto the end of the array.
for file in files:
	temp = read_second_column(file)
	output = np.column_stack((output, temp))

# Generates the column headers if the -t argument was chosen.
if t:
	column_headers = np.array(files[0].split('.')[0])
	for file in files:
		column_headers = np.column_stack((column_headers, file.split('.')[1]))
	output = np.vstack((column_headers, output))

# Iterates through the output array and prints it to the console one row at a time.
for row in output:
	print(delimiter.join(row))