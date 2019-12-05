import math

def traceWire(map, wire, n):
    position = {'x': 0, 'y': 0}
    steps = 0
    for line in wire:
        print(position)
        if line[0] == 'R':
            for i in range(position['x']+1, position['x'] + int(line[1:])+1):
                position['x'] = i
                steps += 1
                if (position['x'], position['y']) in map and map[(position['x'], position['y'])] != n:
                    map[(position['x'], position['y'])]['val'] = map[(position['x'], position['y'])]['val'] + n
                    map[(position['x'], position['y'])]['steps'][n] = steps
                else:
                    if n == 1:
                        map[(position['x'], position['y'])] = {'val': n, 'steps':{1: steps}}
                    if n == 2:
                        map[(position['x'], position['y'])] = {'val': n, 'steps':{2: steps}}
        elif line[0] == 'L':
            for i in range(position['x']-1, position['x'] - int(line[1:])-1, -1):
                position['x'] = i
                steps += 1
                if (position['x'], position['y']) in map and map[(position['x'], position['y'])] != n:
                    map[(position['x'], position['y'])]['val'] = map[(position['x'], position['y'])]['val'] + n
                    map[(position['x'], position['y'])]['steps'][n] = steps
                else:
                    if n == 1:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {1: steps}}
                    if n == 2:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {2: steps}}
        elif line[0] == 'U':
            for i in range(position['y']+1, position['y'] + int(line[1:])+1):
                position['y'] = i
                steps += 1
                if (position['x'], position['y']) in map and map[(position['x'], position['y'])] != n:
                    map[(position['x'], position['y'])]['val'] = map[(position['x'], position['y'])]['val'] + n
                    map[(position['x'], position['y'])]['steps'][n] = steps
                else:
                    if n == 1:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {1: steps}}
                    if n == 2:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {2: steps}}
        elif line[0] == 'D':
            for i in range(position['y']-1, position['y'] - int(line[1:])-1, -1):
                position['y'] = i
                steps += 1
                if (position['x'], position['y']) in map and map[(position['x'], position['y'])] != n:
                    map[(position['x'], position['y'])]['val'] = map[(position['x'], position['y'])]['val'] + n
                    map[(position['x'], position['y'])]['steps'][n] = steps
                else:
                    if n == 1:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {1: steps}}
                    if n == 2:
                        map[(position['x'], position['y'])] = {'val': n, 'steps': {2: steps}}
    return map

def main():
    with open("input3") as input:
        wire1 = list(str(input.readline()).split(","))
        wire2 = list(str(input.readline()).split(","))
    best_key_val = None
    best_key_val_dist = None
    best_key_step = None
    best_key_step_count = None
    map_dict = {}
    #wire1 = ['R8','U5','L5','D3']
    #wire2 = ['U7','R6','D4','L4']
    map_dict = traceWire(map_dict, wire1, 1)
    map_dict = traceWire(map_dict, wire2, 2)
    for key, value in map_dict.items():
        if value['val'] == 3:
            print('Key with 3:', key, value['steps'])
            key_dist = abs(key[0]) + abs(key[1])
            if not best_key_val == None:
                if best_key_val_dist > key_dist:
                    best_key_val = key
                    best_key_val_dist = key_dist
            else:
                best_key_val = key
                best_key_val_dist = key_dist

            if best_key_step != None:
                if value['steps'][1] + value['steps'][2] < best_key_step_count:
                    best_key_step = key
                    best_key_step_count = value['steps'][1] + value['steps'][2]
            else:
                best_key_step = key
                best_key_step_count = value['steps'][1] + value['steps'][2]


    print('Best Val:', best_key_val, best_key_val_dist)
    print('Best Step:', best_key_step, best_key_step_count)

if __name__ == "__main__":
    main()