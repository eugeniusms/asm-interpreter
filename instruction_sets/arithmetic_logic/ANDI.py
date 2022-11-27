from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Logical AND with Immediate (Rd <- Rd and K)
def ANDI(rd, k):
    hasil = LOAD_REGISTER(rd) and int(k)
    STORE_REGISTER(rd, hasil)