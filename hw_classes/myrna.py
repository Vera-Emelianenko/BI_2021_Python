from Bio.Seq import Seq


class MyRNA:

    """A class that describes RNA,
    with traslation method and reverse transcription method"""

    def __init__(self, sequence=''):
        rna_alphabet = ['A'.casefold(), 'U'.casefold(), 'G'.casefold(), 'C'.casefold()]
        for character in sequence:
            if character.casefold() not in rna_alphabet:
                raise Exception('not an RNA string')
        self.sequence = sequence

    def translate(self):

        """Traslation method - returns a protein string using standard genetic code"""

        my_rna = Seq(self.sequence)
        my_aa = str(my_rna.translate())
        return my_aa
 
    def back_transcribe(self):

        """Reverse transcription method - returns a DNA string that corresponds to this RNA"""

        my_dna = self.sequence.replace('U', 'T')
        return (my_dna)
