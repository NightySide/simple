
def alias(w1, w2, p):
    """w1 will now be available as w2"""
    p.aliases[w1]=w2
def replace(w1, w2, p):
    """w1 will now be only availlable as w2"""
    if w1 in p.aliases.keys():
        p.aliases[w2] = p.aliases[w1]
        del p.aliases[w1]
def ignore(w, p):
    p.ignore.append(w)
functions = {"~~":alias,"[":replace,"X":ignore}
