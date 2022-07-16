#REFERENCIA = https://github.com/python-cafe/data_structures/blob/master/arvores/tree.py

from Node import Node

class BSTree:
    
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, label):
        
        if self.root == None:
            return self._insert(label)

        elif self.search(label):
            print("Já existe esse valor na arvore.")
            return False

        return self._insert(label)

    def _insert(self, label):
        node = Node(label)

        if self.root is None:
            self.root = node
        else:

            node_d = None
            current_node = self.root

            while True:

                if current_node != None:

                    node_d = current_node
                    
                    if node.getLabel() < current_node.getLabel():
                        current_node = current_node.getLeft()
                    else:
                        current_node = current_node.getRight()

                else:

                    if node.getLabel() < node_d.getLabel(): 
                        node_d.setLeft(node)
                    else:
                        node_d.setRight(node)

                    return node
         
    def search(self, label):
        if(not self.empty()):
            return self._search(label, self.getRoot())

    def _search(self, label, node):

        if node is None:
            return node

        if node.getLabel() == label:
            return node

        if label < node.getLabel():
            return self._search(label, node.getLeft())
        else:
            return self._search(label, node.getRight())

    def empty(self):
        if self.root == None:
            print("Arvore esta vazia.")
            return True
        return False

    def showTreePreOrder(self):
        if (not self.empty()):
            return self._showTreePreOrder(self.root)

    def _showTreePreOrder(self, node):
        if node != None:
            print('%d' % node.getLabel(), end=' ')
            self._showTreePreOrder(node.getLeft())
            self._showTreePreOrder(node.getRight())

    def showTreePosOrder(self, node=None):

        if(self.empty()):
            return

        if node is None:
            node = self.root

        if node.getLeft():
            self.showTreePosOrder(node.getLeft())

        if node.getRight():
            self.showTreePosOrder(node.getRight())

        print('%d' % node.getLabel(), end=' ')

    def showTreeInOrder(self, node=None):

        if(self.empty()):
            return

        if node is None:
            node = self.root

        if node.getLeft():
            self.showTreeInOrder(node.getLeft())
        print('%d' % node.getLabel(), end=' ')

        if node.getRight():
            self.showTreeInOrder(node.getRight())

    def min(self, node=0):
        if node == 0:
            node = self.root

        while node.getLeft():
            node = node.getLeft()

        return node.getLabel()

    def remove(self, label):
        if(not self.empty()):
            return self._remove(label, self.root)

    def _remove(self, label, node):

        if node is None:
            print(f"\nElemento {label} nao encontrado")

            return node

        if label < node.getLabel():
            node.setLeft(self._remove(label, node.getLeft()))

        elif label > node.getLabel():
            node.setRight(self._remove(label, node.getRight()))

        else:

            if node.getLeft() is None:
                return node.getRight()

            elif node.getRight() is None:
                return node.getLeft()

            else:

                substitute = self.min(node.getRight())

                node.setLabel(substitute)

                node.setRight(self._remove(substitute, node.getRight()))

        return node

    def showConnections(self, node=None):

        if (self.empty()):
            return

        if node is None:
            node = self.root

        if node.getLeft() and node.getRight() and not node == self.root:
            print(f"{node.getLabel()} -> {node.getLeft().getLabel()}")
            print(f"{node.getLabel()} -> {node.getRight().getLabel()}")

        if node.getLeft():
            if not node.getRight() or node == self.root:
                print(f"{node.getLabel()} -> {node.getLeft().getLabel()}")
            self.showConnections(node.getLeft())

        if node.getRight():
            if not node.getLeft() or node == self.root:
                print(f"{node.getLabel()} -> {node.getRight().getLabel()}")
            self.showConnections(node.getRight())







            
    






