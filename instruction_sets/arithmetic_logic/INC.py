from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Increment (Rd <- Rd + 1)
def INC(rd):
    hasil = LOAD_REGISTER(rd) + 1
    STORE_REGISTER(rd, hasil)