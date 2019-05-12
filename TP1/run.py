import time
import sys
"""
Input
    Multiplas naves de maneira conjunta
    N = Numero de postos de combate encontrados pelo radar
    M = Quantidade total de teleporte possíveis entre postos de combate

    Mlinhas
        a = 
        b = 

    Nlinhas
        c =
        d = 


Exemplo:
    15 14


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

    def UGRAPHcc(self, graph, cc):
        self.qt_componente_conexa = 0
        self.indexAdja = 0
        self.Transportadores = 0
        self.Reconhecimento = 0
        self.Frigatas = 0
        self.Bombardeiros = 0
        self.countVertice = 0
        self.countAresta = 0
        for v in range(1, self.qt_vertex + 1): # M + 1
            cc.append(-1)

        for v in range(1, self.qt_vertex + 1): # M + 1
            try:
                if(cc[v-1] == -1):
                    self.qt_componente_conexa = self.qt_componente_conexa +1                    
                    """ call dfsRcc """
                    self.singleGraph = {}
                    self.countAresta = 0
                    self.countVertice = 0
                    returnDfs = self.dfsRcc(graph, cc, v, self.qt_componente_conexa)
                    qt_ships = self.check_ships(returnDfs, self.countVertice)
            except IndexError as identifier:
                pass
        return str(self.qt_componente_conexa) + "-" + str(qt_ships)

    def dfsRcc(self,graph, cc, v, id):
        cc[v-1] = id
        self.singleGraph[v] = []
        self.singleGraph[v] = graph[v]
        self.countVertice = self.countVertice + 1
        try:
            for a in graph[v]:
                if(cc[a-1] == -1):
                    self.dfsRcc(graph, cc, a, id)
        except KeyError as identifier:
            pass
        return self.singleGraph
        
    def check_ships(self, graph, numberVertice):
        grau = []
        soma = 0
        for k, v in graph.items():
            grau.append(len(v))

        # Reconhece nave do tipo Transportadores
        # Se todos os vertices tiverem grau 2, entao, e um Transportador    
        if (all(s == 2 for s in grau)):
            self.Transportadores = self.Transportadores + 1

        for i in grau:
            soma = soma + i

        # Reconhece nave do tipo Reconhecimento
        # Se todos os vertires a partir da segunda posicao ate a penultima,
        # tiverem grau 2, entao, eh um caminho simples, portanto, uma nave do tipo Reconhecimento
        if grau[0] == 1 and grau[-1] == 1:
            del grau[0]
            del grau[-1]
            if (all(s == 2 for s in grau)):
                self.Reconhecimento = self.Reconhecimento + 1
        
        if grau[0] != grau[-1] or 3 in grau or 5 in grau or 6 in grau:
            if (numberVertice >= int(soma/2)):
                self.Frigatas = self.Frigatas + 1

        
        return str(self.Reconhecimento) + "-" + str(self.Frigatas) + "-" + str(self.Bombardeiros) + "-" + str(self.Transportadores)

        

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

            Output
                R,F,B e T  
                    R = Nave de reconhecimento 
                    F = Nave Frigatas  
                    B = Nave bombardeiros  
                    T = Naves Transporte
                V = Tempo de vantagem que sua frota possui                
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

    # Naves
    Transportadores = 0
    Reconhecimento = 0
    Frigatas = 0
    Bombardeiros = 0
    sum_qtComponents = 0

    for i in range(0, int(qt_teleportes)):
        var = obj_file.readline()
        node.set_adjacency_list(int(var.split(" ")[0]), int(var.split(" ")[1]))
    qt_Components = components.UGRAPHcc(node.get_adjacency_list(), vector)

    Reconhecimento = qt_Components.split("-")[1]
    Frigatas = qt_Components.split("-")[2]
    Bombardeiros = qt_Components.split("-")[3]
    Transportadores = qt_Components.split("-")[4]
    sum_qtComponents = int(Reconhecimento) + int(Frigatas) + int(Bombardeiros) + int(Transportadores)
    Bombardeiros = int(qt_Components.split("-")[0]) - int(sum_qtComponents)
    
    print(str(Reconhecimento) + " " + str(Frigatas) + " " + str(Bombardeiros) + " " + str(Transportadores))
if __name__ == "__main__":
    main()