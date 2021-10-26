# Description
This repo was created as part of the python course at [Bioinformatics institute](https://bioinf.me/en/education/) (Bioinformatics for biologists, online, 2021). The repo mainly contains python course homeworks. 

# Files 

### Homework1 
File `dna_rna_trancriber.py`. 

Program that works with sequences of nucleic acids. 

Commands:

`exit` - exits the program   
`help` - prints this help message and waits for the next command  
`trancribe` - prints the transcribed coding string of DNA to RNA   
(so it will give the same string but with all 'T' replaced by 'U'). 
! Returns the same string if input is an RNA string.   
Example: ATGCA -> AUGCA  
`reverse` - prints the reversed sequence   
Example: ATGCA -> ACGTA  
`complement` - prints the complement sequence   
If the sequence can be either DNA or RNA (e. g. "AGGGCCCA"), the complement string is generated as DNA (e. g. "TCCCGGGA" and not "UCCCGGGA").  
If you want to get complement of an RNA string that does not contain uracil, use 'complement RNA'.  
Example: ATGCA -> TACGT  
`reverse complement` - prints reverse complement sequence.   
If the sequence can be either DNA or RNA, the reverse complement string is generated as DNA  
Example: ATGCA -> TGCAT  
`complement RNA` - prints complement sequence, forced to use 'U' as a complement of 'A'   
Example: AGGGCCCA -> UCCCGGGA  

The program preserves the case (e. g. complement from 'AtGc' will be 'TaCg').  
The program will correct the user that tries to use the sequence with incorrect alphabet (e.g. 'ATGCP' or 'GttCU').   
! The use of 'N' or white spaces is not supported!  

### Homework3 
File `fastq-filtrator.py`. 

Filters fastq files by GC content, mean quality of the read and length. Does not trim low-quality ends.
Options:

`input_fastq` - path to file to filter (e.g. './data/fastq_example.fastq'). Only .fq and fastq files are supported.
Gzipped files are not supported.

`output_file_prefix` - path to output file.
If save_filtered = False, then output file will get name output_file_prefix + '_passsed.fastq'.
If save_filtered = True, additional file output_file_prefix + '_failed.fastq' will be written.

`gc_bounds` - upper and lower limit for GC content (e. g. '0;50'). Default '0, 100'.
Reads that have GC content lower than lower bound or higher that upper bound will be discarded.
GC-content is calculated as (G+C)/(G+C+A+T), Ns are not taken into account!

`length_bounds` - upper and lower limit for length (e. g. '0;200'). Default '0, 2**32'.
Reads that are shorter than lower bound or longer that upper bound will be discarded.

`quality_threshold` - average quality of the read to pass the filter. Deafault '0'

`save_filtered` ('True' or 'False') - set 'True' to save discarded reads in a file output_file_prefix + '_failed.fastq'
Default 'False'.

Usage example:

```
python fastq-filtrator.py input_fastq='./data/fastq_example.fastq' output_file_prefix='./test4' gc_bounds='0;100'
length_bounds='0;200' quality_threshold=27 save_filtered='True' #creates ./test4_failed.fastq and ./test4_passed.fastq
```
