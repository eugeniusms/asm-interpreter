# label address {label: line_in_program}
LABEL_ADDRESS = {}

def SET_LABEL_ADDRESS(label, line):
    LABEL_ADDRESS[label] = line

def GET_LABEL_ADDRESS(label):
    return LABEL_ADDRESS[label]