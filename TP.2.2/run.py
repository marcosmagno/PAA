import time
import sys
import copy
import heapq
import operator
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
        if u not in self.graph:
            self.graph[u] = {}
            self.graph[u][v] = w
        else: 
            self.graph[u][v] = w
            
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
    graph = Graph()
    file_recv = sys.argv[1]
    obj_file = file_.read_file(str(file_recv))
    first_line = obj_file.readlines()
    vertices = first_line[0].split(" ")[0]
    arestas = first_line[0].split(" ")[1]
    arestasInt = arestas.replace("\n","")
    pesoMin = []
    conjuntoFinal = {}

    for l in first_line[1:len(first_line)]:
        r = list(map(int, l.split("\n")[0].split(" ")))
        graph.set_adjacency_list(r[0], r[1], r[2])
    graphSize = len(graph.get_graph().values())
    conjuntoSolucao = []
    conjuntoT = []
    for i in range(1, len(graph.get_graph().keys())+1):#tem que ver para os casos de testes
        conjuntoSolucao.append(i)
    agregate = {}
    listaSuprema = []
    deletados = []
    
    for i in range(0,len(graph.get_graph().keys())-1):
        listaConjuntoA = []
        a = 1
        conjuntoa = []
        r = []
        w = 0
        result, c = search(graph.get_graph(), a, conjuntoa, r)
        s = result[-2]
        t = result[-1]
        for i in c:
            if i not in conjuntoFinal:
                conjuntoFinal[i] = {}
                conjuntoFinal[i] = 0 # tem que ver se vai funcionar com zero
        if s in conjuntoFinal:
            conjuntoFinal[s] = t
        
        #if t not in graph.get_graph().get(s):
        #    s = result[-3]

        if graph.get_graph().get(t) != None:
            for k, v in graph.get_graph().get(t).items():
                w = w + v
                if graph.get_graph().get(s) != None:
                    if k in graph.get_graph().get(s): # se existe uma aresta, atualiza o peso
                        # atualiza o peso
                        graph.get_graph().get(s)[k] = graph.get_graph().get(t)[k] + graph.get_graph().get(s)[k]
            
                # atualiza o peso inverso
                if graph.get_graph().get(k) != None:
                    if s in graph.get_graph().get(k):
                        graph.get_graph().get(k)[s] = graph.get_graph().get(t).get(k) + graph.get_graph().get(k)[s]
            
                if graph.get_graph().get(s) != None:
                    if k not in graph.get_graph().get(s) and k != s:
                        graph.get_graph()[s][k] = v
              
                # deletando as arestas
                if graph.get_graph().get(k) != None:
                    if t in graph.get_graph().get(k):
                        del graph.get_graph().get(k)[t]
            pesoMin.append(w)
            del graph.get_graph()[t]
        

    print(min(pesoMin))
def search(graph, a, conjuntoa, r): # a = Vertice inicial
    r.append(a)
    if len(conjuntoa) == len(graph) -1:
        return
    
    conjuntoa.append(a)
    dictConjuntoToAdd = {}
    
    for i in conjuntoa: # 2
        if i in graph: # if 2, no graph
            for k, v in graph[i].items(): # para cada k, v do grafo na posicao 2
                if k not in conjuntoa: # se o 1, 5 não esta no conjunto A
                    if k not in dictConjuntoToAdd:
                        dictConjuntoToAdd[k] = {}
                        dictConjuntoToAdd[k] = v #1-> 2 5->2
                    else:
                        dictConjuntoToAdd[k] = dictConjuntoToAdd.get(k) + v
        else:
            pass
    m = max(dictConjuntoToAdd.items(), key=operator.itemgetter(1))[0]
    search(graph, m, conjuntoa, r)
    
    return r, conjuntoa


if __name__ == "__main__":
    main()