import time
import sys
import copy
import heapq
"""
Input
    n,m - Numero de Vertices e Aresta
    m (u,v,w) - aresta com peso w entre os vertices u e v
"""

"""
Output
    n = Quantidade de vertices no conjunto S
    i = Indices dos vertices S, separado por espaço
    w = W(C(S)) - corte mínimo 
"""
class Graph(object):
    def __init__(self):
        
        self.graph = dict()
    def set_adjacency_list(self,u, v, w):
        """ 
            Cria lista de Adjacencia
        """
        if v not in self.graph:
            self.graph[v] = {}
            self.graph[v][u] = w
        else: 
            self.graph[v][u] = w
    
    def mergeGraph(self, v, newVertice):
        self.graph[v] = newVertice

            
    def get_graph(self):
        return self.graph

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
    print(matrizAdjacencia)
    print(vertices, arestasInt)

    #for i in range(0, int(vertices)):
    #    for j in range(0, int(vertices)):
    #        matrizAdjacencia[i][j] = 2
    for l in first_line[1:len(first_line)]:
        r = list(map(int, l.split("\n")[0].split(" ")))
        print(r)
        matrizAdjacencia[r[0]][r[1-1]] = r[2]
            
    print(matrizAdjacencia)

    graph = Graph()
    #print(graph.get_graph())

    #print(graph.get_graph())
    


            	    

if __name__ == "__main__":
    main()