import funcs

class ProgramState:
    def __init__(self):
        self.program = []
        self.line = 0

        self.functions = {}

    def load(self, filename):
        self.program = funcs.readFile(filename)
        self.line = 0
