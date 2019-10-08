import time
import sys
import copy
import heapq
import timeit
"""
Input
    n,m - Dimensão do container
    nm representará o pedo do k-ésimo pacote.
    Tabela 1 - Posição inicial
    Tabela 2 - Posição final

"""

"""
Output
    n = numero inteiro com a menor quantidade de energia necessaria
        para transformar a configuração inicial na configuração final
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
        else: 
            self.graph[v][u] = w
        
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
    linhas = first_line[0].split(" ")[0]
    colunas = first_line[0].split(" ")[1]
    pesos = first_line[1]
    rPeso = pesos.replace("\n","")
    allPesos = rPeso.split(" ")
    matrizInicial = []

    
    for i in range(2, len(first_line)):
        index = first_line[i].replace("\n","").split(" ")
        
        rIndex = list(map(int, index))
        for j in rIndex:
            matrizInicial.append(j)


    lenLinhaColuna = int(linhas) * int(colunas)
    vectorPesos = list(map(int, allPesos))
    resultMatrizInicial = list(map(int, matrizInicial))
    matrizInicial = resultMatrizInicial[0:lenLinhaColuna]
    matrizFinal = resultMatrizInicial[lenLinhaColuna:len(resultMatrizInicial)]
    i = 0
    dic_permutacao = {}
    for p in permutacao(matrizInicial):
        i = i + 1
        dic_permutacao[str(p)] = int(i)
    
    create_Graph(dic_permutacao, int(linhas), int(colunas), matrizInicial, matrizFinal, vectorPesos)
    end = timeit.timeit()
    
def create_Graph(permutations, l, c, matrizInicial, matrizFinal, vectorPesos):
    matriz = []
    matrizResultante = []
    graph = Graph()
    idMatrizFinal = permutations.get(str(matrizFinal))
    
    for k, v in permutations.items():
        
        #n = l
        r = k.replace("[","")
        r = r.replace("]","")
        resultList = list(map(int, r.split(",")))
        matriz = [resultList[i:i+int(c)] for i in range(0, len(resultList), int(c))]
        for i in range(0,l):
            for j in range(0,c-1):
                
                somaPeso = 2
                somaPeso = vectorPesos[matriz[i][j] -1 ] + vectorPesos[matriz[i][j+1]-1]
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][j+1]
                matriz[i][j+1] = aux
                
                u = getIdMatriz(matriz, permutations)

                graph.set_adjacency_list(u,v,somaPeso)
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][j+1]
                matriz[i][j+1] = aux
                somaPeso = 0


        for i in range(0,l-1):
            for j in range(0,c):
                aux = matriz[i][j]
                somaPeso = vectorPesos[matriz[i+1][j] -1 ] + vectorPesos[matriz[i][j]-1]
                matriz[i][j] = matriz[i+1][j]
                matriz[i+1][j] = aux
                u = getIdMatriz(matriz,permutations)
                graph.set_adjacency_list(u,v, somaPeso)
                aux = matriz[i][j]
                matriz[i][j] = matriz[i+1][j]
                matriz[i+1][j] = aux  
                somaPeso = 0
       
    result = calculate_distances(graph.get_graph(), 1)
    print(result[idMatrizFinal])


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def getIdMatriz(matrizResultante, allpermutations):

    array_toCheck = [item for sublist in matrizResultante for item in sublist]
    #print(flat_list)
    #for i in matrizResultante:
    #    for j in i:
    #        array_toCheck.append(j)
    return allpermutations.get(str(array_toCheck))
    
def permutacao(matrizAtual, c=0):
    if c + 1 >= len(matrizAtual):
        yield matrizAtual
    else:
        for p in permutacao(matrizAtual, c + 1):
            yield p
        for i in range(c + 1, len(matrizAtual)):
            matrizAtual[c], matrizAtual[i] = matrizAtual[i], matrizAtual[c]
            for p in permutacao(matrizAtual, c + 1):
                yield p
            matrizAtual[c], matrizAtual[i] = matrizAtual[i], matrizAtual[c]
            	    

if __name__ == "__main__":
    main()