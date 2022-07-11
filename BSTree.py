#REFERENCIA = https://github.com/python-cafe/data_structures/blob/master/arvores/tree.py

#Binary Serach Tree
from Node import Node

class BSTree:
    
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, label):
        ## CRIANDO O NODO QUE SERAH INSERIDO (objeto da classe -node-)
        node = Node(label)
        #current_node = None
        #node_d = None

        ##verificando se a arvore esta vazia , ou nao
        if self.empty(): ##raiz eh o nodo que esta sendo inserido
            self.root = node
        else:
            # arvore nao esta vazia - insercao sera realizada de forma recursiva
            node_d = None
            current_node = self.root

            while True: #se repete ate o meu caso base (node == null)

                #1 - etapa do fluxo do percurso
                if current_node != None: #cheguei no caso base, aqui vou inserir

                    node_d = current_node

                    #verifica se eh maior ou menor - se vai para direita ou para esquerda
                    if node.getLabel() < current_node.getLabel(): #esquerda
                        current_node = current_node.getLeft()
                    else: #vai para direita
                        current_node = current_node.getRight()

                # 2 - para encontrar onde deve ser inserido, ate que o nodo atual seja none
                else: #current_node eh NONE --> eh para realizar a insercao
                    #insere ou na direita, ou na esquerda
                    if node.getLabel() < node_d.getLabel(): 
                        #insercao na esquerda do pai
                        node_d.setLeft(node)
                    else:
                        #insercao na direita do pai
                        node_d.setRight(node)
                    break #sai do grupo
         
    def search(self, label):
        return self._search(label, self.getRoot() )

    def _search(self, label, node):

        if node is None:
            print("\n", label, "não encontrado")
            return node

        if node.getLabel() == label:
            print("\n", node.label, "encontrado")
            return node

        if label < node.getLabel():
            return self._search(label, node.getLeft())
        else:
            return self._search(label, node.getRight())

    def empty(self):
        if self.root == None: #se a raiz nao existe
            return True #sim, a arvore esta vazia
        return False

    #metodo pre-ordem para percorrer : raiz, esquerda, direita
    def showTree(self, current_node):
        if current_node != None:
            print('%d' % current_node.getLabel(), end=' ')
            self.showTree(current_node.getLeft())
            self.showTree(current_node.getRight())

    def min(self, node = 0):
        if node == 0:
            node = self.getRoot()
        while node.getLeft():
            node = node.getLeft()
        return node.getLabel()

    def remove(self, label):
        return self._remove(label, self.root)

    def _remove(self, label, node):
        ## 1 CASO: se o nodo a ser removido NAO TEM FILHOS - folha
        ######### CASO MAIS SIMPLES: so preciso setar/apontar o pai (do nodo removido) para NONE

        if node is None:
            return node
        
        # Se o valor for menor, desce à esquerda
        if label < node.getLabel():
            node.setLeft(self._remove(label, node.getLeft()))

        # Se o valor for maior, desce à direita
        elif label > node.getLabel():
            node.setRight(self._remove(label, node.getRight()))
           
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()
            else:
                ### 3 CASO: nodo a ser removido tem DOIS FILHOS
                ###### DEVE PEGAR O MENOR ELEMENTO DA SUBARVORE DA DIREITA
                
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.getRight())
                # Ao invés de trocar a posição dos nós, troca o valor
                node.setlabel(substitute) 
                # Depois, remove o substituto da subárvore à direita
                node.setRight(self.remove(substitute, node.getRight())) 

        return node
    
    ### METODO DE REMOCAO 
    ### 3 CASOS 
    

    ## 2 CASO: nodo a ser removido tem UM FILHO APENAS
    ##### o filho do nodo removido PASSA PARA O LUGAR DELE - FILHO SOBE DE NIVEL 






            
    






