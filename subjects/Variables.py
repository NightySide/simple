def var(name, value="|", p=None):
    if value=="|":
        p.vars[name] = str(p.buffer)
    else:
        p.vars[name] = str(value)


functions = {"var":var}
