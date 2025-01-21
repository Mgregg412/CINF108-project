import random
import art

### names from file
def file_1(names):
    with open("names.txt", 'r') as file:
        ## Make into list NOT dict
        names = [line.strip() for line in file.readlines()]
        return names

def extra_lab_conch(names, names2):
    ###RANDOMIZER
    chosen_names = random.sample(names, names2)
#### SHELLS
    shells = "\U0001F41A" * 125
### Art emojie
    art.tprint(shells)
    print(shells)

    for name in chosen_names:
        shells += f"{name} \n"
        # {name}
        # shells

### Art emojie
    art.tprint(shells)
    print(shells)
    
def main_input():
    # Load names from a text file
    names = file_1("names.txt")
    chosen_number = int(input("Choose any number of names less than your file number: "))
    extra_lab_conch(names, chosen_number)

if __name__ == "__main__":
    main_input()