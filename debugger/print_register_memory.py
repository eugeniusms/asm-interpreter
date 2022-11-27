from memory.register_memory import R

def print_register_memory():
    print("=====================================")
    print("Register Memory")
    print("=====================================")
    for i in range(0, 32):
        if (i % 2 == 1):
            prt = "R" + str("%02d" % i) + ": " + str(R[i])
            print(prt.ljust(16, ' '))
        else:
            prt = "R" + str("%02d" % i) + ": " + str(R[i])
            print(prt.ljust(16, ' '), end = " ")
    print("=====================================")