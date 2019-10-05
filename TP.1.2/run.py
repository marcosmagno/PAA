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

class Node(object):
    def __init__(self):
        self.adjacency_list = dict()
    
    def set_adjacency_list(self, u, v):
        """ 
            Cria lista de Adjacencia
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []    
        self.adjacency_list[u].append(v)        
        self.adjacency_list[v].append(u)


    def get_adjacency_list(self):
        return self.adjacency_list


class Related_Components(object):
    """
        Implementa o calculo de componentes conexas
        O algoritmo aqui utilizado, temos como referencia o site abaixo:
            Ref: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/components.html
    """
    def __init__(self, qt_vertex):
        self.qt_vertex = qt_vertex

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
    graph = {}
    for p in permutacao([1,2,3,4,5,6,7,8,9]):
    #for p in permutacao([1,2,3,4]):
        i = i + 1
        dic_permutacao[i] = list(p)
    #create_Graph(dic_permutacao, 2, 2)
    create_Graph(dic_permutacao, 3, 3)

#n linhas m colunas
def create_Graph(p, l, c):
    tmp = []
    matriz = []
    matrizResultante = []
    controleLinha = 0
    for k, v in p.items():
        n = l
        matriz = []
        len_l = len(v)
        for i in range(n):
            start = int(i*len_l/n)
            end = int((i+1)*len_l/n)
            matriz.append(v[start:end])
        print("\n\n\n\n")
        print("Vetor Inicial", k, v)
        # permutacoes
        
        for i in range(0,l):
            for j in range(0,c-1):
                
                matrizResultante = [lst[:] for lst in matriz] #copy.deepcopy(matriz)
                #print(matriz[i][j])
                #print(matriz[i][j+1])
                aux = matriz[i][j] # 1
                matrizResultante[i][j] = matriz[i][j+1] #2
                matrizResultante[i][j+1] = aux
                print("Matriz Inicial Horizontal: ", matriz)
                espande_Permutacao(matrizResultante)

                #print("matriz Trocada", matrizResultante)

        #print("\n")
        for i in range(0,l-1):
            for j in range(0,c):
                matrizResultante = [lst[:] for lst in matriz] #copy.deepcopy(matriz)
                aux = matriz[i][j] # 1
                matrizResultante[i][j] = matriz[i+1][j] #3
                matrizResultante[i+1][j] = aux
                print("Matriz Inicial Vertical: ", matriz)
                espande_Permutacao(matrizResultante)
                                
        
        


def espande_Permutacao(matrizResultante):
    
    print("matriz Trocada", matrizResultante)
    time.sleep(2)

    

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