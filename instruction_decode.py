# instruction sets
from instruction_sets.arithmetic_logic.ADD import ADD

def decode(line):
    if (line == ""): # saat line kosong
        return None
    else:
        # split line
        command_list = split_command(line)
        print(command_list) # [DEBUG COMMAND LIST]

    # ADD("r0", "r1")

# GET command list in a line of code
def split_command(line):
    command_list = []
    command = ""
    for ch in line:
        # saat bertemu comment (skip comment)
        if (ch == "/"):
            break

        # saat bertemu spasi atau tab
        if (ch == " " or ch == "\t"):
            if (command != ""):
                # saat ada komanya jangan ditambahin
                if (command[-1] == ","):
                    command = command[:-1]
                command_list.append(command)
            command = "" # reset command

        # saat bertemu command biasa
        else:
            command += ch
    
    if (command != ""): # saat tidak ada kelebihan spasi
        command_list.append(command)

    return command_list
