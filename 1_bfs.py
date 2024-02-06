from collections import defaultdict

class Graph:
    
    #constructor
    def __init__(self) -> None:
      self.graph = defaultdict(list)

    # method to add edge
    def addEdge(self, u, v):
       self.graph[u].append(v)
       self.graph[v].append(u)

    # method for bfs traversal of graph
    def BFS(self, src):
        
       visited = {}

       que = []

       que.append(src)
       visited[src] = True

       while (que):
          s = que.pop(0)
          print(s, end = " ")

          for nei in self.graph[s]:
             if (visited.get(nei, 0) == 0):
                visited[nei] = True
                que.append(nei)

       print()


if __name__ == '__main__':
 
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
 
    print("Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)

    