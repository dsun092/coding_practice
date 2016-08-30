class Vertex:
    def __init__(self, key):
        self.id = key
        self.adj = {}
        self.distance = 0
        self.pred = None
        self.color = 0

    def addConnection(self, neighbor, weight=0):
        self.adj[neighbor] = weight
    def getConnections(self):
        return self.adj.keys()
    def getId(self):
        return self.id
    def getWeight(self, neighbor):
        if neighbor in adj:
            return self.adj[neighbor]
        else:
            return None

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVert = 0

    def addVertex(self, key):
        if key not in self.vertList:
            vert = Vertex(key)
            self.vertList[key] = vert
            self.numVert = self.numVert + 1
            return vert
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList
    def addEdge(self, origin, dest, weight=0):
        if origin not in self.vertList:
            origin_v = self.addVertex(origin)
        if dest not in self.vertList:
            dest_v = self.addVertex(dest)
        self.vertList[origin].addConnection(self.vertList[dest], weight)
    def getVertices(self):
        return self.vertList.keys()
    def resetGraph(self):
        keys = self.vertList.keys()
        for k in keys:
            self.vertList[k].distance = 0
            self.vertList[k].color = 0
            self.vertList[k].pred = None

