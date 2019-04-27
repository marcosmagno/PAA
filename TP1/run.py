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
        for k,v in graph.items():
            if k not in self.vertex:
                self.vertex.append(k)
            for i in v:
                if i not in self.vertex:
                    self.vertex.append(i)


        for v in self.vertex:
            cc.append(-1)

        for v in self.vertex:
            try:
                if(cc[v-1] == -1):
                    self.id = self.id +1
                    """ call dfsRcc """
                    print("enviando vertice", v)
                    self.dfsRcc(graph, cc, v, self.id)
            except IndexError as identifier:
                pass
        return self.id
            

    def dfsRcc(self,graph, cc, v, id):
        print("dfsRcc", v)
        #time.sleep(1)
        cc[v-1] = id
        print(cc)
        try:
            for a in graph[v]:
                print("adja", a)
                if(cc[a-1] == -1):
                    self.dfsRcc(graph, cc, a, id)
                    print(cc)

        except KeyError as identifier:
            pass
            
def main():
    node = Node()
    components = Related_Components()
    vector = [] 
    """ exemplo 1 """
    node.set_adjacency_list(1,2)
    node.set_adjacency_list(1,3)
    node.set_adjacency_list(1,4)
    node.set_adjacency_list(4,5)
    node.set_adjacency_list(6,8)
    node.set_adjacency_list(6,9)
    node.set_adjacency_list(6,10)
    node.set_adjacency_list(7,8)
    node.set_adjacency_list(7,9)
    node.set_adjacency_list(7,10)
    node.set_adjacency_list(11,12)
    node.set_adjacency_list(12,13)
    node.set_adjacency_list(13,14)
    node.set_adjacency_list(14,15)
    node.set_adjacency_list(16,17)
    node.set_adjacency_list(17,18)
    node.set_adjacency_list(18,19)
    node.set_adjacency_list(20,20)
    node.set_adjacency_list(21,22)
    node.set_adjacency_list(21,23)
    node.set_adjacency_list(23,22)
    
    """ exemplo 2 """
    """
    node.set_adjacency_list(1,8)
    node.set_adjacency_list(8,7)
    node.set_adjacency_list(7,6)
    node.set_adjacency_list(6,5)
    node.set_adjacency_list(5,4)
    node.set_adjacency_list(4,3)
    node.set_adjacency_list(3,2)
    node.set_adjacency_list(2,1)
    node.set_adjacency_list(9,10)
    node.set_adjacency_list(10,11)
    node.set_adjacency_list(11,12)
    node.set_adjacency_list(12,13)
    node.set_adjacency_list(13,14)
    node.set_adjacency_list(14,9)
    node.set_adjacency_list(15,16)
    node.set_adjacency_list(16,17)
    node.set_adjacency_list(17,18)
    node.set_adjacency_list(18,19)
    """
    print(node.get_adjacency_list())
    print(components.UGRAPHcc(node.get_adjacency_list(), vector))

   # print(node.get_node())
    
    

































if __name__ == "__main__":
    main()