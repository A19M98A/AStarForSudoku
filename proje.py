class Node:
    Page = [[0,0,0,0,0,0,0,0] for i in range(8)]
    parent = 1
    f = 0
    h = 0
    
def printPage(page):
    print('----------------------')
    for i in range(8):
        s = ''
        for j in range(8):
            s += str(page[i][j]) + ' '
        print(s)

def checkExistence(Page):
    # return False
    for node in openList:
        if checkSame(node.Page, Page):
            return True
    for node in closedList:
        if checkSame(node.Page, Page):
            return True
    return False

def checkSame(Page1, Page2):
    for i in range(8):
            for j in range(8):
                if Page1[i][j] != Page2[i][j]:
                    return False
    return True

def findH(Page):
    Collision = 0
    for i in range(8):
        for j in range(8):
            if Page[i][j] != 0:
                for p in range(1, 8):
                    if i - p >= 0 and j - p >= 0:
                        if Page[i - p][j - p] != 0:
                            Collision += 1
                    if i - p >= 0 and j + p < 8:
                        if Page[i - p][j + p] != 0:
                            Collision += 1
                    if i + p < 8 and j - p >= 0:
                        if Page[i + p][j - p] != 0:
                            Collision += 1
                    if i + p < 8 and j + p < 8:
                        if Page[i + p][j + p] != 0:
                            Collision += 1
                if Page[i][j] == 1:
                    for p in range(8):
                        if Page[p][j] != 0 and p != i:
                            Collision += 1
                        if Page[i][p] != 0 and p != j:
                            Collision += 1
    return Collision

def copyMatris(ParentPage):
    Page = [[0,0,0,0,0,0,0,0] for i in range(8)]
    for i in range(8):
        for j in range(8):
            Page[i][j] = ParentPage[i][j]
    return Page

def extendQueenUp(ParentNode, i, j):
    for move in range(1, 8):
        if i - move >= 0:
            if ParentNode.Page[i - move][j] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i][j] = 0
                node.Page[i - move][j] = 1
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendQueenDown(ParentNode, i, j):
    for move in range(1, 8):
        if i + move < 8:
            if ParentNode.Page[i + move][j] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i][j] = 0
                node.Page[i + move][j] = 1
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendQueenLeft(ParentNode, i, j):
    for move in range(1, 8):
        if j - move >= 0:
            if ParentNode.Page[i][j - move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i][j] = 0
                node.Page[i][j - move] = 1
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendQueenRight(ParentNode, i, j):
    for move in range(1, 8):
        if j + move < 8:
            if ParentNode.Page[i][j + move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i][j] = 0
                node.Page[i][j + move] = 1
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendUpRight(ParentNode, i, j):
    for move in range(1, 8):
        if i - move >= 0 and j + move < 8:
            if ParentNode.Page[i - move][j + move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i - move][j + move] = node.Page[i][j]
                node.Page[i][j] = 0
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendUpLeft(ParentNode, i, j):
    for move in range(1, 8):
        if i - move >= 0 and j - move >= 0:
            if ParentNode.Page[i - move][j - move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i - move][j - move] = node.Page[i][j]
                node.Page[i][j] = 0
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendDownRight(ParentNode, i, j):
    for move in range(1, 8):
        if i + move < 8 and j + move < 8:
            if ParentNode.Page[i + move][j + move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i + move][j + move] = node.Page[i][j]
                node.Page[i][j] = 0
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extendDownLeft(ParentNode, i, j):
    for move in range(1, 8):
        if i + move < 8 and j - move >= 0:
            if ParentNode.Page[i + move][j - move] == 0:
                node = Node()
                node.Page = copyMatris(ParentNode.Page)
                node.Page[i + move][j - move] = node.Page[i][j]
                node.Page[i][j] = 0
                if checkExistence(node.Page):
                    continue
                node.f = ParentNode.f + 1
                node.h = findH(node.Page)
                node.parent = ParentNode
                openList.append(node)
            else:
                return
        else:
            return

def extend(ParentNode):
    for i in range(8):
        for j in range(8):
            if ParentNode.Page[i][j] != 0:
                extendUpLeft(ParentNode, i, j)
                extendUpRight(ParentNode, i, j)
                extendDownLeft(ParentNode, i, j)
                extendDownRight(ParentNode, i, j)
            if ParentNode.Page[i][j] == 1:
                extendQueenUp(ParentNode, i, j)
                extendQueenDown(ParentNode, i, j)
                extendQueenLeft(ParentNode, i, j)
                extendQueenRight(ParentNode, i, j)
for t in range(101):
    f = open("inputs/input" + str(t) + ".txt", "r")
    print(f.name)
    lines = f.read().split('\n')
    Page = [[0,0,0,0,0,0,0,0] for i in range(8)]
    for i in range(8):
        for j in range(8):
            Page[i][j] = int(lines[i].split(' ')[j])
    openList = []
    closedList = []
    node = Node()
    node.Page = Page
    node.h = findH(Page)
    node.f = 0
    openList.append(node)
    while len(openList) > 0:
        minNode = openList[0]
        for node in openList:
            if minNode.h*100 + minNode.f > node.h*100 + node.f:
                minNode = node
        openList.remove(minNode)
        closedList.append(minNode)
        if minNode.h == 0:
            print('f: ' + str(minNode.f))
            print('nodes: ' + str(len(openList) + len(closedList)))
            temp = minNode
            while temp != 1:
                printPage(temp.Page)
                temp = temp.parent
            break
        extend(minNode)