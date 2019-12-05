import math

def parser(opcode_list_r, input_var):
    PC = 0
    opcode = opcode_list_r[PC]
    output_var = None
    while(opcode != 99):
        if str(opcode)[-2:] == '01':
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC + 1]], opcode_list[opcode_list[PC + 2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] + opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 4
            except:
                return [0]
        if str(opcode)[-2:] == '02':
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] * opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 4
            except:
                return [0]
        if str(opcode)[-2:] == '03':
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                opcode_list_r[opcode_list_r[PC + 1]] = input_var
            except:
                return [0]
        if str(opcode)[-2:] == '04':
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                output_var = opcode_list_r[opcode_list_r[PC + 1]]
                print(output_var)
            except:
                return [0]
        opcode = opcode_list_r[PC]
        #print(opcode, opcode_list)
    return opcode_list_r


def main():
    with open("input2") as input:
        opcode_list = list(map(int, str(input.readline()).split(",")))
        size = len(opcode_list)
    out = parser(opcode_list, 1)


if __name__ == "__main__":
    main()