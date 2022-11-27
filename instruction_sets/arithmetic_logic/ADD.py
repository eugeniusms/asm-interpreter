from memory.register_memory import store, load

# add without carry (Rd <- Rd + Rr)
def ADD(rd, rr):
    hasil = load(rd) + load(rr)
    store(rd, hasil)
    
