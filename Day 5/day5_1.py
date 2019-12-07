import math

def parser(opcode_list_r, input_var):
    PC = 0
    opcode = opcode_list_r[PC]
    output_var = None
    while(opcode != 99):
        if opcode%100 == 1:
            try:
                if opcode>100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC+1]
                else:
                    C = opcode_list_r[opcode_list_r[PC+1]]

                if opcode>1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC+2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]
                opcode_list_r[opcode_list_r[PC + 3]] = C + B
                PC = PC + 4
            except:
                return [0]
        if opcode%100 == 2:
            try:
                if opcode>100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC+1]
                else:
                    C = opcode_list_r[opcode_list_r[PC+1]]

                if opcode>1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC+2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]
                opcode_list_r[opcode_list_r[PC + 3]] = C * B
                PC = PC + 4
            except:
                return [0]
        if opcode%100 == 3:
            try:
                opcode_list_r[opcode_list_r[PC + 1]] = input_var
                PC = PC + 2
            except:
                return [0]
        if opcode%100 == 4:
            try:
                output_var = opcode_list_r[opcode_list_r[PC + 1]]
                PC = PC + 2
                print(output_var)
            except:
                return [0]
        if opcode%100 == 5:
            try:
                if opcode>100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC+1]
                else:
                    C = opcode_list_r[opcode_list_r[PC+1]]

                if opcode>1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC+2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if C != 0:
                    PC = B
                else:
                    PC = PC + 3
            except:
                return [0]
        if opcode%100 == 6:
            try:
                if opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if C == 0:
                    PC = B
                else:
                    PC = PC + 3
            except:
                return [0]
        if opcode%100 == 7:
            try:
                if opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if C < B:
                    opcode_list_r[opcode_list_r[PC + 3]] = 1
                else:
                    opcode_list_r[opcode_list_r[PC + 3]] = 0
                PC = PC + 4
            except:
                return [0]
        if opcode%100 == 8:
            try:
                if opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if C == B:
                    opcode_list_r[opcode_list_r[PC + 3]] = 1
                else:
                    opcode_list_r[opcode_list_r[PC + 3]] = 0
                PC = PC + 4
            except:
                return [0]

        opcode = opcode_list_r[PC]
    return opcode_list_r


def main():
    with open("input5") as input:
        opcode_list = list(map(int, str(input.readline()).split(",")))
        size = len(opcode_list)
    parser(opcode_list, 5)
if __name__ == "__main__":
    main()