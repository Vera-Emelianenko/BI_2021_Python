class BacterialChromosome:
    
    """An example class to contain info about bacterial chromosome and print it out"""
    
    def __init__(self, chromosome_id, organism_name = 'unknown', length = 0, sequence = ''):
        self.chromosome_id = chromosome_id
        self.organism_name = organism_name
        self.length = length
        self.sequence = sequence
    
    def print_sequence(self):
        """print out the sequence"""
        if self.sequence == '':
            print ('No sequence')
        else:
            print (self.sequence)
    
    def print_info (self):
        """print out chromosome_id, organism and length"""
        print (f'chromosome id: {self.chromosome_id} \nOrganism: {self.organism_name} \nlength: {self.length}')  
    
    @classmethod
    def from_gbff(cls, path_to_file): 
        """get chromosome id, organism name and sequence length from GB file. 
        Only the first record in gb file will be processed!"""
        with open(path_to_file) as file:
            for line in file: 
                if 'LOCUS' in line: 
                    length = line.split()[2]
                    break
            for line in file:
                if 'ACCESSION' in line:
                    chromosome_id = line.split()[1]
                    break
            for line in file:
                if 'ORGANISM' in line: 
                    organism_name = ' '.join (line.split()[1:])
                    break

                    
        return cls(chromosome_id, organism_name, length)