from graph import Graph, Vertex
from queue import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line.strip()
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def bfs(g, start):
    bfs_graph = {}
    start.distance = 0
    start.pred = None
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while not vertQueue.isEmpty():
        current = vertQueue.dequeue()
        for neighbor in current.getConnections():
            if neighbor.color == 0:
                neighbor.color = 1
                neighbor.distance = current.distance + 1
                neighbor.pred = current
                vertQueue.enqueue(neighbor)
        current.color = 2

def dfs(g, start):
    start.color = 1
    for neighbor in start.getConnections():
        if neighbor.color == 0:
            dfs(g, neighbor)

def traverse(end):
    if end.pred is not None:
        traverse(end.pred)
    print end.getId()
