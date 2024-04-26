"""
Implementar a árvore AVL (balanceada). Imprimir os nós no formato:   

valor (altura)
"""





from abc import ABC, abstractmethod
from typing import Optional

class BTNode:
  parent: Optional["BTNode"]
  left: Optional["BTNode"]
  right: Optional["BTNode"]
  value: int
  fator: int

  def __init__(self, value):
    self.parent = None
    self.left = None
    self.right = None
    self.value = value
    self.height = 0
    self.fator = 0

  def numChildren(self):
    return sum([self.left is not None, self.right is not None])

class IBinTree(ABC):
  @abstractmethod
  def insert(self, value) -> bool:
    ...

  @abstractmethod
  def remove(self, node: BTNode) -> bool:
    ...

  @abstractmethod
  def search(self, value) -> Optional[BTNode]:
    ...

  @abstractmethod
  def printInOrder(self):
    ...

class BinTree(IBinTree):
  rootNode: Optional[BTNode] = None
  total: int = 0

  def insert(self, value) -> bool:
    novo = BTNode(value)
    atual = self.rootNode
    anterior = None

    while atual is not None:
      anterior = atual
      if value <= atual.value:
        atual = atual.left
      else:
        atual = atual.right

    novo.parent = anterior
    if anterior is not None:
      if value <= anterior.value:
        anterior.left = novo
        self.altura(novo)
        self.fatorBalanceamento(novo)
        self.balanceamento(novo)
      else:
        anterior.right = novo
        self.altura(novo)
        self.fatorBalanceamento(novo) 
        self.balanceamento(novo)
    else:
      self.rootNode = novo
      self.altura(novo)
      self.fatorBalanceamento(novo)
      self.balanceamento(novo)

    self.total += 1
    return True

  def sucessor(self, node: BTNode) -> BTNode:
    node = node.right
    while node.left is not None:
      node = node.left
    return node
  
  def removeSemFilhos(self, node: BTNode, lado: str):
    if lado == "raiz":
      self.rootNode = None
    elif lado == "esquerdo":
      node.parent.left = None
    else:
      node.parent.right = None
      
    self.altura(node.parent)
    self.fatorBalanceamento(node.parent)
    self.balanceamento(node.parent)
    self.total -= 1
    #pdb.set_trace()
    return True
    

  def removeUmFilho(self, node: BTNode, lado: str):
    unicoFilho = node.left
    if unicoFilho is None:
      unicoFilho = node.right
    
    pai = node.parent
    if lado == "raiz":
      self.rootNode = unicoFilho
      unicoFilho.parent = pai
      self.altura(unicoFilho)
      self.fatorBalanceamento(unicoFilho)
      self.balanceamento(unicoFilho)
    elif lado == "esquerdo":
      node.parent.left = unicoFilho
      unicoFilho.parent = pai
      self.altura(unicoFilho)
      self.fatorBalanceamento(unicoFilho)
      self.balanceamento(unicoFilho)
    else:
      node.parent.right = unicoFilho
      unicoFilho.parent = pai
      self.altura(unicoFilho)
      self.fatorBalanceamento(unicoFilho)
      self.balanceamento(unicoFilho)

    self.total -= 1
    #pdb.set_trace()
    return True
    
    
  def removeDoisFilhos(self, node: BTNode, lado: str):
    sucessor = self.sucessor(node)
    pai = sucessor.parent
    node.value = sucessor.value #essa linha tem que ficar acima, tava invertido
    self.remove(sucessor) #essa linha tem que ficar abaixo, tava invertido
    self.altura(pai) #faltou recalcular no pai a altura
    self.fatorBalanceamento(pai)
    self.balanceamento(pai) #faltou recalcular no pai o balanceamento
    #pdb.set_trace()
    return True
    

  def remove(self, node: BTNode) -> bool:
    if self.total == 0:
      return False

    if node.parent is None:
      lado = "raiz"
    else:
      lado = node.parent.right
      if lado is not None and lado.value == node.value:
        lado = "direito"
      else:
        lado = "esquerdo"

    if node.numChildren() == 0:
      self.removeSemFilhos(node, lado)
      return True

    elif node.numChildren() == 1:
      self.removeUmFilho(node, lado)
      return True

    else:
      self.removeDoisFilhos(node, lado)
      return True

    #pdb.set_trace()
    return False
    

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

  def turnLeft(self, no: BTNode):
    pivo = no.right
    b = pivo.left

    pivo.parent = no.parent
    if self.rootNode == no:
      self.rootNode = pivo
    else:
      if (no.parent.right is not None) and (no.parent.right == no):
        no.parent.right = pivo
      else:
        no.parent.left = pivo
    no.parent = pivo
    no.right = b
    pivo.left = no
    if b is not None:
      b.parent = no

    self.altura(no)
    self.fatorBalanceamento(no)

  def turnRight(self, no: BTNode):
    pivo = no.left
    b = pivo.right

    pivo.parent = no.parent
    if self.rootNode == no:
      self.rootNode = pivo
    else:
      if (no.parent.right is not None) and (no.parent.right == no):
        no.parent.right = pivo
      else:
        no.parent.left = pivo
    no.parent = pivo
    no.left = b
    pivo.right = no
    if b is not None:
      b.parent = no

    self.altura(no)
    self.fatorBalanceamento(no)

  def altura(self, node:BTNode):
    while node is not None:
      if node.left is None:
        le = -1
      else:
        le = node.left.height
      if node.right is None:
        ld = -1
      else:
        ld = node.right.height
      node.height = max(le,ld)+1
      node = node.parent
    #pdb.set_trace()

  def fatorBalanceamento(self, node:BTNode):
    while node is not None:
      le = -1
      ld = -1
      if node.left is not None:
        le = node.left.height
      if node.right is not None:
        ld = node.right.height
      node.fator = ld - le
      node = node.parent
    #pdb.set_trace()
    

  def balanceamento(self, node:BTNode):
    #vc inverteu as condicoes e n colocou = em algumas comparacoes
    while node is not None:
      fator = node.fator
      if fator >= 2:
        if node.right is not None: #a condicao aqui estava left, tem que ser right
          fatorFilho = (node.right.fator)#aqui tava left tbm
          if fatorFilho <= -1: #aqui tem que ser <=  e tava so <
            self.turnRight(node.right)#a condicao deve ser right pq ele q ta girando
        self.turnLeft(node)
      elif fator <= -2:
        if node.left is not None:#aqui tava invertido tbm com o right no lugar
          fatorFilho = (node.left.fator)#aqui tbm
          if fatorFilho >= 1:#aqui tbm é >= e tava so >
            self.turnLeft(node.left)#aqui tava certo kk
        self.turnRight(node)
      node = node.parent
    #pdb.set_trace()
      

  def printSubTreeInOrder(self, node: Optional[BTNode]):
    if node is None:
      return

    self.printSubTreeInOrder(node.left)
    print("%d (%d)" %(node.value, node.height))
    self.printSubTreeInOrder(node.right)

  def printInOrder(self):
    print("=====================================")
    self.printSubTreeInOrder(self.rootNode)
    print("=====================================")

class TestClass:
    tree = BinTree()

    def insert(self):
        value = int(input())
        self.tree.insert(value)

    def remove(self):
        value = int(input())
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