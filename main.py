import ProgramState
from funcs import next_line

ps = ProgramState.ProgramState()
ps.load("test.smp")

while ps.line < len(ps.program):
    next_line(ps)

print(ps)
