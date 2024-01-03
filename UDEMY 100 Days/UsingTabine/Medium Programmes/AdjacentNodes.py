def are_adjacent(adj_matrix, node1, node2):
    if node1 >= len(adj_matrix) or node2 >= len(adj_matrix):
        return False
    return adj_matrix[node1][node2] == 1 or adj_matrix[node2][node1] == 1


class Matrix:
    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]

    def addEdge(self, u, v):
        self.matrix[u][v] = 1

    def deleteEdge(self, u, v):
        self.matrix[u][v] = 0

    def getNeighbors(self, u):
        neighbors = []
        for i in range(len(self.matrix[u])):
            if self.matrix[u][i] == 1:
                neighbors.append(i)
        return neighbors

    def isAdjacent(self, u, v):
        if self.matrix[u][v] == 1:
            return True
        else:
            return False

    def printMatrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
            
m = Matrix(5)
m.addEdge(0, 1)
m.addEdge(0, 4)
m.addEdge(1, 0)
m.addEdge(1, 2)
m.addEdge(1, 3)
m.addEdge(1, 4)
m.addEdge(2, 1)
m.addEdge(2, 3)
m.addEdge(3, 1)
m.addEdge(3, 2)
m.addEdge(3, 4)
m.addEdge(4, 0)
m.addEdge(4, 1)
m.addEdge(4, 3)

m.printMatrix()
print(m.getNeighbors(1))
print(m.isAdjacent(1, 3))

