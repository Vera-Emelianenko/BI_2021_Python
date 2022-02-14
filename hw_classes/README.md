# Classes homework

## Description

These four classes were created as part of the python course at [Bioinformatics institute](https://bioinf.me/en/education/) (Bioinformatics for biologists, online, 2021). 

The classes are contained both in `.py` files and Jupyter notebook `Test_classes_notebook_with_class_definition.ipynb`. The notebook without class definition (`Test_classes_notebook.ipynb`) contains just the examples of using the classes, imports the classes themselves from the .py files. Therefore, we do not provide examples in this README.md file. 


## Installation

The classes are supposed to be imported in your code via `from filename import class` (e. g. `from myfasta import Fasta`, given that `myfasta.py` file is in the same directoty as your script). Alternatively, you can just copy and paste the class definition in your code. 

Be aware that the classes require some libraries mentioned in requirements.py, in particular, matplotlib, seaborn, Bio - be sure to install and import them before using the classes. The code was tested in Python 3.8.5.

#### Downloading
You can download the archive with myfasta.py, myrna.py, mybacterialchromosome.py, myset.py, Test_classes_notebook.ipynb, Test_classes_notebook_with_class_definition.ipynb and example .gb and .fasta files using wget: 

```
wget https://github.com/Vera-Emelianenko/BI_2021_Python.git
unzip hw_classes.zip
cd BI_2021_Python-hw_classes/hw_classes
```

#### Testing the scripts
To test that all scripts work, you may try running all the cells in test Jupyter notebooks. If they produced only one error ('not an RNA string'), then you are good to go! 

## Files description

#### File `mybacterialchromosome.py`

Contains the definition of class BacterialChromosome - an example class to contain info about bacterial chromosome and print it out. 

Methods:

print_sequence() - print out the sequence
print_info () - print out chromosome_id, organism and length
from_gbff(path_to_file) - get chromosome id, organism name and sequence length from GB file and assign to a new instance of a class. Only the first record in gb file will be processed!

Attributes:

organism_name - name of bacterium
length - length of the chromosome
sequence - sequence of the chromosome
chromosome_id - id of the chromosome

Since it is just the example class, it allows one bacterial chromosome to have different length and len(sequence). 


#### File `myrna.py`

Contains the definition of class MyRNA - a class that describes RNA

Methods:

translate() - traslation method - returns a protein string using standard genetic code"""
back_transcribe(self) - reverse transcription method - returns a DNA string that corresponds to this RNA

Attributes:

sequence - RNA sequence


#### File `myset.py` - a class that inherits from sets, contains only positive numbers when created and will not add non-positive values.

Methods:

all the methods from set, but the "add" method allows only positive numbers to be added. 


#### File `myfasta.py`

Contains class Fasta - a class that that contains fasta sequences from fasta file and displats some statistics.

If input fasta file contains several sequences with the same names, only one of them will be stored and processed. 

Methods:

count_seqs() - returns the number of sequences in the file
plot_len(save = False, name = './length.png') - plots the figure with disctribution of lengths. If save=True, then also saves the figure, the default name is './length.png'.
gc() - returns a dictionary with sequence names as keys and their GC-content as values. 
gc_average() - returns average GC-content across all sequences 
plot_gc_hist(save = False, name = './gc_hist.png') - lots the figure with disctribution of GC-content. If save=True, then also saves the figure, the default name is './gc_hist.png'.
plot_4mers(self, save = False, name = './4mers.png') - plots the distribution of all the 4mers that are found in the data. If save=True, then also saves the figure, the default name is './4mers.png'.
count_n() - returns dictionary with total number of Ns and the number of sequences that contain Ns (in format {'n':n_count, 'seqs':seq_count})
metrics() - does not return anything, prints Number of sequences, average GC-content, number of N characters, and 3 plots (length distribution, GC-distribition, k-mer distribution).

Attributes:

self.path - path to fasta file
self.seq_dict - dictionary that contains sequence names as keys and sequences as values. 