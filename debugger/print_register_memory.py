from memory.register_memory import lst

def print_register_memory():
    print("Register Memory:")
    for i in range(0, 32):
        print("r" + str(i) + ": " + str(lst[i]))
    print("")