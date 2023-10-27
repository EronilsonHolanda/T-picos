
class Tree:
    def __init(self):
        self.root = None
    #}__init__
    def dfs(self, valor): #Busca em Profundidade
        pass
    #}dfs
    def bfs(self, valor): #Busca em Largura
        fila = []
        if self.root is not None:
            fila.append(self.root)
            
        while len(fila) > 0:
            node_atual = fila[0]
            del(fila[0])
            if node_atual.value == valor:
                return node_atual
            else:
                if node_atual.childLeft is not None:
                    fila.append(node_atual.childLeft)
                if node_atual.childRight is not None:
                    fila.append(node_atual.childRight)
        return None
    #}bfs  
    def print(self):
        if self.root is not None:
            self.root.print()
    
#}class Tree
