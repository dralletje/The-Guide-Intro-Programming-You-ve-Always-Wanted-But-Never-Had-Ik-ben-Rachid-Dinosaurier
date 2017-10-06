def traceBack(cameFromMap, current):
    result = [current]
    while current in cameFromMap.keys():
        current = cameFromMap[current]
        result.append(current)
    return result[::-1]

def dosomeastarxxx(start, goal, get_neighbours_of, neighbour_distance, heuristic, is_goal_reached=lambda a,b:a==b):
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
        if is_goal_reached(current, goal):
            return [fScoreMap[current], traceBack(cameFromMap, current)]
        openSet.remove(current)
        closedSet.append(current)

        for neighbour in get_neighbours_of(current):
            # Misschien is deze sneller als `closedSet` een `set()` is?
            if neighbour in closedSet:
                continue
            # Misschien kan deze check nog meer sneller als we van `openSet` een `set()` maken?
            if not neighbour in openSet:
                openSet.append(neighbour)
            newGScore = gScoreMap[current] + neighbour_distance(current, neighbour)
            if newGScore < gScoreMap.get(neighbour,inf):
                cameFromMap[neighbour] = current
                gScoreMap[neighbour] = newGScore
                fScoreMap[neighbour] = newGScore + heuristic(neighbour, goal)
    return [0,[]]

edges = {
    "A": {"S": 7, "B": 3, "D": 4},
    "C": {"S": 3, "L": 2},
    "B": {"A": 3, "H": 1,
    "S": 2, "D": 4},
    "E": {"K": 5, "G": 2},
    "D": {"A": 4, "B": 4, "F": 5},
    "G": {"H": 2, "E": 2},
    "F": {"H": 3, "D": 5},
    "I": {"K": 4, "J": 6, "L": 4},
    "H": {"B": 1, "G": 2, "F": 3},
    "K": {"I": 4, "J": 4, "E": 5},
    "J": {"I": 6, "K": 4, "L": 4},
    "L": {"I": 4, "C": 2, "J": 4},
    "S": {"A": 7, "C": 3, "B": 2},
}

result = dosomeastarxxx('S', 'E', lambda x: edges[x], lambda current, neighbour: edges[current][neighbour], lambda x, y: 0)

print('result: ' + str(result))
