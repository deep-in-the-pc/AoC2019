import math
import operator
import numpy as np

class asteroid():

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.rho, self.phi = self.cart2pol(self.x, self.y)
        self.astDetCount = 0
        self.astDetVec = []

    def getPositionCart(self):
        return (self.x, self.y)

    def addDetAsteroid(self, position_cart):
        self.astDetCount = self.astDetCount + 1

        self.astDetVec.append((position_cart[0], position_cart[1]))
        #print("ADDED: ", position_cart)

    def checkVisibility(self, position_cart, mode=0):
        if not mode:
            if self.astDetCount == 0:
                self.addDetAsteroid(position_cart)
            else:
                A0 = position_cart[0] - self.x
                B0 = position_cart[1] - self.y
                position_pol_0 = self.cart2pol(A0, B0)
                #print("Position:", position_cart, position_pol_0)
                for n, vec in enumerate(self.astDetVec):
                    A1 = vec[0] - self.x
                    B1 = vec[1] - self.y
                    position_pol_1 = self.cart2pol(A1, B1)

                    #print("Vec:", vec, position_pol_1)
                    if position_pol_0[1] == position_pol_1[1]:
                        if position_pol_0[0]<position_pol_1[0]:
                            #print("Switched: ", self.astDetVec[n], "for ", position_cart)
                            self.astDetVec[n] = position_cart
                        return 0
                self.addDetAsteroid(position_cart)
                return 1
        else:
            self.addDetAsteroid(position_cart)
            return 1

    def cart2pol(self, x, y):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        return(rho, phi)

    def pol2cart(self, rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        return(x, y)

def normalizeAngle(angle):
    newAngle = angle

    while (newAngle <= -np.pi):
        newAngle += 2*np.pi
    while (newAngle > np.pi):
        newAngle -= 2*np.pi
    return newAngle


def main():

    asteroids = []

    with open("input10") as input:

        for y, line in enumerate(input.readlines()):
            for x, data in enumerate(line):
                if data == '#':
                    asteroids.append(asteroid((x, y)))

    print(len(asteroids))
    # bestlocation = 0
    # ast_index = 0
    # for n, ast in enumerate(asteroids):
    #     asteroids[n].astDetVec = []
    #     for cAst in asteroids:
    #         if asteroids[n] == cAst:
    #             continue
    #         asteroids[n].checkVisibility(cAst.getPositionCart())
    #     if ast.astDetCount>bestlocation:
    #         bestlocation = ast.astDetCount
    #         ast_index = n


    bestlocation = 274
    ast_index = 210

    print(ast_index, bestlocation)

    asteroids[ast_index].astDetVec = []

    for cAst in asteroids:
        if asteroids[ast_index] == cAst:
            continue
        asteroids[ast_index].checkVisibility(cAst.getPositionCart(), 1)

    asteroids_pol = []
    min_norm_angle = 0
    print(asteroids[ast_index].x, asteroids[ast_index].y)
    for n in asteroids[ast_index].astDetVec:

        A0 = asteroids[ast_index].x - n[0]
        B0 = asteroids[ast_index].y - n[1]

        rho = np.sqrt(A0**2 + B0**2)
        phi = np.arctan2(B0, A0)
        #print(A0, B0, phi)
        phi = normalizeAngle(phi)
        #print(A0, B0, phi)
        asteroids_pol.append((rho, phi))


    asteroids_pol = sorted(asteroids_pol, key=operator.itemgetter(0), reverse = False)

    asteroids_pol = sorted(asteroids_pol, key=operator.itemgetter(1), reverse = False)

    for n, val in enumerate(asteroids_pol):
        if val[1] == np.pi/2:
            break

    lastval = None
    count = 0
    while(len(asteroids_pol)):

        if(len(asteroids_pol)<=n):
            n = 0
        val = asteroids_pol[n][1]
        x = round(asteroids_pol[n][0] * np.cos(asteroids_pol[n][1]))
        y = round(asteroids_pol[n][0] * np.sin(asteroids_pol[n][1]))
        x = asteroids[ast_index].x - x
        y = asteroids[ast_index].y - y
        #print(n, count, lastval, val, x, y)
        if lastval == None or val != lastval:

            if count == 199:
                x = asteroids_pol[n][0] * np.cos(asteroids_pol[n][1])
                y = asteroids_pol[n][0] * np.sin(asteroids_pol[n][1])
                x = asteroids[ast_index].x - x
                y = asteroids[ast_index].y - y
                print(n, count, lastval, val, asteroids_pol[n], x, y)
                break
            lastval = asteroids_pol.pop(n)[1]
            count = count + 1
        else:
            n = n + 1


    print(x*100+y)




if __name__ == "__main__":
    main()