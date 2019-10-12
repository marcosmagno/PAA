# Python program for finding min-cut in the given graph 
# Complexity : (E*(V^3)) 
# Total augmenting path = VE and BFS with adj matrix takes :V^2 times 
import time
import sys
import copy
import heapq
import operator  
from collections import defaultdict 
  
# This class represents a directed graph using adjacency matrix representation 
class Graph: 
  
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self.org_graph = [i[:] for i in graph] 
        self. ROW = len(graph) 
        self.COL = len(graph[0]) 
  
  
    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
  
        # Create a queue for BFS 
        queue=[] 
  
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
  
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
  
  
    # Returns the min-cut of the given graph 
    def minCut(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        # print the edges which initially had weights 
        # but now have 0 weight 
        for i in range(self.ROW): 
            for j in range(self.COL): 
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0: 
                    print(str(i) + " - " + str(j))
  
class Input(object):
    def read_file(self, file_name):
        get_file = open(file_name,"r")
        return get_file

def main():
    file_ = Input()
    file_recv = sys.argv[1]
    obj_file = file_.read_file(str(file_recv))

    first_line = obj_file.readlines()
    vertices = first_line[0].split(" ")[0]
    arestas = first_line[0].split(" ")[1]
    arestasInt = arestas.replace("\n","")[0]
    #matrizAdjacencia = [4][4]
    matrizAdjacencia = [[0]*int(vertices) for i in range(int(vertices))]

    #for l in first_line[1:len(first_line)]:
    #    r = list(map(int, l.split("\n")[0].split(" ")))
    #    matrizAdjacencia[r[0]][r[1]] = r[2]
            
    #print(matrizAdjacencia)

    #graph = Graph()
    # Create a graph given in the above diagram 





    graph = [[0, 2, 0, 0, 3, 0, 0, 0], 
            [2, 0, 3, 0, 2, 2, 0, 0], 
            [0, 0, 3, 4, 0, 0, 2, 0], 
            [0, 0, 4, 2, 0, 0, 2, 2], 
            [0, 2, 0, 0, 2, 3, 0, 0], 
            [0, 2, 3, 0, 0, 3, 3, 0], 
            [0, 2, 0, 0, 0, 3, 1, 3], 
            [0, 0, 0, 2, 0, 0, 3, 3]]
    g = Graph(graph) 
    
    for i in range(0, 8):
        source = i; sink = 8 -1
    
        g.minCut(source, sink) 
if __name__ == "__main__":
    main()