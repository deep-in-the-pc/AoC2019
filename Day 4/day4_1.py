import math

def checkAdjacent(n):
    adj2 = False
    seq = False
    sn = str(n)
    for i in range(5):
        if sn[i] == sn[i+1]:
            if not seq:
                seq = True
                adj2 = True
            else:
                adj2 = False
        else:
            if adj2:
                break
            seq = False


    return adj2

def checkIncreasing(n):
    inc = True
    sn = str(n)
    for i in range(5):
        if sn[i] > sn[i+1]:
            inc = False
            break
    return inc

def main():
    input_range = range(134564, 585159)
    count = 0
    for n in input_range:
        if checkAdjacent(n) and checkIncreasing(n):
            count = count + 1
    print("Valid pw:",count)



if __name__ == "__main__":
    main()