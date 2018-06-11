import ProgramState
from funcs import next_line
import importlib


def use(*name, p): #import a module, and load references to use it
    #print(name)
    new_module = importlib.import_module(name[0])
    p.functions.update(new_module.functions)

functions = {"use" : use}

ps = ProgramState.ProgramState()
ps.load("test.smp")
ps.functions.update(functions)
while ps.line < len(ps.program):
    next_line(ps)
