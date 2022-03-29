# Iterators homework

## Description

These generator function 'fasta_iterator' and iterator class 'MutatedFastaIterator' were created as part of the python course at [Bioinformatics institute](https://bioinf.me/en/education/) (Bioinformatics for biologists, online, 2021-2022). 

They are contained in `hw_iterators.py` file and Jupyter notebook `Iterators.ipynb`. 


## Installation

The class `MutatedFastaIterator` can be imported in the code via `from hw_iterators.py import MutatedFastaIterator` , given that `hw_iterators.py` file is in the same directoty as your script. Alternatively, you can just copy and paste the class definition and function definition in your code.

The only library used by 'MutatedFastaIterator' is `random`, you do not need to install it. 'fasta_iterator' does not use any libraries at all. 

## Files description

#### File `hw_iterators.py`

Contains the definition of class `MutatedFastaIterator`, a class used to iterate over fasta sequences from a given file.

    Takes path to fasta file with aminoasid sequences as an input.
    Iterates over the sequences infinitely.
    Generates sequences with 'mutations':
       - random aminoacid is changed for glycin
       - deletion up to 5 aminoacids is introduced

Attributes
    path : str
        path to fasta file
    sequences : list
        list of entries in the fasta file
    length : int
        number of entries in the fasta file

Methods

    next()
        Prints the next mutated sequence

Also contains generator function `fasta_iterator`, a generator that iterates over aminoacid sequences in a given file. 


#### File `Iterators.ipynb`

Contains the same class and generator, with the task description. 


#### File `sequences.fasta` 

Example aminoacid sequences in fasta format from the task description, provided by class instructors.