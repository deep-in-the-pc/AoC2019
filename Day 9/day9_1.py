import math
from itertools import permutations

def parser(opcode_list_r, PC, input_var):
    sendOutput = 0
    opcode = opcode_list_r[PC]
    relative_base = 0
    reset = 0
    sizeofopcode = len(opcode_list_r)
    while(opcode != 99):
        #print(opcode, PC, input_var, opcode_list_r)
        if opcode%100 == 1:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]
                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]
                if opcode > 10000 and str(opcode)[-5] == '2':
                    A = relative_base + opcode_list_r[PC + 3]
                else:
                    A = opcode_list_r[PC + 3]

                #print("ADDRESS: ", A, "C: ", C, "B: ", B)

                if(A>=sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1+A-sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                opcode_list_r[A] = C + B
                PC = PC + 4
            except:
                return [0]

        if opcode%100 == 2:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if opcode > 10000 and str(opcode)[-5] == '2':
                    A = relative_base + opcode_list_r[PC + 3]
                else:
                    A = opcode_list_r[PC + 3]
                    
                #print("ADDRESS: ", A, "C: ", C, "B: ", B)

                if (A >= sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1 + A - sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                opcode_list_r[A] = C * B
                PC = PC + 4
            except:
                return [0]

        if opcode%100 == 3:

            try:

                if opcode > 100 and str(opcode)[-3] == '2':

                    C = relative_base + opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[PC + 1]


                #print("ADDRESS: ", C)

                if(C>=sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1+C-sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                opcode_list_r[C] = input_var[0]


                #print(opcode_list_r[C])

                PC = PC + 2
            except:
                return [0]

        if opcode%100 == 4:
            try:

                if opcode > 100 and str(opcode)[-3] == '2':
                    C = relative_base + opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[PC + 1]

                # print("ADDRESS: ", C)

                if(C>=sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1+C-sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                output_var = opcode_list_r[C]

                PC = PC + 2

                print(output_var)
            except:
                return [0]

        if opcode%100 == 5:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]


                # print("C: ", C, "B: ", B)

                if C != 0:
                    PC = B
                else:
                    PC = PC + 3
            except:
                return [0]

        if opcode%100 == 6:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                # print("C: ", C, "B: ", B)

                if C == 0:
                    PC = B
                else:
                    PC = PC + 3

            except:
                return [0]

        if opcode%100 == 7:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if opcode > 10000 and str(opcode)[-5] == '2':
                    A = relative_base + opcode_list_r[PC + 3]
                else:
                    A = opcode_list_r[PC + 3]

                #print("ADDRESS: ", A, "C: ", C, "B: ", B)

                if (A >= sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1 + A - sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                if C < B:
                    opcode_list_r[A] = 1
                else:
                    opcode_list_r[A] = 0
                PC = PC + 4
            except:
                return [0]

        if opcode%100 == 8:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                if opcode > 1000 and str(opcode)[-4] == '2':
                    B = opcode_list_r[relative_base + opcode_list_r[PC + 2]]
                elif opcode > 1000 and str(opcode)[-4] == '1':
                    B = opcode_list_r[PC + 2]
                else:
                    B = opcode_list_r[opcode_list_r[PC + 2]]

                if opcode > 10000 and str(opcode)[-5] == '2':
                    A = relative_base + opcode_list_r[PC + 3]
                else:
                    A = opcode_list_r[PC + 3]

                # print("ADDRESS: ", A, "C: ", C, "B: ", B)

                if (A >= sizeofopcode):
                    opcode_list_r.extend([0 for x in range(1 + A - sizeofopcode)])
                    sizeofopcode = len(opcode_list_r)

                if C == B:
                    opcode_list_r[A] = 1
                else:
                    opcode_list_r[A] = 0
                PC = PC + 4
            except:
                return [0]

        if opcode%100 == 9:
            try:
                if opcode > 100 and str(opcode)[-3] == '2':
                    C = opcode_list_r[relative_base + opcode_list_r[PC + 1]]
                elif opcode > 100 and str(opcode)[-3] == '1':
                    C = opcode_list_r[PC + 1]
                else:
                    C = opcode_list_r[opcode_list_r[PC + 1]]

                # print("C: ", C)

                relative_base = relative_base + C

                PC = PC + 2

            except:
                return [0]

        opcode = opcode_list_r[PC]
    return opcode_list_r, -1, output_var


def main():
    with open("input9") as input:
        opcode_list_og = list(map(int, str(input.readline()).split(",")))

        opcode_list = opcode_list_og[:]

        opcode_list, PC, ov = parser(opcode_list, 0, (1, 0))

        opcode_list = opcode_list_og[:]

        opcode_list, PC, ov = parser(opcode_list, 0, (2, 0))




if __name__ == "__main__":
    main()