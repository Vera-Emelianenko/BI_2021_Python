# Description
This repo was created as part of the python course at [Bioinformatics institute](https://bioinf.me/en/education/) (Bioinformatics for biologists, online, 2021). The repo mainly contains python course homeworks. 

# Files 

## Homework1 
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

