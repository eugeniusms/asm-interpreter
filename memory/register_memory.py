lst = [0, 7, 0, 0, 0,
       0, 0, 0, 0, 0,
       0, 0, 0, 0, 0,
       0, 0, 0, 0, 0,
       0, 0, 0, 0, 0,
       0, 0, 0, 0, 0,
       0, 0] # register r0-r31
        
def store(reg, value):
    index = int(reg[1:])
    lst[index] = value

def load(reg):
    index = int(reg[1:])
    return lst[index]