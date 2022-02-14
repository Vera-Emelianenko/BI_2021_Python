import seaborn as sns
import matplotlib.pyplot as plt

class Fasta():
    
    """A class that that collects some statistics from fasta file"""
    
    def __init__ (self, path):
        self.path = path
        self.seq_dict = {}
        counter = 0
        with open (path) as file:
            
            for line in file:
                counter += 1
                line = line.strip()
                if line == '':
                    pass
                if line.startswith('>'):
                    if counter > 1:
                        self.seq_dict[name] = seq
                        seq = ''
                        name = line[1:]
                    else:
                        seq = ''
                        name = line[1:]
                else:
                    seq = seq + line
        self.seq_dict[name] = seq
           
    def count_seqs(self):
        return len(self.seq_dict)
        
    def plot_len(self, save = False, name = './length.png'):
        lengths = [len(value) for value in self.seq_dict.values()]
        ax = sns.histplot(x=lengths, kde=True)
        ax.set(xlabel='length', title='Length histogram')
        if save == True:
            plt.savefig(fname = name, bbox_inches='tight')
        plt.show()
        plt.close()

    def gc(self):
        try:
            self.gc_dict
            return (self.gc_dict)
        except AttributeError:
            self.gc_dict = {}
            for key, value in self.seq_dict.items():
                seq = value.casefold()
                gc_all = seq.count('g')+seq.count('c')
                atgc_all = seq.count('g')+seq.count('c')+seq.count('a')+seq.count('t')
                gc_content = gc_all/atgc_all
                self.gc_dict[key] = gc_content
            return self.gc_dict
        
    def gc_average(self):
        self.gc()
        average = sum (self.gc_dict.values()) / len (self.seq_dict)
        return average
    
    def plot_gc_hist(self, save = False, name = './gc_hist.png'):
        self.gc()
        gc_values = [value for key, value in self.gc_dict.items()]
        ax = sns.histplot(x=gc_values, kde=True)
        ax.set(xlabel='GC-content', title='GC-content histogram')
        if save == True:
            plt.savefig(fname = name, bbox_inches='tight')
        plt.show()
        plt.close()

    def plot_4mers(self, save = False, name = './4mers.png'):
        try:
            self.k_mers_dict
        except AttributeError:
            self.k_mers_dict = {}
            for seq in self.seq_dict.values():
                for i in range (len(seq)-3):
                    kmer = seq[i:i+4]
                    if kmer not in self.k_mers_dict:
                        self.k_mers_dict[kmer] = 1
                    else:
                        self.k_mers_dict[kmer] +=1
            self.k_mers_dict = dict(sorted(self.k_mers_dict.items(), key=lambda item: item[1], reverse = True))
        k_mer_names = list(self.k_mers_dict.keys())
        k_mer_counts = list(self.k_mers_dict.values())
        sum_of_counts = sum(k_mer_counts)
        count_fraction = [k_mer_count/sum_of_counts for k_mer_count in k_mer_counts]
        
        plt.figure(figsize=(40,12))
        ax = sns.barplot(x=k_mer_names, y=count_fraction)
        
        for item in ([ax.xaxis.label] + ax.get_xticklabels()):
            item.set_fontsize(7)
            
        for item in ([ax.yaxis.label] + ax.get_yticklabels()):
            item.set_fontsize(40)

        plt.title('4-mer frequency', fontdict = {'fontsize' : 50})
        plt.xticks(rotation=90)
        ax.set(xlabel='k-mers in this fasta file')
        
        if save == True:
            plt.savefig(fname = name, bbox_inches='tight')
            
        plt.show()
        plt.close()
        
        
    def count_n(self):
        n_count = 0
        seq_count = 0
        for seq in self.seq_dict.values(): 
            n = seq.casefold().count('n')
            if n > 0: 
                n_count += n
                seq_count +=1
        n_count_dict = {}
        n_count_dict['n'] = n_count
        n_count_dict['seqs'] = seq_count
        return n_count_dict
    
    def metrics(self):
        print ('Number of sequences: ', self.count_seqs())
        print ('Average GC-content: ', self.gc_average())
        print (f"{self.count_n()['seqs']} sequences contating 'N' characters, {self.count_n()['n']} 'N' characters in total")
        self.plot_len()
        self.plot_gc_hist()
        self.plot_4mers()
    
        
    def __repr__(self):
        return self.path
    
    def __str__(self):
        return f"{self.count_seqs()} sequences from file {self.path}"