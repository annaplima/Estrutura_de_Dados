#Implementar um algoritmo para validar a parentização em expressões matemáticas
#{2+3-[5+(2-1)]+0}
#{2+3-[5+(2-1)]+0]
#{2+3-[5+2-1)]+0}
#{2+3-(5+2-1)]+0}
from abc import ABC, abstractmethod

class IPilha(ABC):
        @abstractmethod
        def empilha(self, valor):
            if valor == '{' or valor == '[' or valor == '(':
                self.v[self.topo] = valor
                self.topo += 1
                print(self.v)
            else:
                return False
        @abstractmethod
        def confere(expr : str):
            pilha = []
            for i in range(len(expr)):
                if expr[i] == '{' or expr[i] == '[' or expr[i] == '(':
                    pilha.append(expr[i])
                else:
                    if expr[i] == '}' or expr[i] == ']' or expr[i] == ')':
                        if len(pilha) != 0:
                            if (pilha[-1] == '{' and expr[i]== '}') or (pilha[-1] == '[' and expr[i] == ']') or (pilha[-1] == '(' and expr[i] == ')'):
                             pilha.pop(-1)
                            else:
                                return False
                        else:
                            return False

            if len(pilha) == 0:
                return True
            else:
                return False
        

exp = input()
while(True):
  try:
    print(IPilha.confere(exp))
    exp = input()
  except EOFError as e: 
    break
