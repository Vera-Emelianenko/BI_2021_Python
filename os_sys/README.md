# Command-line tools in python (wc.py, ls.py, rm.py, sort.py)

## Description

This suit of pseudo-command-line tools was created as part of the python course at [Bioinformatics institute](https://bioinf.me/en/education/) (Bioinformatics for biologists, online, 2021). 

The advantages of using our .py scripts in comparison with basic command line tools: 
 - have less options (less chanses to get confused!)
 - need to be made executable or run with python in front of them (you can be sure not to run them accidentally!)
 - have higher probability to though some error (you will have more fun!)
 - work slower (you can go and drink your coffee while the program is working for you)

## Installation

The installation process does not rely on distinct OS features and can be applied for Windows, Linux and Mac systems. The script is supposed to be run from bash-like command line. To use it on Windows, please install Windows Subsystem for Linux (WSL) (this [user guide](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) can help you). Then you can run the commands in the WSL command line. The script is written and tested in Python 3.8, and the installation process assumes you have python3 on your mashine. You can check the current version of python using `python --version`. To install or update Python, visit [www.python.org](https://www.python.org/downloads/).The scripts were tested in WSL1 Ubuntu-20.04 in Windows Terminal 1.11.2921.0 in Microsoft Windows [Version 10.0.19043.1288] (Windows 10 Home Version 21H1), Python 3.8.5. The scripts use only standart libraries: 

#### Downloading
You can download the archive with wc.py, ls.py, rm.py and sort.py using wget:

```
wget https://github.com/Vera-Emelianenko/BI_2021_fastqc/archive/refs/heads/main.zip
unzip main.zip
cd BI_2021_fastqc-main
```
Alternatively, the archive with the content of the project can be downloaded via visual interface of GitHub. Go to *main* branch, choose green button "Code" on the upper right and download zip. Zip archive might be unpacked with any tool you have or with unzip (`unzip BI_2021_fastqc.zip`)

You can also download the project via git clone: 
```
git clone https://github.com/Vera-Emelianenko/BI_2021_fastqc.git

## Contributors

- Vera Emelianenko [@Vera-Emelianenko](https://github.com/Vera-Emelianenko) wrote wc.py, ls.py, rm.py, sort.py, README. 


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

