import time
import sys
import copy
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
    def set_adjacency_list(self,u, v):
        """ 
            Cria lista de Adjacencia
        """
        #print(u, v)

        if v not in self.graph:
            self.graph[v] = [[u,2]]
        else:
            self.graph[v].append([u,2])    
        
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
    i = 0
    dic_permutacao = {}
    
    #for p in permutacao([1,2,3,4,5,6,7,8,9]):
    #for p in permutacao([1,2,3,4,5,6,7,8]):
    for p in permutacao([1,2,3,4]):
        i = i + 1
        dic_permutacao[str(p)] = i
    create_Graph(dic_permutacao, 2, 2)
   
    #create_Graph(dic_permutacao, 3, 3)
    #create_Graph(dic_permutacao, 4, 2)

#n linhas m colunas
def create_Graph(permutations, l, c):
    matriz = []
    matrizResultante = []
    graph = Graph()
    #print(permutations)
    for k, v in permutations.items():
        n = l
        r = k.replace("[","")
        r = r.replace("]","")
        resultList = list(map(int, r.split(",")))
        #resultList = [1,2,3,4,5,6,7,8,9]
        matriz = [resultList[i:i+c] for i in range(0, len(resultList), c)]
        #print("\n\n\n")
        #print(k, v)
        #matriz = [[1,2,3],[3,4,6],[7,8,9]]
        #len_l = len(v)
        #for i in range(n):
        #    start = int(i*len_l/n)
        #    end = int((i+1)*len_l/n)
        #    matriz.append(v[start:end])
        # permutacoes

        for i in range(0,l):
            for j in range(0,c-1):
                #matrizResultante = [lst[:] for lst in matriz] #copy.deepcopy(matriz)
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
                graph.set_adjacency_list(u,v)

                #print("matriz Trocada ", matriz)

                aux = matriz[i][j]
                matriz[i][j] = matriz[i][j+1]
                matriz[i][j+1] = aux


        for i in range(0,l-1):
            for j in range(0,c):
                #matrizResultante = [lst[:] for lst in matriz] #copy.deepcopy(matriz)
                #print("Matriz Inicial Vertical: ", matriz)
                #print("Custo Troca", matriz[i][j]+ matriz[i+1][j])
                aux = matriz[i][j] # 1
                matriz[i][j] = matriz[i+1][j] #3
                matriz[i+1][j] = aux
                u = espande_Permutacao(matriz,permutations)
                graph.set_adjacency_list(u,v)
                aux = matriz[i][j]
                matriz[i][j] = matriz[i+1][j]
                matriz[i+1][j] = aux     

    for k, v in graph.get_graph().items():
        print(k, v)

def relax(u, v, w):
    """
        if v.d > u.d + w(u,v)
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