
"""
Implementar as operações Insert, Search e Remove da árvore binária de busca. (sem balanceamento)
"""



from abc import ABC, abstractmethod
from typing import Optional


class BTNode:
    parent: Optional["BTNode"]
    left: Optional["BTNode"]
    right: Optional["BTNode"]
    value: int

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        #isleft child

    def numChildren(self):
        return sum([self.left is not None, self.right is not None])


class IBinTree(ABC):

    @abstractmethod
    def insert(self, value) -> bool: ...

    @abstractmethod
    def remove(self, node: BTNode) -> bool: ...

    @abstractmethod
    def search(self, value) -> Optional[BTNode]: ...

    @abstractmethod
    def printInOrder(self): ...


class BinTree(IBinTree):
    rootNode: Optional[BTNode] = None
    total: int = 0

    def insert(self, value) -> bool:
      new = BTNode(value)
      ptrActual = self.rootNode
      ptrPrev = None
  
      while( ptrActual is not None):
        ptrPrev = ptrActual
        if value <= ptrActual.value:
          ptrActual = ptrActual.left 
        else:
          ptrActual = ptrActual.right
        
      new.parent = ptrPrev
      if ptrPrev is not None:
        if  value <= ptrPrev.value:
          ptrPrev.left = new   
        else:
          ptrPrev.right = new
      else:
        self.rootNode = new
      
      self.total +=1
      return True

    def sucessor(self, node: BTNode) -> BTNode:
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    def remove(self, node: BTNode) -> bool:
      if node.parent == None:
        lado = "raiz"
      elif node.parent.left is not None and node.value == node.parent.left.value:
        lado = "esquerdo"
      else:
        lado = "direito"
#CASO SEM FILHO
      if node.numChildren() == 0:
        if lado == "raiz":
          self.rootNode = None
          self.total -=1
          return True
        elif lado == "esquerdo":
          node.parent.left = None
          self.total -=1
          return True
        else:
          node.parent.right = None
          self.total -=1
          return True          
          
#CASO COM UM FILHO
      elif node.numChildren() == 1:
        crianca = node.left
        if crianca == None:
          crianca = node.right
          
        if lado == "raiz":
          self.rootNode = crianca
          crianca.parent = None
          self.total -=1
          return True
          
        elif lado == "esquerdo":
          node.parent.left = crianca
          crianca.parent = node.parent
          self.total -=1
          return True
          
        else:
          node.parent.right = crianca
          crianca.parent = node.parent
          self.total -=1
          return True       
#CASO COM DOIS FILHOS
      else:
        sucessor = self.sucessor(node)
        node.value = sucessor.value
        self.remove(sucessor)
        return True 


    def search(self, value) -> Optional[BTNode]:
        actual = self.rootNode
        while actual is not None:
            if value < actual.value:
                actual = actual.left
            elif value > actual.value:
                actual = actual.right
            else:
                return actual

        return None

    def printSubTreeInOrder(self, node: Optional[BTNode]):
        if node is None:
            return

        self.printSubTreeInOrder(node.left)
        print(node.value)
        self.printSubTreeInOrder(node.right)

    def printInOrder(self):
        print("==============================")
        self.printSubTreeInOrder(self.rootNode)
        print("==============================")


class TestClass:
    tree = BinTree()

    def insert(self):
        value = input()
        self.tree.insert(value)

    def remove(self):
        value = input()
        node: Optional[BTNode] = self.tree.search(value)
        if node is not None:
            self.tree.remove(node)

    def print(self):
        self.tree.printInOrder()


def test():
    t = TestClass()
    commands = {"I": t.insert, "R": t.remove, "P": t.print}
    while True:
        cmd = input()
        if cmd == 'X':
            break
        commands[cmd]()


test()

