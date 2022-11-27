from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Substract without Carry (Rd <- Rd - K)
def SUBI(rd, k):
    hasil = LOAD_REGISTER(rd) - int(k)
    STORE_REGISTER(rd, hasil)