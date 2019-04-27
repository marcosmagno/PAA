import time
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
    def UGRAPHcc(self, graph, cc):
        self.vertex = []
        self.id = 0
        index = 0
        self.indexAdja = 0
        
        """ TODO: improve this"""
        #for k,v in graph.items():
        #    if k not in self.vertex:
        #        self.vertex.append(k)
        #    for i in v:
        #        if i not in self.vertex:
        #            self.vertex.append(i)
        

        for v in range(1, 100001): # M + 1
            cc.append(-1)

        for v in range(1, 100001): # M + 1
            try:
                if(cc[v-1] == -1):
                    self.id = self.id +1
                    """ call dfsRcc """
                    self.dfsRcc(graph, cc, v, self.id)
            except IndexError as identifier:
                pass
        print(cc)
        return self.id
            

    def dfsRcc(self,graph, cc, v, id):
        cc[v-1] = id
        try:
            for a in graph[v]:
                if(cc[a-1] == -1):
                    self.dfsRcc(graph, cc, a, id)
        except KeyError as identifier:
            pass

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
    node = Node()
    components = Related_Components()
    file_ = Input()
    vector = [] 
    obj_file = file_.read_file("tests/in/10.in")
    first_line = obj_file.readline()
    qt_teleportes = first_line.split(" ")[1]
    qt_local_tripulante = first_line.split(" ")[0]
    for i in range(0, int(qt_teleportes)):
        var = obj_file.readline()
        node.set_adjacency_list(int(var.split(" ")[0]), int(var.split(" ")[1]))
    qt_Components = components.UGRAPHcc(node.get_adjacency_list(), vector)
    print(qt_Components)
    #print(vector)
   
    
    

































if __name__ == "__main__":
    main()