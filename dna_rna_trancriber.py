# define main function 
def main():
	# in case user has zero idea about what is this file, promts him to use the help message
	print("Type 'help' for more information")


	# starts an infinite loop to take user's orders
	while True: 
		#promts user for command 
		command = input("Enter command: ").replace(" ", "")
		
		#exits if user wants to
		if command == 'exit' or command == 'exit()': 
			print('Good luck!')
			break
			# exits program with exit code "0" (because we chose to exit so everything should be fine) 
			return(0)

		# shows help message
		elif command.casefold() in ['help', '-help', '--help', 'help()']: 
			print(help_message)
			continue

		# checks if the command is valid - if not, promts the user for the command again
		elif command not in ['transcribe', 'reverse', 'complement', 'reversecomplement', 'complementRNA']: 
			print("Invalid command. Valid commands are 'transcribe', 'reverse', 'complement', 'reverse complement', 'complement RNA', 'exit'. Type 'help' for more information")
			continue

		# starts an infinite loop to accept sequence unti it has correct alphabet
		while True:
			# prompts user for sequence. Removes any whitespaces. 
			sequence = input("Enter sequence: ").replace(" ", "")
			if sequence == 'exit' or sequence == 'exit()': 
				break

			# checks sequence correctness - it should be RNA or DNA
			if not check(sequence): 
				print ("Invalid alphabet. Check for 'N's. Try again or type 'exit' to choose a new command")
			else: 
				# executes the chosen command
				if command == 'transcribe': 
					print(transcribe(sequence))
				elif command == 'reverse': 
					print(reverse(sequence))
				elif command == 'complement': 
					print(complement(sequence))
				elif command == 'reversecomplement': 
					print(revcom(sequence))
				elif command == 'complementRNA': 
					print(complementRNA(sequence))
				break

# functions declaration

def transcribe(sequence):
	# replaces Ts for Us case sensitive
	sequence_transcribed = sequence.replace("T", "U").replace("t", "u")
	return(sequence_transcribed)

def reverse(sequence):
	# takes the string in the reverse order
	sequence_reversed = sequence[::-1] 
	return(sequence_reversed)

def complement(sequence):
	# prints a sequence complement to given, uses DNA alphabet by default
	if 'u' in sequence or 'U' in sequence:
		# use U and u as a complement for A and a
		transTable = sequence.maketrans("agcuAGCU", "ucgaUCGA")
		sequence_complement = sequence.translate(transTable)
	else: 
		# uses T and t as a complement for A and a
		transTable = sequence.maketrans("agctAGCT", "tcgaTCGA")
		sequence_complement = sequence.translate(transTable)
	return(sequence_complement)

def revcom(sequence):
	# prints reverse complement of a sequence
	sequence_revcom = reverse(complement(sequence))
	return(sequence_revcom)

def complementRNA(sequence):
	# prints complement of a sequence, using 'U' as a complement of 'A'
	transTable = sequence.maketrans("agcutAGCUT", "ucgaaUCGAA")
	sequence_RNAcomplement = sequence.translate(transTable)
	return(sequence_RNAcomplement)

def check(sequence):
	# checks that sequence contains only letters found in DNA or RNA alphabets
	dna_alphabet = {'a', 't', 'g', 'c'}
	rna_alphabet = {'a', 'u', 'g', 'c'}
	sequence_alphabet = set(sequence.casefold())
	if sequence_alphabet.issubset(dna_alphabet) or sequence_alphabet.issubset(rna_alphabet):
		return(True)
	else:
		return(False)

help_message = '''
This is a program that works with sequences of nucleic acids. It was created as a homework for python course in Bioinformatics institute 2021.
Commands:

exit - exits the program 
help - prints this help message and waits for the next command
trancribe - prints the transcribed coding string of DNA to RNA 
(so it will give the same string but with all 'T' replaced by 'U'). 
Example: ATGCA -> AUGCA
reverse - prints the reversed sequence 
Example: ATGCA -> ACGTA
complement - prints the complement sequence 
If the sequence can be either DNA or RNA (e. g. "AGGGCCCA"), the complement string is generated as DNA (e. g. "TCCCGGGA" and not "UCCCGGGA")
If you want to get complement of an RNA string that does not contain uracil, use 'complement RNA'
Example: ATGCA -> TACGT
reverse complement - prints reverse complement sequence. 
If the sequence can be either DNA or RNA, the reverse complement string is generated as DNA
Example: ATGCA -> TGCAT
complement RNA - prints complement sequence, forced to use 'U' as a complement of 'A' 
Example: AGGGCCCA -> UCCCGGGA
The program preserves the case (e. g. complement from 'AtGc' will be 'TaCg')
The program will correct the user that tries to use the sequence with incorrect alphabet (e.g. 'ATGCP' or 'GttCU'). The use of 'N' or white spaces is not supported!

'''
# call main function so it's exited
main()