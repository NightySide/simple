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
    #print("Processing line |{}".format(current_line))

    current_line, raw_text = separate_string(current_line)



    #put back string
    current_line = current_line.replace('|',"{}").format(*raw_text)

    current_line = current_line.split()
    if current_line[0] in ps.functions.keys() :
        ps.functions[current_line[0]](*current_line[1:],p = ps)
    else :
        print("unknown command : {}".format(current_line[0]))
    ps.line+=1

def separate_string(line):
    line = line.split('"')
    raw_text = line[1::2]
    #print("quotings : {}".format(raw_text))

    line = '|'.join(line[::2])
    #print("un-quoted line : {}".format(line))

    return (line, raw_text)
