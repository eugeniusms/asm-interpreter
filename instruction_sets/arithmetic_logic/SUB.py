from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Substract without Carry (Rd <- Rd - Rr)
def SUB(rd, rr):
    hasil = LOAD_REGISTER(rd) - LOAD_REGISTER(rr)
    STORE_REGISTER(rd, hasil)