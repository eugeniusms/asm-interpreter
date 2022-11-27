# instruction sets
# arithmetic logic
from instruction_sets.arithmetic_logic.ADD import ADD
# data transfer
from instruction_sets.data_transfer.LDI import LDI

def execute(command_list):
    if (command_list[0].upper() == "ADD"):
        ADD(command_list[1], command_list[2])
        print("ADD") # [DEBUG COMMAND]
    elif (command_list[0].upper() == "LDI"):
        LDI(command_list[1], command_list[2])
        print("LDI")
    else:
        print("command not found")