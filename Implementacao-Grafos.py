from abc import ABC, abstractmethod
from typing import List

class Vertice:
  value: int

  def __init__(self, value):
    self.value = value


class Aresta:
  de: Vertice
  para: Vertice
  value: float

  def __init__(self, de: Vertice, para: Vertice, value: float):
    self.de = de
    self.para = para
    self.value = value


class IGrafo(ABC):
  @abstractmethod
  def getVertices(self) -> List[Vertice]: ...

  @abstractmethod
  def getArestas(self, v: Vertice) -> List[Aresta]: ...

  @abstractmethod
  def addVertice(self, v: Vertice) -> bool: ...

  @abstractmethod
  def delVertice(self, v: Vertice) -> bool: ...

  @abstractmethod
  def addAresta(self, a: Aresta) -> bool: ...

  @abstractmethod
  def delAresta(self, a: Aresta) -> bool: ...

  @abstractmethod
  def print(self): ...


class Grafo(IGrafo):
  adjList: List[List[Aresta]] = list()
  vertices: List[Vertice] = list()

  def getVertices(self) -> List[Vertice]:
    return self.vertices

  def getArestas(self, v: Vertice) -> List[Aresta]:
    return self.adjList[self.vertices.index(v)]

  def addVertice(self, v: Vertice) -> bool:
    self.vertices.append(v)
    self.adjList.append(list())
    return True

  def delVertice(self, v: Vertice) -> bool: 
    idx = self.vertices.index(v)
    self.vertices.remove(v)
    self.adjList.pop(idx)

    indices = []
  
    for i in range (len(self.adjList)):
      for j in range(len(self.adjList[i])):
        if self.adjList[i][j].de == v or self.adjList[i][j].para == v:
          indices.append((i, j))
  
    for i, j in indices:
      self.adjList[i].pop(j)
      
    return True
      
  def addAresta(self, a: Aresta) -> bool:
    achouDe = False
    achouPara = False
    for i in range(len(self.vertices)):
      if a.de == self.vertices[i]:
        achouDe = True
        idx = i
      if a.para == self.vertices[i]:
        achouPara = True

    if achouDe == False or achouPara == False:
      return False

    self.adjList[idx].append(a)
    
    return True

  def delAresta(self, a: Aresta) -> bool:
    indices = []
    for i in range (len(self.adjList)):
      for j in range(len(self.adjList[i])):
        if self.adjList[j] == a:
          indices.append((i,j))

    for i, j in indices:
      self.adjList[i].pop(j)
      
    return True

  def print(self):
    print("=============================")
    for v in self.getVertices():
      print(f"V{v.value}:", end="")
      for a in self.getArestas(v):
        print(f"V{a.para.value}({a.value})  ", end="")
      print()
    print("=============================")


class Gerenciador:
  g = Grafo()

  def buscaVerticePorValor(self, valor: int) -> Vertice:
    return next((x for x in self.g.getVertices() if x.value == valor), None)

  def buscaArestaPorNos(self, de: int, para: int) -> Aresta:
    vert = self.buscaVerticePorValor(de)
    return next((x for x in self.g.getArestas(vert) if x.para == para), None)

  def adicionaVertice(self, valor: int):
    self.g.addVertice(Vertice(valor))

  def adicionaAresta(self, valorDe: int, valorPara: int, peso: float):
    de = self.buscaVerticePorValor(valorDe)
    para = self.buscaVerticePorValor(valorPara)
    novaAresta = Aresta(de, para, peso)
    self.g.addAresta(novaAresta)

  def removeVertice(self, valor):
    vert = self.buscaVerticePorValor(valor)
    self.g.delVertice(vert)

  def removeAresta(self, valorDe: int, valorPara: int):
    aresta = self.buscaArestaPorNos(valorDe, valorPara)
    self.g.delAresta(aresta)

  def imprime(self):
    self.g.print()


gerenciador = Gerenciador()


def VI():
  valor = int(input())
  gerenciador.adicionaVertice(valor)


def VR():
  valor = int(input())
  gerenciador.removeVertice(valor)


def AI():
  valorDe = int(input())
  valorPara = int(input())
  peso = float(input())
  gerenciador.adicionaAresta(valorDe, valorPara, peso)


def AR():
  valorDe = int(input())
  valorPara = int(input())
  gerenciador.removeAresta(valorDe, valorPara)


def P():
  gerenciador.imprime()


funcoes = {
  'VI': VI,
  'VR': VR,
  'AI': AI,
  'AR': AR,
  'P': P
}

while True:
  cmd = input()
  if cmd in funcoes:
      funcoes[cmd]()
  else:
      break
