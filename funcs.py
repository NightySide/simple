def readFile(name):
    with open(name, 'r') as f:
        content = f.read().strip()
        content = content.replace('|', '\n')
        program = content.split('\n')
        program = list(filter(len, program))
        program = list(map(str.strip, program))

    return program

def next_line(ps):
    current_line = ps.program[ps.line]
    print("Processing line |{}".format(current_line))

    current_line = current_line.split()
    if current_line[0] in ps.functions.keys() :
        ps.functions[current_line[0]](*current_line[1:],p = ps)
    ps.line+=1
