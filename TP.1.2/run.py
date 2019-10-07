import time
import sys
import copy
import heapq
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
        print(u, v)
        if v not in self.graph:
            self.graph[v] = {}
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
    vectorPesos = []
    for i in range(2, len(first_line)):
        index = first_line[i].replace("\n","").split(" ")
        rIndex = list(map(int, index))
        for j in rIndex:
            vectorPesos.append(allPesos[j-1])
    lenLinhaColuna = int(linhas) * int(colunas)

    resulIntVector = list(map(int, vectorPesos))
    matrizInicial = resulIntVector[0:lenLinhaColuna]
    matrizFinal = resulIntVector[lenLinhaColuna:len(resulIntVector)]
    time.sleep(2)
    i = 1
    dic_permutacao = {}
    for p in permutacao(matrizInicial):
        dic_permutacao[str(p)] = int(i)
        i = i + 1
    create_Graph(dic_permutacao, int(linhas), int(colunas), matrizInicial, matrizFinal)


def create_Graph(permutations, l, c, matrizInicial, matrizFinal):
    matriz = []
    matrizResultante = []
    graph = Graph()
    
    for k, v in permutations.items():
        n = l
        r = k.replace("[","")
        r = r.replace("]","")
        resultList = list(map(int, r.split(",")))
        matriz = [resultList[i:i+int(c)] for i in range(0, len(resultList), int(c))]
        #matriz = [[1,2,3],[3,4,6],[7,8,9]]
        #len_l = len(v)
        #for i in range(n):
        #    start = int(i*len_l/n)
        #    end = int((i+1)*len_l/n)
        #    matriz.append(v[start:end])
        # permutacoes
        for i in range(0,l):
            for j in range(0,c-1):
                #print(matriz[i][j+1])
                #aux = matriz[i][j] # 1
                #matrizResultante[i][j] = matriz[i][j+1] #2
                #matrizResultante[i][j+1] = aux
                #print("Matriz Inicial Horizontal: ", matriz)
                # tentando fazer na mesma matriz
                #print("Custo Troca", matriz[i][j]+ matriz[i][j+1])
                aux = matriz[i][j] # 1
                matriz[i][j] = matriz[i][j+1]
                matriz[i][j+1] = aux
                u = espande_Permutacao(matriz, permutations)
                somaPeso = matriz[i][j] + matriz[i][j+1]
                graph.set_adjacency_list(u,v,somaPeso)
                aux = matriz[i][j]
                matriz[i][j] = matriz[i][j+1]
                matriz[i][j+1] = aux
                somaPeso = 0


        for i in range(0,l-1):
            for j in range(0,c):
                aux = matriz[i][j] # 1
                matriz[i][j] = matriz[i+1][j] #3
                matriz[i+1][j] = aux
                u = espande_Permutacao(matriz,permutations)
                somaPeso = matriz[i][j] + matriz[i+1][j]
                graph.set_adjacency_list(u,v, somaPeso)
                aux = matriz[i][j]
                matriz[i][j] = matriz[i+1][j]
                matriz[i+1][j] = aux  
                somaPeso = 0
    
    returnDistance = calculate_distances(graph.get_graph(), permutations.get(str(matrizInicial)))
    #print(returnDistance)
    #print(returnDistance[permutations.get(str(matrizFinal))])
    #for k, v in graph.get_graph().items():
    #    print(k, v)
    #for k,v in permutations.items():
    #    print(k,v)


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def relax(u, v, w):
    """ if v.d > u.d + w(u,v)
        v.d = u.d + w(u,v)
    """
    
def initSingleSource(G,s):
    """
        for cada vertice v in V[G]
            v.d = infinito
        s = 0
    """
def espande_Permutacao(matrizResultante, allpermutations):
    """ 
        return key from dict, if matrizResultante is in allpermutations
    """
    #print("matriz Trocada", matrizResultante)
    array_toCheck = []
    for i in matrizResultante:
        for j in i:
            array_toCheck.append(j)
    return allpermutations.get(str(array_toCheck))


def permutacao(matrizAtual, c=0):
    if c + 1 >= len(matrizAtual):
        #print("Matriz Atual", matrizAtual, c)

        yield matrizAtual
    else:
        for p in permutacao(matrizAtual, c + 1):
            #print("Matriz Atual", matrizAtual, c)
            yield p
        for i in range(c + 1, len(matrizAtual)):
            matrizAtual[c], matrizAtual[i] = matrizAtual[i], matrizAtual[c]
            for p in permutacao(matrizAtual, c + 1):
                #print("Matriz Atual", matrizAtual, c)
                yield p
            matrizAtual[c], matrizAtual[i] = matrizAtual[i], matrizAtual[c]
            	    

if __name__ == "__main__":
    main()