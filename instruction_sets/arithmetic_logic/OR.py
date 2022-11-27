from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Logical OR (Rd <- Rd or Rr)
def OR(rd, rr):
    hasil = LOAD_REGISTER(rd) or LOAD_REGISTER(rr)
    STORE_REGISTER(rd, hasil)