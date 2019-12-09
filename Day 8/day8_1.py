import math

def main():

    with open("input8") as input:
        data = input.readline()
    layers = []
    n=0
    k=0
    lowest_0 = 0
    lowest_k = 0
    while(n<len(data)):
        layer = []
        for i in range(25):

            for j in range(6):

                layer.append(int(data[n]))

                n = n + 1
        if(k == 0 or layer.count(0)<lowest_0):
            lowest_0 = layer.count(0)
            lowest_k = k
            print(lowest_0, lowest_k)
        k = k + 1
        layers.append(layer)
    print(k)
    print(layers[lowest_k].count(1)*layers[lowest_k].count(2))


    image = [None]*25*6

    for l in layers:
        n = 0
        for pixel in l:
            if pixel != 2 and image[n] != 0 and image[n] != 1:
                image[n] = pixel
            n = n + 1
    image = ['1' if x == 1 else ' ' for x in image]
    for n in range(0, 6):
        print(image[n*25:25+n*25])




if __name__ == "__main__":
    main()