import funcs
import importlib

def use(*name, p): #import a module, and load references to use it
    #print(name)
    new_module = importlib.import_module(name[0])
    p.functions.update(new_module.functions)

class ProgramState:
    def __init__(self):
        self.program = []
        self.line = 0

        self.functions = {"use":use}
        self.aliases = {"use":"use"}
    def generate_aliases(dict):
        for w in dict.keys():
            self.aliases[w]=w
    def load(self, filename):
        self.program = funcs.readFile(filename)
        self.line = 0

    def __repr__(self):
        n = "\n"
        r = "----Program State----\n"
        r += "program length : "+str(len(self.program))+n
        r += "aliases table : "+str(self.aliases)+n
        r += "available functions : "+str(list(self.functions.keys()))
        return r
