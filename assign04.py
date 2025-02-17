def main():                                                                 # main function to be called exactly once. includes the output format and necessary function calls.
    id = input("Enter student id: ")                                        # takes the Student ID as a string input and stores it into variable "id"
    print("A student of IUT Batch", get_batch(id)+'.')                      
    print("Studying", get_degree(id), "in", get_program(id)+'.')
    print("Section:", get_section(id)+';', "Roll no:", get_roll(id))
    return 0

def get_batch(id):                                                          # takes id and returns the 1st 2 digits (characters)
    return id[:2]

def get_degree(id):                                                         # takes id and returns appropriate degree
    if id[4] == '6':
        return "BBA"
    if id[2:6] == "0031":
        return "DTE"
    degree = "MSc" if id[2] == '1' else "BSc"
    degree += "TE" if id[4] == '3' else "Engg"
    return degree

def get_program(id):                                                        # takes id and return apropriate program
    progs = [
        ["ME", "IPE"],                                                      # 2D list where each row represents a department
        ["EEE"],
        ["What?"],
        ["CSE", "SWE"],
        ["CEE"],
        ["TM"]
    ]
    tech_progs = list("ME EEE Why? CSE".split(" "))                         # special case for technical programs
    return progs[int(id[4])-1][int(id[5])-1] if (id[4]!='3') else tech_progs[int(id[6])-1]

def get_section(id):                                                        # takes id, returns the 3rd last character for section
    return '1' if get_degree(id)[-2:] == "TE" else id[-3]                   # considers the special case for technical programs

def get_roll(id):                                                           # takes id and returns the last 2 characters for roll no
    return id[-2:]

main()                                                                      # initiates the program
