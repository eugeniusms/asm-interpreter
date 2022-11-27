# label address ===============================================================
from memory.label_address_memory import SET_LABEL_ADDRESS

# instruction sets ============================================================
# arithmetic logic
from instruction_sets.arithmetic_logic.ADD import ADD
# data transfer
from instruction_sets.data_transfer.LDI import LDI
# directive
from instruction_sets.directive.DEF import DEF
from instruction_sets.directive.INCLUDE import INCLUDE

def execute(line_counter, command_list):
    print(line_counter, command_list) # [DEBUG COMMAND LIST]

    # label address
    if (command_list[0][-1] == ":"):
        label = command_list[0][:-1]
        SET_LABEL_ADDRESS(label, line_counter)
        print("LABELING")

    # arithmetic logic
    elif (command_list[0].upper() == "ADD"):
        ADD(command_list[1], command_list[2])
        print("ADD") # [DEBUG COMMAND]

    # data transfer
    elif (command_list[0].upper() == "LDI"):
        LDI(command_list[1], command_list[2])
        print("LDI")

    # directive
    elif (command_list[0].upper() == ".DEF"):
        DEF(command_list[1], command_list[3])
        print(".DEF")
    elif (command_list[0].upper() == ".INCLUDE"):
        INCLUDE(command_list[1])
        print(".INCLUDE")

    # not found
    else:
        print("command not found")