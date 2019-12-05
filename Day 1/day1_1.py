import math

def traceWire(map, wire):
    position = {'x': 0, 'y': 0}
    for line in wire:
        if line[0] == 'R':
            for i in range(position['x'], int(line[1:])):
                if (position['x'], position['x']) in map:
                    map[(position['x'], position['x'])] = map[(position['x'], position['x'])] + 1
                else:
                    map[(position['x'], position['x'])]
        elif line[0] == 'L':
            for i in range(position['x']-int(line[1:]), position['x']):
        elif line[0] == 'U':

        elif line[0] == 'D':


def main():
    total = 0
    input = open("input1.txt")
    for line in input:
        if (line != ''):
            print(line)
            total = total + findFuel(int(line))
    print("Total " + str(total))

if __name__ == "__main__":
    main()