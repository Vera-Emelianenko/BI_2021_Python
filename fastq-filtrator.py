import sys

# defining all messages that the program uses
help_message = '''
This program filters fastq files by GC content, mean quality of the read and length. It does not trim low-quality ends.
Options:

input_fastq - path to file to filter (e.g. './data/fastq_example.fastq'). Only .fq and fastq files are supported.
Gzipped files are not supported.

output_file_prefix - path to output file.
If save_filtered = False, then output file will get name output_file_prefix + '_passsed.fastq'.
If save_filtered = True, additional file output_file_prefix + '_failed.fastq' will be written.

gc_bounds - upper and lower limit for GC content (e. g. '0;50'). Default '0, 100'.
Reads that have GC content lower than lower bound or higher that upper bound will be discarded.
GC-content is calculated as (G+C)/(G+C+A+T), Ns are not taken into account!

length_bounds - upper and lower limit for length (e. g. '0;200'). Default '0, 2**32'.
Reads that are shorter than lower bound or longer that upper bound will be discarded.

quality_threshold - average quality of the read to pass the filter. Deafault '0'

save_filtered ('True' or 'False') - set 'True' to save discarded reads in a file output_file_prefix + '_failed.fastq'
Default 'False'.

Usage example:

python fastq-filtrator.py input_fastq='./data/fastq_example.fastq' output_file_prefix='./test4' gc_bounds='0;100'
length_bounds='0;200' quality_threshold=27 save_filtered='True' #creates ./test4_failed.fastq and ./test4_passed.fastq
'''

input_file_missing_message = '''input file not defined! Try checking spelling\nUsage example:
python fastq-filtrator.py input_fastq='./data/fastq_example.fastq'
output_file_prefix='test' gc_bounds='0;50' length_bounds='0;200' quality_threshold='20' save_filtered='True' '''

output_prefix_missing_message = '''output file prefix file not defined! Try checking spelling\nUsage example:
python fastq-filtrator.py input_fastq='./data/fastq_example.fastq'
output_file_prefix='test' gc_bounds='0;50' length_bounds='0;200' quality_threshold=20 save_filtered='True' '''


# define a function to take arguments from the user
def take_user_input():
    # if one of two necessary arguments (input and output files) is missing:
    if len(sys.argv) < 3:
        sys.exit(help_message)
    # if the number of argumemts id right, we can start assigning the values to variables
    else:
        # first define the default parameters

        # in fact this might not be necessary since I define default parameters inside function definition
        # but I don't know how to call main function later with all these parameters if they don't exist
        # this function could return five variables, but instead it assigns values to global variables and returns None
        global length_bounds_list
        length_bounds_list = [0, 2**32]
        global gc_bounds_list
        gc_bounds_list = [0, 100]
        global quality_threshold_number
        quality_threshold_number = 0
        global saving_filtered
        saving_filtered = False

        # assign non-default values
        for arg in sys.argv:
            if arg.split('=')[0] == 'input_fastq':
                global input_file
                input_file = arg.split('=')[1]
            elif arg.split('=')[0] == 'output_file_prefix':
                global output_prefix
                output_prefix = arg.split('=')[1]
            elif arg.split('=')[0] == 'gc_bounds':
                gc_bounds_list = [int(i) for i in arg.split('=')[1].split(';')]
            elif arg.split('=')[0] == 'length_bounds':
                length_bounds_list = [int(i) for i in arg.split('=')[1].split(';')]
            elif arg.split('=')[0] == 'quality_threshold':
                quality_threshold_number = int(arg.split('=')[1])
            elif arg.split('=')[0] == 'save_filtered':
                if arg.split('=')[1] == 'True':
                    saving_filtered = True
    # check that input file argument is present
    try:
        input_file
    except NameError:
        sys.exit(input_file_missing_message)
    # check that output file argument is present
    try:
        output_prefix
    except NameError:
        sys.exit(output_prefix_missing_message)
    # warn user if the extention is wrong
    if input_file.split('.')[-1] != 'fastq' and input_file.split('.')[-1] != 'fq':
        sys.exit('Wrong file extention, use .fq or .fastq files. If the file is gzipped try using `gunzip filename`')


