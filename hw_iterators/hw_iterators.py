# Iterators homework 

import random

## Task 1

def fasta_iterator(path: str):
    """
    A generator that iterates over sequences in a given file
    """

    with open (path, 'r') as fasta_file:
        # split the file into id+seq ('entry')
        entries = fasta_file.read().split('>')
        for entry in entries:
            if entry != '':
                # the first line is id
                seq_id = entry.split('\n')[0]
                # everything else is sequence
                seq = ('').join(entry.split('\n')[1:])
                yield '> ' + seq_id, seq

# initialize a generator
reader = fasta_iterator('./sequences.fasta')
print(type(reader))

# iterate over sequence id and sequence in './sequences.fasta'
for id_, seq in reader:
    print (id_, seq[:10])

## Task 2

class MutatedFastaIterator:
    """
    A class used to iterate over fasta sequences from a given file

    Takes path to fasta file with aminoasid sequences as an input.
    Iterates over the sequences infinitely.
    Generates sequences with 'mutations':
       - random aminoacid is changed for glycin
       - deletion up to 5 aminoacids is introduced
       
    Attributes
    ----------
    path : str
        path to fasta file
    sequences : list
        list of entries in the fasta file
    length : int
        number of entries in the fasta file

    Methods
    -------
    next()
        Prints the next mutated sequence
    """

    def __init__ (self, path):
        """
        Initializes the object of the class. Accepts path to fasta file.
        """
        
        self.path = path
        self.__cur_index = 0

        # open file for reading
        with open(self.path, 'r') as file:
            self.sequences = file.read().split('>')
            self.length = len(self.sequences)

    def __iter__(self):
        return self

    @staticmethod
    def changed_seq(entry):
        # the first line is id
        seq_id = entry.split('\n')[0]
        # everything else is sequence
        seq = ('').join(entry.split('\n')[1:])
        seq_length = len(seq)
        # generate random index from 0 to seq_length-6
        random_index=random.randrange(seq_length-6)
        # generate number of aminoacid that we want to remove, up to 5
        number_of_aa_deleted = random.randrange(5)
        # delete random number of aa (up to 5) from position random_index
        seq_with_deletion = seq[:random_index]+seq[random_index+number_of_aa_deleted:]
        # select aa index to change for glycin
        random_index2 = random.randrange(len(seq_with_deletion))
        seq_with_mutation_to_glycin = seq_with_deletion[:random_index2]+'G'+seq_with_deletion[random_index2+1:]
        # join sequence id and sequence
        new_entry = '>' + seq_id + '\n' + seq_with_mutation_to_glycin + '\n'
        return new_entry


    def __next__(self):
        """
        Return the next mutated sequence
        """

        self.__cur_index += 1
        # if file is finished, open the file again
        if self.__cur_index >= self.length:
            with open(self.path, 'r') as file:
                self.sequences = file.read().split('>')
                self.length = len(self.sequences)
                self.__cur_index = 1
        seq = self.sequences[self.__cur_index]
        new_seq = self.changed_seq(seq)
        return new_seq

# initialize an object of class MutatedFastaIterator
sequences_fasta_iterator = (MutatedFastaIterator('./sequences.fasta'))
next(sequences_fasta_iterator)