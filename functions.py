def insertNewData(treeBinary):
    try:
        newData = int(input("\nDigite um novo elemento para inserção:"))

        result = treeBinary.insert(newData)

        if result:
            print(f"Elemento adicionado com sucesso: Elemento {newData}")
            
        return
    except:
        print("Arvore somente de numeros. Digite um numero\n")
        insertNewData(treeBinary)


def searchNewData(treeBinary):
    try:
        if (not treeBinary.empty()):
            chooseSearch = int(input("\nDigite um elemento para procurar: "))

            result = treeBinary.search(chooseSearch)
            
            if result:
                print(f"Elemento {result.getLabel()} encontrado")
            
            else:
                print("Elemento não encontrado")
            return

    except:
        print("Arvore somente de numeros. Digite um numero.\n")
        searchNewData(treeBinary)


def showPreOrder(treeBinary):
    print("\nLista elementos em pre-ordem:")
    treeBinary.showTreePreOrder()
    print("\n")


def showPosOrder(treeBinary):
    print("\nLista elementos em pos-ordem:")
    treeBinary.showTreePosOrder()

def showInOrder(treeBinary):
    print("\nLista elementos em ordem:")
    treeBinary.showTreeInOrder()

def removeData(treeBinary):
    try:
        if (not treeBinary.empty()):
            chooseDelete = int(input("\nDigite o dado para exclusão:"))

            treeBinary.remove(chooseDelete)

            return

    except:
        print("Arvore somente de numeros. Digite um numero.\n")
        removeData(treeBinary)


def showConnectionsData(treeBinary):

    print("\nLigações da arvore: ")

    treeBinary.showConnections()

def menu(treeBinary):
    choose = int(input(
        "\n\n 1 - Inserir dados \n 2 - Buscar dados \n 3 - Deletar dados \n 4 - Listar elementos em pre-ordem \n 5 - Listar elementos pos-ordem \n 6 - Listar elementos em ordem \n 7 - Exibir ligações \n 8 - Finalizar programa\n Oque você deseja realizar?"))

    if choose == 1:
        insertNewData(treeBinary)

    elif choose == 2:
        searchNewData(treeBinary)

    elif choose == 3:
        removeData(treeBinary)

    elif choose == 4:
        showPreOrder(treeBinary)

    elif choose == 5:
        showPosOrder(treeBinary)

    elif choose == 6:
        showInOrder(treeBinary)

    elif choose == 7:
        showConnectionsData(treeBinary)

    elif choose == 8:
        print("Finalizando programa")
        return

    else:
        print("Não possui essa escolha. Digite novamente")

    menu(treeBinary)