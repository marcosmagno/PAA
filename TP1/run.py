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
"""

class Node(object):
    def __init__(self):
        self.adjacency_list = dict()
    
    def set_adjacency_list(self, u, v):
        
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def get_adjacency_list(self):
        return self.adjacency_list


class Related_Components(object):

    def UGRAPHcc(self, graph, cc):
        self.vertex = []
        self.id = 0
        index = 0
        self.indexAdja = 0


        """ TODO improve this"""
        for k,v in graph.items():
            if k not in self.vertex:
                self.vertex.append(k)
            for i in v:
                if i not in self.vertex:
                    self.vertex.append(i)


        for v in self.vertex:
            cc.append(-1)

        for v in self.vertex:
            if(cc[index] == -1):
                self.id = self.id +1
                """ call dfsRcc """ 
                self.dfsRcc(graph, cc, index, self.id)
            index = index + 1
        print("IDDDD", self.id)

    def dfsRcc(self,graph, cc, index, id):
        cc[index] = id
        
        for k,adjv in graph.items():
            for a in adjv:
                print("a", a)
                print("Index", self.indexAdja)
                print("cc", cc[self.indexAdja])
                time.sleep(2)
                if (cc[self.indexAdja] == -1):
                    self.dfsRcc(graph, cc, self.indexAdja, id)
                    print("k,a", k, a)
        self.indexAdja = self.indexAdja + 1





            
def main():
    node = Node()
    components = Related_Components()
    vector = []
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
    node.set_adjacency_list(14,15)

    components.UGRAPHcc(node.get_adjacency_list(), vector)

   # print(node.get_node())
    
    

































if __name__ == "__main__":
    main()