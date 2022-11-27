from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Logical AND (Rd <- Rd and Rr)
def AND(rd, rr):
    hasil = LOAD_REGISTER(rd) and LOAD_REGISTER(rr)
    STORE_REGISTER(rd, hasil)