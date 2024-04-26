"""
Implementar o método Run da classe BFS

VI
1
VI
2
VI
3
VI
4
VI
5
VI
6
VI
7
VI
8
AI
1
3
1.1
AI
3
5
1.1
AI
2
4
1.1
AI
6
7
1.1
AI
1
6
1.1
AI
5
7
1.1
AI
4
1
1.1
P
B
S
4
PP
D
7
X
P
VR
4
P
B
S
1
PP
X
X
GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> GRA> =============================
V1:V3(1.1)  V6(1.1)
V2:V4(1.1)
V3:V5(1.1)
V4:V1(1.1)
V5:V7(1.1)
V6:V7(1.1)
V7:
V8:
=============================
GRA> BFS>
BFS> ===========================
1  : P=4    D=1
2  : P=-1   D=-1
3  : P=1    D=2
4  : P=-1   D=0
5  : P=3    D=3
6  : P=1    D=2
7  : P=6    D=3
8  : P=-1   D=-1
===========================
BFS> 3
BFS>
GRA> =============================
V1:V3(1.1)  V6(1.1)
V2:V4(1.1)
V3:V5(1.1)
V4:V1(1.1)
V5:V7(1.1)
V6:V7(1.1)
V7:
V8:
=============================
GRA> GRA> =============================
V1:V3(1.1)  V6(1.1)
V2:
V3:V5(1.1)
V5:V7(1.1)
V6:V7(1.1)
V7:
V8:
=============================
GRA> BFS>
BFS> ===========================
1  : P=-1   D=0
2  : P=-1   D=-1
3  : P=1    D=1
5  : P=3    D=2
6  : P=1    D=1
7  : P=6    D=2
8  : P=-1   D=-1
===========================
BFS>
GRA>

"""



import os
import stat
from abc import ABC, abstractmethod
from typing import List
from queue import Queue
import sys

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
        self.adjList.append([])
        return False

    def delVertice(self, v: Vertice) -> bool:
        arestasParaRemover = []
        for i, vert in enumerate(self.vertices):
            for j, aresta in enumerate(self.adjList[i]):
                if aresta.para == v:
                    arestasParaRemover.append((i,aresta))

        for i,a in arestasParaRemover:
            self.adjList[i].remove(a)
        pos = next((i for i, vv in enumerate(self.vertices) if vv == v))
        self.vertices.remove(v)
        self.adjList.pop(pos)
        return True

    def addAresta(self, a: Aresta) -> bool:
        vertFrom = next((i for i, v in enumerate(self.vertices) if a.de == v))
        # vertTo = [i for i,a in enumerate(vertices) if e.para==a]

        self.adjList[vertFrom].append(a)
        return True

    def delAresta(self, a: Aresta) -> bool:
        self.adjList[a.de].remove(a)
        return True

    def print(self):
        print("=============================")
        for v in self.getVertices():
            print(f"V{v.value}:", end="")
            for a in self.getArestas(v):
                print(f"V{a.para.value}({a.value})  ", end="")
            print()
        print("=============================")


class BFS:
    def __init__(self, grafo: IGrafo):
        self.grafo = grafo
        self.dists = {}
        self.pai = {}

    def run(self, v: Vertice):
      fila = [v]
      arestas = self.grafo.getArestas(v)
      self.pai[v] = None
      self.dists[v] = 0


      while len(fila) != 0:
        atual = fila.pop(0)
        arestas = self.grafo.getArestas(atual)

        for i in arestas:
          if i.para not in self.pai:
            self.pai[i.para] = i.de
            self.dists[i.para] = self.dists[i.de] + 1
            fila.append(i.para)

    def getPai(self, v: Vertice):
        return self.pai[v] if v in self.pai else None

    def getDist(self, v: Vertice):
        return self.dists[v] if v in self.dists else -1


class GerenciadorBFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.BFS = BFS(self.grafo)
        self.prompt = "BFS> "

    def run(self):
        f = int(input())
        v = next((i for i in self.grafo.getVertices() if i.value == f))
        self.BFS.run(v)
        print("")

    def getPai(self):
        vertice = int(input())
        v = next((i for i in self.grafo.getVertices() if i.value == vertice))
        vPai: Vertice = self.BFS.getPai(v)
        print(vPai.value if vPai is not None else "NULL")

    def getDistancia(self):
        vertice = int(input())
        v = next((i for i in self.grafo.getVertices() if i.value == vertice))
        dist: int = self.BFS.getDist(v)
        print(dist)

    def printAll(self):
        print("===========================")
        for v in self.grafo.getVertices():
            vPai: Vertice = self.BFS.getPai(v)
            vDist = self.BFS.getDist(v)
            print("%-3d: P=%-3d  D=%-3d" % (v.value, vPai.value if vPai is not None else -1, vDist))
        print("===========================")

    def loop(self):
        funcoes = {
            'S': self.run,
            'P': self.getPai,
            'D': self.getDistancia,
            'PP': self.printAll,
        }
        while True:
            print(self.prompt, end="")
            cmd = input()
            if cmd in funcoes:
                funcoes[cmd]()
            else:
                break


class Gerenciador:
    g = Grafo()

    def __init__(self):
        self.prompt = "GRA> "

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

    def VI(self):
        valor = int(input())
        self.adicionaVertice(valor)

    def VR(self):
        valor = int(input())
        self.removeVertice(valor)

    def AI(self):
        valorDe = int(input())
        valorPara = int(input())
        peso = float(input())
        self.adicionaAresta(valorDe, valorPara, peso)

    def AR(self):
        valorDe = int(input())
        valorPara = int(input())
        self.removeAresta(valorDe, valorPara)

    def P(self):
        self.imprime()

    def BFS(self):
        bfs = GerenciadorBFS(self.g)
        bfs.loop()
        print("")

    def loop(self):
        funcoes = {
            'VI': self.VI,
            'VR': self.VR,
            'AI': self.AI,
            'AR': self.AR,
            'P': self.P,
            'B': self.BFS
        }
        try:
            while True:
                print(self.prompt, end="")
                cmd = input()
                if cmd in funcoes:
                    funcoes[cmd]()
                else:
                    break
        except EOFError:
            ...


gerenciador = Gerenciador()
gerenciador.loop()