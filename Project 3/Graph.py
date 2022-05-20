import networkx as nx
import matplotlib.pyplot as plt
import random 
import numpy as np

class Graph:
    def __init__(self):
        self.content = None
        self.type = None
        self.graph = nx.Graph()
        self.minSpanTree = nx.Graph()
        plt.subplot(111)
        self.nodes = []
        self.hasDistMatrix = False

    def create_random_graph(self) -> None:
        # clear graph
        nodesInGraph = list(self.graph.nodes)
        self.graph.remove_nodes_from(nodesInGraph)
        self.nodes.clear()

        self.numberOfVertices = random.randint(4,15)
        self.nodes.append(1)

        # distance matrix for later
        self.distMatrix = np.zeros((self.numberOfVertices, self.numberOfVertices))

        # add vertices and connect
        for i in range(2,self.numberOfVertices):
            self.graph.add_node(i)
            self.nodes.append(i)
            randomNode = random.choice(self.nodes)
            while randomNode is i:
                randomNode = random.choice(self.nodes)
            randomWeight = random.randint(1,10)
            self.graph.add_edge(i, randomNode, weight=randomWeight)
        
        # add some more edges
        targetNumberOfEdges = random.randint(self.numberOfVertices+1, self.numberOfVertices*2 - 2)
        for i in range(self.numberOfVertices-1, targetNumberOfEdges):
            nonExistingEdges = list(nx.non_edges(self.graph))
            if len(nonExistingEdges) != 0:
                edgeTuple = random.choice(nonExistingEdges)
                randomWeight = random.randint(1,10)
                self.graph.add_edge(edgeTuple[0], edgeTuple[1], weight=randomWeight)
        
        self.hasDistMatrix = False
             

    def visualize(self) -> None:
        plt.figure(2)
        plt.clf()
        plt.figure(1)
        plt.clf()
        self.pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, self.pos, with_labels=True)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, self.pos, edge_labels=labels)
        plt.show()

    def init(self, selectedVertex, ds, ps, selected) -> None:
        for i in range(self.numberOfVertices):
            ds[i] = float('inf')
            ps[i] = None
        ds[selected] = 0

    def relax(self, u, v, ds, ps):
        w = self.graph.get_edge_data(u,v)['weight']
        if ds[v] > ds[u] + w:
            ds[v] = ds[u] + w
            ps[v] = u


    def getDijkstra(self, selectedVertex):
        ds = [0] * self.numberOfVertices
        ps = [0] * self.numberOfVertices
        self.init(selectedVertex, ds, ps, selectedVertex)
        
        # vertexes left to do, checking what is left, instead of checking what isn't in "already done"
        toDo = [_ for _ in range(1, self.numberOfVertices)]
        
        while len(toDo) != 0:
            u = toDo[0]
            for i in toDo:
                if ds[u] > ds[i]:
                    u = i
            toDo.remove(u)

            for v in toDo:
                if self.graph.has_edge(u, v):
                    self.relax(u, v, ds, ps)

        # add all distances to distance Matrix
        for i in range(1, self.numberOfVertices):
            self.distMatrix[selectedVertex][i] = ds[i]

        return ds, ps
    
    def getPathsFrom(self, selectedVertex):
        #convert previous nodes and distances to string output
        ds, ps = self.getDijkstra(selectedVertex)
        ans = "START: n = " + str(selectedVertex) + "\n"
        for i in range(1, self.numberOfVertices):
            if i == selectedVertex:
                ans += "d(" + str(i) + ") = " + str(ds[i]) + " ==> [" + str(i) + "]\n"
            else:
                ans += "d(" + str(i) + ") = " + str(ds[i]) + " ==> [" + str(i) + " <- "
                currentVertex = i
                while ps[currentVertex] != selectedVertex and ps[currentVertex] != None :
                    ans += str(ps[currentVertex]) + " <- "
                    currentVertex = ps[currentVertex]
                ans += str(selectedVertex) + " ]\n"
        return ans


    def getDistMatrix(self):

        # fill distance matrix
        for i in range(1, self.numberOfVertices):
            self.getDijkstra(i)

        # delete row 0 and column 0
        distMatrixNo0 = np.delete(self.distMatrix, 0, 1)
        distMatrixNo0 = np.delete(distMatrixNo0, 0, 0)

        # one liner to convert matrix into nice string output
        ans = '\n'.join('\t'.join('%d' %x for x in y) for y in distMatrixNo0)
        self.hasDistMatrix = True
        return ans

    def getCenter(self):
        if self.hasDistMatrix is False:
            self.getDistMatrix()
        
        #get sum in rows
        distanceSum = [float('inf')] * self.numberOfVertices
        for i in range(1,self.numberOfVertices):
            rowSum = 0
            for j in range(1, self.numberOfVertices):
                rowSum += self.distMatrix[i][j]
            distanceSum[i] = rowSum
        
        #choose smallest
        return str(np.argmin(distanceSum))
    
    def getMinimax(self):
        if self.hasDistMatrix is False:
            self.getDistMatrix()
        
        #get highest value in rows
        maxDist = [float('inf')] * self.numberOfVertices
        for i in range(1, self.numberOfVertices):
            rowHighest = 0
            for j in range(1, self.numberOfVertices):
                if rowHighest < self.distMatrix[i][j]:
                    rowHighest = self.distMatrix[i][j]
            maxDist[i] = rowHighest
        
        #choose smallest
        return str(np.argmin(maxDist)) 
    
    def getAdjacencyMatrix(self, G) -> None:
        for i in range(1, self.numberOfVertices):
            for j in range(1, self.numberOfVertices):
                if self.graph.has_edge(i, j):
                    G[i][j] = self.graph.get_edge_data(i,j)['weight']
        
        return

    def initMinSpanTree(self):
        for i in range(1, self.numberOfVertices):
            self.minSpanTree.add_node(i)
        return

    def drawMinSpanTree(self):
        # clear tree
        nodesInTree = list(self.minSpanTree.nodes)
        self.minSpanTree.remove_nodes_from(nodesInTree)
        self.initMinSpanTree()

        v = self.numberOfVertices
        G = np.zeros((v, v))
        self.getAdjacencyMatrix(G)
        
        selected = [False] * self.numberOfVertices
        numberOfEdges = 0
        selected[1] = True

        while numberOfEdges < v-2:
            minimum = float('inf')
            x = 1
            y = 1
            for i in range(1, v):
                if selected[i]:
                    for j in range(1, v):
                        if selected[j] == False and G[i][j] > 0.001:
                            if minimum > G[i][j]:
                                minimum = G[i][j]
                                x = i
                                y = j

            w = self.graph.get_edge_data(x, y)['weight']
            self.minSpanTree.add_edge(x, y, weight=w, color='g')
            selected[y] = True
            numberOfEdges += 1
        
        # draw min span tree
        plt.figure(2)
        pos = nx.spring_layout(self.minSpanTree)
        nx.draw(self.minSpanTree, self.pos, with_labels=True)
        labels = nx.get_edge_attributes(self.minSpanTree, 'weight')
        nx.draw_networkx_edge_labels(self.minSpanTree, self.pos, edge_labels=labels)
        plt.show()
        

