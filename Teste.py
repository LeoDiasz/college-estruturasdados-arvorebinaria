from BSTree import BSTree

tree = BSTree()

tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(15)
tree.insert(25)
tree.insert(7)

tree.showTree(tree.getRoot())

tree.search(30)

tree.remove(6)
tree.showTree(tree.getRoot())


