import time
import sys
"""
Input
    Multiplas navaes de maneira conjunta
    N = Numero de postos de combate encontrados pelo radar
    M = Quantidade total de teleporte possíveis entre postos de combate

    Mlinhas
        a = 
        b = 

    Nlinhas
        c =
        d = 

Output
    R,F,B e T  
        R = Nave de reconhecimento 
        F = Nave Frigatas  
        B = Nave bombardeiros  
        T = Naves Transporte
    V = Tempo de vantagem que sua frota possui


Exemplo:
    15 14

Ref: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/components.html
"""

class Node(object):
    def __init__(self):
        self.adjacency_list = dict()
    
    def set_adjacency_list(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []    
        self.adjacency_list[u].append(v)        
        self.adjacency_list[v].append(u)


    def get_adjacency_list(self):
        return self.adjacency_list


class Related_Components(object):
    
    def __init__(self, qt_vertex):
        self.qt_vertex = qt_vertex

    def UGRAPHcc(self, graph, cc):
        self.id = 0
        self.indexAdja = 0
        self.Transportadores = 0
        self.Reconhecimento = 0
        for v in range(1, self.qt_vertex + 1): # M + 1
            cc.append(-1)

        for v in range(1, self.qt_vertex + 1): # M + 1
            try:
                if(cc[v-1] == -1):
                    self.id = self.id +1                    
                    """ call dfsRcc """
                    self.singleGraph = {}
                    color = []
                    returnDfs = self.dfsRcc(graph, cc, v, self.id)
                    qt_transportadores = self.check_Transportadores(returnDfs)
                    print("qt_ transportadores", qt_transportadores)
                    newg = returnDfs.copy()
                    self.UGRAPHtwoColor(newg, color)
            except IndexError as identifier:
                pass
        return self.id

    def dfsRcc(self,graph, cc, v, id):
        cc[v-1] = id
        self.singleGraph[v] = []
        self.singleGraph[v] = graph[v]
        try:
            for a in graph[v]:
                if(cc[a-1] == -1):
                    self.dfsRcc(graph, cc, a, id)
        except KeyError as identifier:
            pass
        
        return self.singleGraph
        
    def check_Transportadores(self, graph):
        grau = []
        for k, v in graph.items():
            grau.append(len(v))
        if (all(s == 2 for s in grau)):
            self.Transportadores = self.Transportadores + 1  
        
        
        if grau[0] == 1 and grau[-1] == 1:
            del grau[0]
            del grau[-1]
            #print("Depois",grau)
            if (all(s == 2 for s in grau)):
                self.Reconhecimento = self.Reconhecimento + 1
        
        return str(self.Transportadores) + " - " + str(self.Reconhecimento)

    def UGRAPHtwoColor(self, graph, color):
        for i in range(1, len(graph) + 1):
            color.append(-1)

        for v in range(1, len(graph) + 1):
            if color[v - 1] == -1:
                if (self.dfsRcolor(graph, v, color, 0) == False):
                    return False
                else:
                    return True

    def dfsRcolor(self, graph, v, color, c):
        color[v - 1] = c 
        i = v - 1
        print("VERTICE", v)
        print("COLOR", color)
        print("GRAPH", graph)
        for a in graph.values():
            
            w = a[i]
            i + 1 
            print("VARIAVEL A", a)
            print("VARIAVEL W", w)
            if(color[w - 1] == -1):
                print("CHAMOU REC DFS")
                self.dfsRcolor(graph, w, color, 1-c)
            elif(color[w] == c):
                return False
        return True
        

class Input(object):

    def read_file(self, file_name):
        """ Entrada
            10 <= N <= 1000000  Numero de posto de combate
            9  <= M <= 10000000 Quantidade de teleportes
            M linhas : teleportes possíveis
                1 <= a <= N
                1 <= b <= N

            N linhas : O tripulante c deve retornar para o posto correto d
                1 <= c <= N
                1 <= d <= N
        """
        get_file = open(file_name,"r")
        return get_file

def main():
    """ TODO improve variavel name"""
    file_ = Input()
    file_recv = sys.argv[1]
    obj_file = file_.read_file(str(file_recv))
    first_line = obj_file.readline()
    qt_teleportes = first_line.split(" ")[1]
    qt_local_tripulante = first_line.split(" ")[0]
    node = Node()
    components = Related_Components(int(qt_local_tripulante))
    vector = []
    
    for i in range(0, int(qt_teleportes)):
        var = obj_file.readline()
        node.set_adjacency_list(int(var.split(" ")[0]), int(var.split(" ")[1]))
    qt_Components = components.UGRAPHcc(node.get_adjacency_list(), vector)
    print(qt_Components)

if __name__ == "__main__":
    main()