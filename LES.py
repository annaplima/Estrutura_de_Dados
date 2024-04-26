"""
Criar uma lista estática sequencial e implementar um menu para interação com a mesma de acordo com o exemplo ilustrado abaixo.

O Tamanho da LES é 5

Atenção: É necessário, pelo menos, 1 herança e 1 sobrecarga de método.


I    <-- Insere
1    <-- Número 1
R    <-- Remove
0    <-- Índice 0
B    <-- Busca
1    <-- Número 1 
P    <-- Imprime toda a lista
X    <-- Sai do programa
"""




from abc import ABC, abstractmethod

class ILista(ABC):
  @abstractmethod
  def insere(self, num): ...
    
  @abstractmethod
  def busca(self, num): ...

  @abstractmethod
  def remove(self, idx): ...
    
  @abstractmethod
  def __repr__(self): ...
    
class LES(ILista):
  def __init__(self):
    self.v = [None]*5
    self.n = 0

  def insere(self, num):
    if(self.n < 5):
      i = 0
      while i < self.n and num > self.v[i]:
        i+=1
  
      for j in range(self.n-1, i-1, -1):
        self.v[j+1] = self.v[j]
  
      self.v[i] = num
      self.n += 1
      print("inserido")
    else:
      print("erro")

  def busca(self, num):
    x = 0
    for i in range (self.n):
      if(num == self.v[i]):
        x = 1

    if(x == 1):
      print("encontrado")
    else:
      print("nao encontrado")
        
    
  def remove(self, idx): 
    if(idx > self.n or idx < 0 or self.n == 0):
      print("erro")
    else:
        self.v.pop(idx)
        print("removido")
        self.n -= 1
  
  def __repr__(self):
    return ' '.join([str(x) for x in self.v if x!= None])


                    
menu = input()
classe = LES()

while menu != "X":
  if(menu == "I" or menu == "i"):
    num = int(input())
    LES.insere(classe, num)
  elif(menu == "R" or menu == "r"):
    num = int(input())
    LES.remove(classe, num)
  elif(menu == "P" or menu == "p"):
    print(classe)
  elif(menu == "B" or menu == "b"):
    num = int(input())
    LES.busca(classe, num)
  

  menu = input()
  


