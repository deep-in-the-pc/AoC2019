import math

class node:

    def __init__(self, name, son=None, parent=None):
        self.name = name
        self.parent = parent
        self.sons = []
        if son != None:
            self.sons.append(son)

        self.count = 0

    def __contains__(self, key):
        return key in self.sons

    def __str__(self):
        if self.parent:
            return self.name + " " + self.parent + " " + str(self.count)
        else:
            return self.name + " " + str(self.count)

    def addSon(self, son):
        self.sons.append(son)

    def addParent(self, parent):
        self.parent = parent


def countRecursive(node_list, node, count):
    cumsum = 0

    if node in node_list:
        for son in node_list[node].sons:
            cumsum = cumsum + countRecursive(node_list, son, count + 1)

    return cumsum + count

def addCount(node_list, node, count):
    cumsum = 0

    if node in node_list:
        node_list[node].count = count
        for son in node_list[node].sons:
            node_list = addCount(node_list, son, count + 1)


    return node_list

def treeToRoot(A, node_dict, tree):

    if node_dict[A].parent:
        tree.append(node_dict[A].parent)

        treeToRoot(node_dict[A].parent, node_dict, tree)
    return tree

def minOrbitDist(A, B, node_dict):

    treeOfA = []
    treeOfB = []

    treeOfA = treeToRoot(A, node_dict, treeOfA)
    treeOfB = treeToRoot(B, node_dict, treeOfB)

    distB = 0

    for bodyB in treeOfB:
        distA = 0
        for bodyA in treeOfA:
            if bodyA == bodyB:
                return distA+distB
            distA = distA + 1
        distB = distB + 1



def main():
    node_dict = {}
    with open("input6") as input:
        for line in input:
            A, B = line.rstrip().split(')')
            if A not in node_dict:
                node_dict[A] = node(A, son=B)
            else:
                node_dict[A].addSon(B)
            if B not in node_dict:
                node_dict[B] = node(B, parent=A)
            else:
                node_dict[B].addParent(A)

    node_dict = addCount(node_dict, 'COM', 0)

    print(minOrbitDist('YOU', 'SAN', node_dict))


if __name__ == "__main__":
    main()