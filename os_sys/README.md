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
wget https://github.com/Vera-Emelianenko/BI_2021_Python/archive/refs/heads/os_sys.zip
unzip os_sys.zip
cd BI_2021_Python-os_sys/os_sys
```

To run scripts, print `python script.py`, where script.py is a name of the script you want to run, e. g.
```
python ls.py
```

#### Making files executable
In theory, files should be executable when downloaded. However, you may want to make them executable yourself: 

```
chmod +x rm.py
chmod +x ls.py
chmod +x sort.py
chmod +x wc.py
```

Then, you can run the scripts from the current directory without prefixing them with `python`: 

```
./ls.py
```

#### Testing the scripts
To test that all scripts work, you may try the following
```
./ls.py
./wc.py test.txt -l -c -w
./sort.py test.txt
mkdir testdir
touch testdir/testfile
./rm.py testdir -r
```

## Files description

All programs have option -h (--help). 

#### File `wc.py`.

Program that is `wc` analog in python to count lines, words, bytes

Usage: 

```
./wc.py [-h] [-l] [-w] [-c] [file [file ...]]
```
If no file is specified, the program reads the input from stdin. 

flags:

`-c` - count bytes
`-l` - count lines
`-w` - count words   
`-h` - prints help message and exits

#### File `ls.py`.

Program that is `ls` analog in python to list all files and directories in a specified directory. 

Usage: 

```
./ls.py [-h] [-a] [directory [directory ...]]
```
If no derectory is specified, the program will list the contents of the current directory ('./'). 

flags:

`-a` - do not ignore entries starting with .
`-h` - prints help message and exits

#### File `sort.py`.

Program that is `sort` analog in python to sort an input file/

Usage: 

```
./sort.py [-h] [file [file ...]]
```
If no file is specified, the program reads the input from stdin.

flags:

`-h` - prints help message and exits

#### File `rm.py`.

Program that is `rm` analog in python to remove files or files and directories (if run recoursively).

Usage: 

```
./rm.py [-h] [-r] [file_or_dir [file_or_dir ...]]
```

flags:
`-r` remove recoursively
`-h` - prints help message and exits

## Contributors

- Vera Emelianenko [@Vera-Emelianenko](https://github.com/Vera-Emelianenko) wrote wc.py, ls.py, rm.py, sort.py, README. 
