from memory.register_memory import STORE_REGISTER, LOAD_REGISTER

# Logical OR with Immediate (Rd <- Rd or K)
def ORI(rd, k):
    hasil = LOAD_REGISTER(rd) or int(k)
    STORE_REGISTER(rd, hasil)