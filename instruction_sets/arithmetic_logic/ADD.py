from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# add without carry (Rd <- Rd + Rr)
def ADD(rd, rr):
    hasil = LOAD_REGISTER(rd) + LOAD_REGISTER(rr)
    STORE_REGISTER(rd, hasil)