# define main function
def main(input_fastq, output_file_prefix, gc_bounds=[0, 100],
         length_bounds=[0, 2**32], quality_threshold=0, save_filtered=False):
    # count how many reads pass the filter
    # it was not required in the task but it is useful to know both for code testing and for real work
    written_passed_reads = 0
    try:
        # open file to write down filtered reads
        new_file = open(output_file_prefix + '_passed.fastq', "w")
        # Warn user if output file not found (the file is created by python but the directory is not)
    except FileNotFoundError:
        sys.exit("Output file directory not found, can't create output file")
    # if we want to save failed reads, we need to open one more file
    if save_filtered:
        # I don't check for the directory here
        # because output_file_prefix is the same and the file is created de novo anyways
        new_file2 = open(output_file_prefix + '_failed.fastq', "w")
        written_failed_reads = 0
    # try opening input file
    try:
        with open(input_fastq, 'r') as fastqfile:
            # print which input file the program is using
            # again it is not necessary but might be useful if we accidentally typed the wrong filename
            print(f"Reading from file {input_fastq}")
            # set a counter of lines - needed to determine which line to check for quality
            # (every 4th), which line is name and so on
            i = 0
            # buffer that will hold 4 lines at a time to be written or discarded (1 read)
            list_of_lines = []
            # variable to decide whether to discard or to save this read
            checker = True
            # iterate over each line of the file
            # I purpusfully don't open the whole file at once because .fastq file may be very big (several Mb or more)
            # so I don't want to hold this amount of data in the memory
            # that is why I open one line at a time,
            # write it down to the list and then empty the list once the read is over
            # this introduces trailing \n in one of the files (.passed.fastq) or (failed.fastq)
            # I don't know how to solve this problem elegantly
            # but at least I tested the program on 122M .fastq file and it performed fine (less than a minute)
            for line in fastqfile:
                # write each line to the buffer
                list_of_lines.append(line)
                # change line number - first line will have number 1
                i += 1
                # if any line does not pass at least one filter, change checker value to false
                if not (pass_quality_threshold(line, i, quality_threshold) and pass_gc_bounds(line, i, gc_bounds) and
                        pass_length_bounds(line, i, length_bounds)):
                    checker = False
                # if we are at the end of the read (line 4, line 8, line 12...)
                if i % 4 == 0:
                    # if checker was not changed, so that all lines passed all filters,
                    # write those 4 lines to the output file
                    if checker:
                        new_file.write(''.join(list_of_lines))
                        written_passed_reads += 1
                    # if the read didn't pass the filter, discard it or write down to _failed.fastq
                    else:
                        if save_filtered:
                            new_file2.write(''.join(list_of_lines))
                            written_failed_reads += 1
                    # in any case, empty the buffer and set checker value for True
                    list_of_lines = []
                    checker = True
    # Warn user if input file was not found
    except FileNotFoundError:
        sys.exit("Input file not found")
    # close the output file
    new_file.close()
    # print out how many reads were written
    print(f"{written_passed_reads} reads passed, written to {output_file_prefix}_passed.fastq")
    # do the same for failed reads
    if save_filtered:
        new_file2.close()
        print(f"{written_failed_reads} reads didn't pass, written to {output_file_prefix}_failed.fastq")


# function to filter for quality
def pass_quality_threshold(line, i, quality_threshold):
    # if its the line with quality
    if i % 4 == 0:
        # delete '\n'
        line = line.strip()
        # create list for phred scores
        quality_numbs = [ord(character) for character in line]
        # calculate average quality shifted by 33
        quality_mean = sum(quality_numbs)/len(quality_numbs)
        # check the quality against quality threshold
        if quality_mean - 33 < quality_threshold:
            return (False)
        else:
            return (True)
    # if the line does not show quality return true
    else:
        return (True)


# filter for GC-content
def pass_gc_bounds(line, i, gc_bounds):
    line = line.strip()
    # if line contains nucleotides
    if (2 + i) % 4 == 0:
        # calculate GC content
        gc_content = 100*(line.count('G')+line.count('C'))/(
                    line.count('T')+line.count('A')+line.count('G')+line.count('C'))
        if gc_content > gc_bounds[0] and gc_content < gc_bounds[1]:
            return (True)
        else:
            return (False)
    # if the line does not contain nucleotides return true
    else:
        return (True)


# filter for length
def pass_length_bounds(line, i, length_bounds):
    line = line.strip()
    if (2 + i) % 4 == 0:
        if len(line) > length_bounds[0] and len(line) < length_bounds[1]:
            return (True)
        else:
            return (False)
    else:
        return (True)


# call functions that take user input and perform the filterings
take_user_input()
main(input_file, output_prefix, gc_bounds_list, length_bounds_list, quality_threshold_number, saving_filtered)
