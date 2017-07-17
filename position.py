import random
import sys
sys.setrecursionlimit(100000000000)

def newCoords(excluded):
    rangeX = (200, 960)
    rangeY = (200, 960)

    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    if (x,y) in excluded or x > 800 or x < 50 or y > 600 or y < 50:
        return newCoords(excluded)
    return { "x": x, "y": y }

def addLocationToNode(node, excluded, deltas):
    coords = newCoords(excluded)
    excluded.update((coords["x"]+dx, coords["y"]+dy) for (dx,dy) in deltas)
    node["coords"] = { "x": coords["x"], "y": coords["y"] }
    
def positionNodes(nodes, deltas):
    excluded = set()
    for node in nodes:
        addLocationToNode(nodes[node], excluded, deltas)
        
def mapNodes(nodes, deltas):
    radius = 3
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x,y))
                
    positionNodes(nodes, deltas)