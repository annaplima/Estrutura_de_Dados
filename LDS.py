"""mplementar a Lista Dinâmica Sequencial de acordo com o exemplo abaixo.

Comandos:

I   - Insere um valor
R   - Remove por índice
B   - Busca por um valor e retorna "Encontrado" ou "Nao Encontrado"
C   - Mostra a capacidade da lista
N   - Mostra a quantidade de elementos cadastrados na lista
P   - Imprime a lista
S   - Aumentar ou diminuir a capacidade da lista e mostra "Reservado" ou "Erro na reserva". O erro vai ocorrer caso a nova capacidade seja menor que a quantidade de elementos
F   - Diminuir a capacidade para caber todos os elementos já cadastrados"""
 



from abc import ABC, abstractmethod
import string

class ILista(ABC):
  @abstractmethod
  def insere(self, num): ...
    
  @abstractmethod
  def busca(self, num): ...

  @abstractmethod
  def remove(self, idx): ...
    

  @abstractmethod
  def capacid(self): ...

  @abstractmethod
  def quantid(self): ...

  @abstractmethod
  def reserve(self): ...

    

class LDS(ILista):
  def __init__(self):
    self.n = 0
    self.cap = 2
    self.v = [None]*self.cap
  
  def insere(self, num):
        if (self.n == self.cap):
          self.realocar(self.cap * 2)

        pos = 0
        for i in range(self.n):
            if(self.v[pos] < num):
                pos+=1

    
        for j in range(self.n, pos-1, -1):
            self.v[j] = self.v[j-1]

        self.v[pos] = num
        self.n += 1
   
    
  def busca(self, num):
        x = 0
        for i in range (self.n):
            if(num == self.v[i]):
                x = 1

        if(x == 1):
            print("Encontrado")
        else:
            print("Nao Encontrado")
    

  def remove(self, idx):

    if(idx > self.n or idx < 0 or self.n == 0):
          pass
    else:
        for i in range(idx, self.n-1):
          self.v[i] = self.v[i + 1];
        self.n -= 1
  
  def __repr__(self):
        return ' '.join([str(x) for idx, x in enumerate(self.v) if x!= None and idx < self.n])

  def quantid(self):
    print("Quantidade:", self.n)

  def capacid(self):
        print("Capacidade:", self.cap)

  
  ##pass

  def realocar(self, novaCapacidade):
      if(novaCapacidade >= self.n):
        self.cap = novaCapacidade
        v_novo = [None]*self.cap
      for i in range (self.n):
        v_novo[i] = self.v[i]
  
      self.v = v_novo
      return "Reservado"

  def reserve(self):
    self.realocar(self.n)
    print("Capacidade ajustada")

menu = input()
classe = LDS()

while menu != "X":
  if(menu == "I"):
    num = int(input())
    LDS.insere(classe, num)
  elif(menu == "P"):
    print(classe)
  elif(menu == "B"):
    num = int(input())
    LDS.busca(classe, num)
  elif(menu == "R"):
    num = int(input())
    LDS.remove(classe, num)
  elif(menu == "C"):
    LDS.capacid(classe)
  elif(menu == "N"):
    LDS.quantid(classe)
  elif(menu == "S"):
    num = int(input())
    print(LDS.realocar(classe, num))
  elif(menu == "F"):
    LDS.reserve(classe)
  menu = input()