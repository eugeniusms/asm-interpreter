from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Decrement (Rd <- Rd - 1)
def DEC(rd):
    hasil = LOAD_REGISTER(rd) - 1
    STORE_REGISTER(rd, hasil)