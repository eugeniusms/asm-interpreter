# instruction sets
# arithmetic logic
from instruction_sets.arithmetic_logic.ADD import ADD
# data transfer
from instruction_sets.data_transfer.LDI import LDI
# directive
from instruction_sets.directive.INCLUDE import INCLUDE

def execute(command_list):
    print(command_list) # [DEBUG COMMAND LIST]

    # arithmetic logic
    if (command_list[0].upper() == "ADD"):
        ADD(command_list[1], command_list[2])
        print("ADD") # [DEBUG COMMAND]

    # data transfer
    elif (command_list[0].upper() == "LDI"):
        LDI(command_list[1], command_list[2])
        print("LDI")

    # directive
    elif (command_list[0].upper() == ".INCLUDE"):
        INCLUDE(command_list[1])
        print("INCLUDE")

    # not found
    else:
        print("command not found")