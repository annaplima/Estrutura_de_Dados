"""Implementar a Lista Dinâmica Duplamente Encadeada de acordo com as instruções abaixo.

Cada linha da entrada (stdin) corresponde a um comando seguida por nenhum ou mais parâmetros. 

O sistema deve inicializar 10 LDDEs. Cada lista é representada por um índice que vai de 0 até 9 (inclusive).

Comandos:

I    <-- Insere ...
1    <-- Número 1 (parâmetro do insere)
R    <-- Remove ...
0    <-- Índice 0 (parâmetro do remove)
B    <-- Busca ...
1    <-- Número 1 (parâmetro da busca)
P    <-- Imprime toda a lista
O    <-- Imprime toda a lista do fim para o início
N    <-- Mostra o total de itens na lista
S    <-- Seleciona lista ...
0    <-- de índice 0 (parâmetro do Seleciona)
J    <-- Junta na lista atual ...
1    <-- os elementos da lista de índice 1 (parâmetro do junta)
X    <-- Sai do programa

Obs:
A lista selecionada por padrão (no início da aplicação) é a de índice 0
A operação Junta coloca todos os elementos da lista do índice informado na lista atualmente selecionada.

Assim, as operações abaixo:
I
1
I
3
S
1
I
2
I
10
S
0
J
1
P

Deve produzir a seguinte saí
"""




from abc import abstractmethod, ABC
from typing import Optional

class ILista(ABC):
    @abstractmethod
    def insere(self, v: int) -> bool:...

    @abstractmethod
    def remove(self, idx: int) -> bool: ...

    @abstractmethod
    def busca(self, valor: int) -> bool:...

    @abstractmethod
    def imprime(self) -> None: 
        ...
    @abstractmethod
    def contrario(self) -> None:
        ...
    @abstractmethod
    def total(self) -> None:
        ...
    @abstractmethod
    def junta(self) -> None:
        ...
    @abstractmethod
    def seleciona(self) -> None:
        ...

    
class No:
    def __init__(self, anterior: Optional['No'], valor: int,proximo: Optional['No']):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior 


class LDDE(ILista):
    def __init__(self):
        self.n = 0
        self.primeiro: Optional[No] = None
        self.ultimo: Optional[No] = None

    def insere(self, valor):
        novo = No( None,valor, None)
        
        anterior, atual = None, self.primeiro
        while atual and atual.valor < valor:
            anterior = atual
            atual = atual.proximo
            

        novo.proximo = atual
        novo.anterior = anterior
        
        if anterior is not None:
            anterior.proximo = novo
        else:
            self.primeiro = novo
        
        if atual is not None:
            atual.anterior = novo
        else:
            self.ultimo = novo

        

        self.n += 1
        return True
    

    def remove(self, idx: int):
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

    def imprime(self):
            atual = self.primeiro
            while atual:
                print(atual.valor, end=" ")
                atual = atual.proximo
            print("")    

    def contrario(self) -> None:
        atual = self.ultimo
        while atual:
            print(atual.valor, end=" ")
            atual = atual.anterior


        print("")

    def busca(self, valor: int):
      atual = self.primeiro
      cont = 0

      while atual and cont < self.n:
        
        if atual.valor == valor:
          print("Encontrado o valor %d"% atual.valor)
          return True 
        else:
          atual = atual.proximo
        cont +=1
      print("Nao Encontrado o valor %d"% valor)
      return False

    def total(self):
        print("Total:", self.n)

    def seleciona(self, indice):
          return indice
    
    def quantidade(self):
        return print("Total:", self.n)

    def junta(self,indice):
        lista_inserir = l[indice]
        inicio = lista_inserir.primeiro
      
        while inicio:
            l[sele].insere(inicio.valor)
            inicio = inicio.proximo
      
l = []
for i in range(10):
  x = LDDE()
  l.append(x)

menu = 'v'
sele = 0

while menu != 'X':
  menu = input("")
  
  if menu == "I":
    l[sele].insere(int(input()))
  elif menu == "P":
    l[sele].imprime()
  elif menu == "R":
    l[sele].remove(int(input()))
  elif menu == "B":
    l[sele].busca(int(input()))
  elif menu == "N":
    l[sele].quantidade()
  elif menu == "O":
    l[sele].contrario()
  elif menu == "S":
    sele = l[sele].seleciona(int(input()))
  elif menu == 'J':
    l[sele].junta(int(input()))