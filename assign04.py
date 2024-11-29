def main():
    id = input("Enter student id: ")
    print("A student of IUT Batch", get_batch(id)+'.')
    print("Studying", get_degree(id), "in", get_program(id)+'.')
    print("Section:", get_section(id)+';', "Roll no:", get_roll(id))
    return 0

def get_batch(id):
    return id[:2]

def get_degree(id):
    if id[4] == '6':
        return "BBA"
    if id[2:6] == "0031":
        return "DTE"
    degree = "MSc" if id[2] == '1' else "BSc"
    degree += "TE" if id[4] == '3' else "Engg"
    return degree

def get_program(id):
    progs = [
        ["ME", "IPE"],
        ["EEE"],
        ["What?"],
        ["CSE", "SWE"],
        ["CEE"],
        ["TM"]
    ]
    tech_progs = list("ME EEE Why? CSE".split(" "))
    return progs[int(id[4])-1][int(id[5])-1] if (id[4]!='3') else tech_progs[int(id[6])-1]

def get_section(id):
    return '1' if get_degree(id)[-2:] == "TE" else id[-3]

def get_roll(id):
    return id[-2:]

main()
