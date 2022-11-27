from memory.register_memory import RVAR

# definiting variabel for register
def DEF(varname, reg):
    RVAR[varname] = int(reg[1:])