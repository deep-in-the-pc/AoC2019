import math
from itertools import permutations

def parser(opcode_list_r, PC, input_var):
    sendOutput = 0
    opcode = opcode_list_r[PC]
    reset = 0
    while(opcode != 99):
        #print(opcode, PC, input_var, opcode_list_r)
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
            if reset:
                #print('reset at ', PC, output_var)
                return opcode_list_r, PC, output_var
            try:

                if PC==0:
                    opcode_list_r[opcode_list_r[PC + 1]] = input_var[0]
                else:
                    reset = 1
                    opcode_list_r[opcode_list_r[PC + 1]] = input_var[1]


                PC = PC + 2
            except:
                return [0]
        if opcode%100 == 4:
            try:
                output_var = opcode_list_r[opcode_list_r[PC + 1]]
                PC = PC + 2
                #print(output_var)
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
    return opcode_list_r, -1, output_var


def main():
    with open("input7") as input:
        opcode_list = list(map(int, str(input.readline()).split(",")))
        size = len(opcode_list)

    highest_sig = 0
    # for sequence in permutations(range(5, 10)):
    #     ov = 0
    #     for n in range(5):
    #         opcode_list, ov = parser(opcode_list, sequence[n], output_var=ov)
    #     for n in range(100):
    #         opcode_list, ov = parser(opcode_list, ov, output_var=ov)
    #         print(opcode_list, ov)
    #     if ov>highest_sig:
    #         print(sequence, ov)
    #         highest_sig = ov
    # print(highest_sig)
    for sequence in permutations(range(5, 10)):
        ov = 0
        PC1 = 0
        PC2 = 0
        PC3 = 0
        PC4 = 0
        PC5 = 0

        opcode_list_r_1 = opcode_list[:]
        opcode_list_r_2 = opcode_list[:]
        opcode_list_r_3 = opcode_list[:]
        opcode_list_r_4 = opcode_list[:]
        opcode_list_r_5 = opcode_list[:]
        ov5 = 0
        while (PC5 != -1):
            opcode_list_r_1, PC1, ov1 = parser(opcode_list_r_1, PC1, (sequence[0], ov5))
            opcode_list_r_2, PC2, ov2 = parser(opcode_list_r_2, PC2, (sequence[1], ov1))
            opcode_list_r_3, PC3, ov3 = parser(opcode_list_r_3, PC3, (sequence[2], ov2))
            opcode_list_r_4, PC4, ov4 = parser(opcode_list_r_4, PC4, (sequence[3], ov3))
            opcode_list_r_5, PC5, ov5 = parser(opcode_list_r_5, PC5, (sequence[4], ov4))
        if ov5>highest_sig:
            print(sequence, ov5)
            highest_sig = ov5

    print("Highest Value:", highest_sig)




if __name__ == "__main__":
    main()