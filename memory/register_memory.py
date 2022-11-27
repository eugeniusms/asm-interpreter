# register r0-r31
R = [0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0] 

# variable register {varname: register}
RVAR = {
    "XL": 26,
    "XH": 27,
    "YL": 28,
    "YH": 29,
    "ZL": 30,
    "ZH": 31,
}
        
def STORE_REGISTER(reg, value):
    index = int(reg[1:])
    R[index] = value

def LOAD_REGISTER(reg):
    index = int(reg[1:])
    return R[index]

def STORE_IMMEDIATE(reg, value):
    R[int(reg[1:])] = int(value)