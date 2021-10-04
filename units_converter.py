help_message = '''
This program converts some volume units to cubic metre. 
'''
invalid_unit_message = '''
Invalid units. Try using 'dm3', 'cm3', 'mm3', 'L', 'mL'
'''
valid_units_dict = {'dm3':0.001, 'cm3':0.001*0.001, 'mm3':0.001*0.001*0.001, 'L':0.001, 'mL':0.001*0.001}

# define main function
def main():
    # in case user has zero idea about what is this file, promts him to use the help message
    print("Type 'help' for more information. Type 'exit' to finish the program")

    # starts an infinite loop to take user's orders
    while True:
        # promts user for command
        command = input("Enter number and units, separated by whitespace: ")

        # exits if user wants to
        if command.replace(" ", "") == 'exit' or command.replace(" ", "") == 'exit()':
            print('Good luck!')
            break
            # exits program with exit code "0" (because we chose to exit so everything should be fine)
            return(0)

        # shows help message
        elif command.casefold() in ['help', '-help', '--help', 'help()']:
            print(help_message)
            continue

        # checks if the command is valid - if not, promts the user for the command again
        elif command.split()[-1] not in valid_units_dict:
            print(invalid_unit_message)
            continue

        else:
            number_in_metres = valid_units_dict[command.split()[1]]*float(command.split()[0])
            print (str (number_in_metres) + 'm3')


# call main function so it's executed
main()
