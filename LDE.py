
""" 
mplementar LDE conforme exemplo

 Atenção: É necessário, pelo menos, 1 herança e 1 sobrecarga de método.


I    <-- Insere
1    <-- Número 1
R    <-- Remove
0    <-- Índice 0
B    <-- Busca
1    <-- Número 1 
P    <-- Imprime toda a lista
N    <-- Mostra o total de itens na lista
X    <-- Sai do programa
"""


from abc import abstractmethod, ABC
from typing import Optional


class ILista(ABC):
    @abstractmethod
    def insere(self, v: int) -> bool:
        ...

    @abstractmethod
    def remove(self, idx: int) -> bool:
        ...

    @abstractmethod
    def busca(self, valor: int) -> bool:
        ...

    @abstractmethod
    def imprime(self) -> None:
        ...

    @abstractmethod
    def total(self) -> None:
        ...


class No:
    def __init__(self, valor: int, proximo: Optional['No']):
        self.valor = valor
        self.proximo = proximo


class LDE(ILista):
    def __init__(self):
        self.n = 0
        self.primeiro: Optional[No] = None

    def insere(self, valor):
        novo = No(valor, None)

        anterior, atual = None, self.primeiro
        while atual and atual.valor < valor:
            anterior = atual
            atual = atual.proximo

        novo.proximo = atual
        if anterior is not None:
            anterior.proximo = novo
        else:
            self.primeiro = novo

        self.n += 1
        return True

    def remove(self, idx):
          # atual = self.primeiro
      #if idx == 0:
       #     atual = self.proximo 
      #else:
       # anterior = None
        #atual = self.primeiro

        if idx < 0 or idx >= self.n:
            print("Indice %d nao removido" % idx)
            return False

        anterior = None
        atual = self.primeiro
        for i in range(idx):
            anterior = atual
            atual = atual.proximo

        if (anterior == None):
            self.primeiro = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print("Indice %d removido" % idx)
        del (atual)
        self.n -= 1
        return True

    def busca(self, valor):
         #atual = self.primeiro
      #while atual and atual.num != num: 
            #atual = atual.proximo
           # if atual and atual.num == num:
        atual = self.primeiro
        for i in range(self.n):
            if (atual.valor == valor):
                print("Encontrado")
                return True
            atual = atual.proximo

        print("Nao encontrado")
        return False

    def imprime(self):
        atual = self.primeiro
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo

        print("")

    def total(self):
        print("Total:", self.n)


menu = input()
classe = LDE()

while menu != "X":
    if (menu == "I"):
        num = int(input())
        LDE.insere(classe, num)
    elif (menu == "P"):
        LDE.imprime(classe)
    elif (menu == "B"):
        num = int(input())
        LDE.busca(classe, num)
    elif (menu == "R"):
        num = int(input())
        LDE.remove(classe, num)
    elif (menu == "N"):
        LDE.total(classe)
    menu = input()
