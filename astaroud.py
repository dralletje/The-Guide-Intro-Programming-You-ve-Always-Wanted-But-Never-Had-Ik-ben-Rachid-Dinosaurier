import math

def traceBack(cameFromMap, current):
    result = [current]
    while current in cameFromMap.keys():
        current = cameFromMap[current]
        result.append(current)
    return result[::-1]

# heuristic may never over-estimate
# f = g + h
def dosomeastarxxx(start, goal, getNbrsOf, nbrDistance, heuristic, isGoalReached=lambda a,b:a==b):
    inf = float("inf")
    closedSet = []
    openSet = [start]
    # for each node: the most efficient preceding node
    cameFromMap = {}
    # for each node: the cost of getting there from start
    gScoreMap = {start: 0}
    # for each node: the total cost of getting from start to goal through that node, partly heuristic
    fScoreMap = {start: heuristic(start, goal)}

    while len(openSet):
        current = min(openSet, key=lambda node: fScoreMap.get(node, inf))
        if isGoalReached(current, goal):
            return [fScoreMap[current], traceBack(cameFromMap, current)]
        openSet.remove(current)
        closedSet.append(current)

        for nbr in getNbrsOf(current):
            if nbr in closedSet:
                continue
            if not nbr in openSet:
                openSet.append(nbr)
            newGScore = gScoreMap[current] + nbrDistance(current, nbr)
            if newGScore < gScoreMap.get(nbr,inf):
                cameFromMap[nbr] = current
                gScoreMap[nbr] = newGScore
                fScoreMap[nbr] = newGScore + heuristic(nbr, goal)
    return [0,[]]

# ALLES HIER ONDER IS NIET NODIG




boardString = """
..s#....
.###..#g
...#.###
...#....
....#...
....#...
........
........
"""

boardString = """
+--+--+--+--+--+--+--+--+--+--+
s  |           |        |     |
+  +  +--+--+  +  +--+  +  +  +
|     |           |     |  |  |
+--+--+  +--+  +--+  +  +  +  +
|        |     |     |  |  |  |
+  +--+--+--+--+  +--+  +  +  +
|        |     |  |     |  |  |
+--+--+  +  +  +  +--+--+  +--+
|     |  |  |  |  |     |     |
+  +  +  +--+  +  +  +  +  +  +
|  |  |     |  |     |     |  |
+  +--+--+  +  +--+--+--+--+  +
|           |        |        |
+--+--+  +--+--+  +  +  +--+--+
|        |     |  |  |     |  |
+  +--+--+--+  +--+  +--+  +  +
|  |  |     |  |     |     |  |
+  +  +  +  +  +  +  +  +--+  +
|        |        |  |        g
+--+--+--+--+--+--+--+--+--+--+
"""



boardString = open("maze.txt",'r').read()

boardLines = boardString.replace(" ",".").split()
width = len(boardLines[0])
length = len(boardLines)

for y, line in enumerate(boardLines):
    for x, char in enumerate(boardLines[y]):
        if char == 's':
            start = (x,y)
            boardLines[y] = boardLines[y].replace('s','.')
        elif char == 'g':
            goal = (x,y)
            boardLines[y] = boardLines[y].replace('g','.')

board = [[0 if (c=='.' or c==' ') else 1 for c in line] for line in boardLines]

moves = [(0,1), (1,0),(0,-1),(-1,0)]

def getAt(x,y):
    if x<0 or y<0 or x>=width or y>=length:
        return -1
    return board[y][x]

def nFunc(node):
    return list(filter(lambda p: getAt(p[0],p[1])==0, [(node[0]+m[0],node[1]+m[1]) for m in moves]))

def h(a, b):
    #return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
    #return abs(a[0]-b[0]) + abs(a[1]-b[1])
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

for i in range(1):
    dist, path = dosomeastarxxx(start, goal, nFunc, lambda a,b: 1.0, h)

for point in path:
    boardLines[point[1]] = str.join("",['x' if i==point[0] else c for i,c in enumerate(boardLines[point[1]])]).replace("."," ")

print(str.join("\n",boardLines))
