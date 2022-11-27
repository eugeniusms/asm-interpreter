from memory.register_memory import STORE_IMMEDIATE

# Load Immediate : Rd <- K
def LDI(rd, k):
    STORE_IMMEDIATE(rd, k)