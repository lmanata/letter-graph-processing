def printNode(nodeId, nodes):
    coords = nodes[nodeId]["coords"]
    ellipseSize = nodes[nodeId]["size"] * 20

    fill(0, 102, 153, 51)
    ellipse(coords["x"], coords["y"], ellipseSize, ellipseSize)
    
    fill(0, 102, 153)
    textAlign(CENTER, CENTER)
    textSize(16)
    text(nodeId, coords["x"], coords["y"])
    
def printNodes(nodes):
    fill(0, 102, 153, 51);
    for nodeId in nodes:
        coords = nodes[nodeId]["coords"]
        printNode(nodeId, nodes)