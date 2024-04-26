"""
Implementar Fila Dinâmica Encadeada

Operações:

E -  Enfileira
D - Desenfileira
I   - Imprime
"""



from abc import ABC, abstractmethod

class IFila(ABC):
  @abstractmethod
  def inserir(self, valor): ...

  @abstractmethod
  def varrer(self): ...

  @abstractmethod
  def acessar(self): ...
    
  @abstractmethod
  def excluir(self): ...


class Node():
    def __init__(self, i):
        self.info = i
        self.prox = None

class filaencad():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir(self, node):
        if not self.primeiro:
            self.primeiro = node
            self.ultimo = node
            return

        self.ultimo.prox = node
        self.ultimo = node
        return

    def varrer(self):
        node = self.primeiro
        while node:
            print(node.info,end=" ")
            node = node.prox
        print()

    def acessar(self):
        if self.primeiro:
            return self.primeiro.info

    def excluir(self):
        if not self.primeiro:
                return
        j =  self.primeiro.prox
        self.primeiro.prox = None
        self.primeiro = j
        return


fila = filaencad()

menu = 'v'

while menu != 'X':
  menu = input("")
  
  if menu == "E":
    num = Node(int(input()))
    fila.inserir(num)
  elif menu == "D":
    print("Valor desenfileirado:",fila.acessar())
    fila.excluir()
  elif menu =="I":
    fila.varrer()
  elif menu =="A":
    print(fila.acessar())