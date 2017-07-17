def printNode(nodeId, nodes):
    printConnections(nodes[nodeId], nodes)
    
    coords = nodes[nodeId]["coords"]
    ellipseSize = nodes[nodeId]["size"] * 20

    strokeWeight(1)

    fill(0, 102, 153, 51)
    ellipse(coords["x"], coords["y"], ellipseSize, ellipseSize)
    
    fill(255,255,255)
    textAlign(CENTER, CENTER)
    textSize(16)
    text(nodeId, coords["x"], coords["y"])
    
def printNodes(nodes):
    fill(0, 102, 153, 51);
    for nodeId in nodes:
        coords = nodes[nodeId]["coords"]
        printNode(nodeId, nodes)
            
def printConnections(node, nodes):
    for target in node:
        try:
            targetPoint = nodes[target]["coords"]
            selfPoint = node["coords"]
            strokeWeight(node[target])
            line(selfPoint["x"], selfPoint["y"], targetPoint["x"], targetPoint["y"])
        except KeyError:
            pass