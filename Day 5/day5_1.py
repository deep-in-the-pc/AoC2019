import math

def parser(opcode_list_r):
    PC = 0
    opcode = opcode_list_r[PC]
    while(opcode != 99):
        if opcode == 1:
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC + 1]], opcode_list[opcode_list[PC + 2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] + opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 4
            except:
                return [0]
        if opcode == 2:
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] * opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 4
            except:
                return [0]
        if opcode == 3:
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] * opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 3
            except:
                return [0]
        if opcode == 3:
            #print(opcode_list[PC + 3], opcode_list[opcode_list[PC+1]], opcode_list[opcode_list[PC+2]])
            try:
                opcode_list_r[opcode_list_r[PC + 3]] = opcode_list_r[opcode_list_r[PC+1]] * opcode_list_r[opcode_list_r[PC+2]]
                PC = PC + 3
            except:
                return [0]
        opcode = opcode_list_r[PC]
        #print(opcode, opcode_list)
    return opcode_list_r


def main():
    with open("input2") as input:
        opcode_list = list(map(int, str(input.readline()).split(",")))
        size = len(opcode_list)
    for i in range(0, size):
        for n in range(0, size):
            with open("input2") as input:
                opcode_list = list(map(int, str(input.readline()).split(",")))
                opcode_list[1] = n
                opcode_list[2] = i
                out = parser(opcode_list)
                #print(n, i, out)
                if out[0] == 19690720:
                        print(100 * n + i)
                        return 1

if __name__ == "__main__":
    main()