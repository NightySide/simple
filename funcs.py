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

    current_line, raw_text = separateString(current_line)

    aliases_keys = list(ps.aliases.keys())
    aliases_keys.sort(key = lambda s: -len(s))
    executable = False

    if aliases_keys is not None :
        totally_replaced = False
        while not totally_replaced :
            totally_replaced = True
            for alias in aliases_keys:
                if alias in current_line :
                    #print("Found :",alias,"replacing with :",ps.aliases[alias])
                    if current_line.index(alias) == 0:
                        executable = True
                    current_line = current_line.replace(alias, ps.aliases[alias])
                    totally_replaced = False
                    if alias == ps.aliases[alias]:
                        #print("Removing (temporarely) the alias",alias)
                        aliases_keys.remove(alias)
                        break


    current_line = current_line.replace("buffer", str(ps.buffer))
    for k,v in ps.vars.items():
        current_line = current_line.replace(k,v)
        #print("alias replaced -> {}".format(current_line))

    #put back strings
    current_line = current_line.replace(" ",'"')
    current_line = current_line.replace('|','{}').format(*raw_text)

    current_line = current_line.split('"')
    if executable and current_line[0] in ps.functions.keys():
        ps.functions[current_line[0]](*current_line[1:],p = ps)
    else :
        print("unknown command : {}".format(current_line[0]))
    ps.line+=1

def separateString(line):
    line = line.split('"')
    raw_text = line[1::2]
    #print("quotings : {}".format(raw_text))

    line = '|'.join(line[::2])
    #print("un-quoted line : {}".format(line))

    return (line, raw_text)
