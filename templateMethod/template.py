from abc import ABC, abstractmethod
from functools import cmp_to_key

#classe abstrata, o template
class Comparator(ABC):
    #o template method, define o esqueleto da comparação
    def compare(self, p1, p2):
        val1 = self.extract_value(p1)
        val2 = self.extract_value(p2)

        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:
            return 0
    
    #esse é a parte que varia, cada subclasse implementa de forma diferente
    @abstractmethod
    def extract_value(self, p):
        pass

class UltimaLetra(Comparator):
    def extract_value(self, p):
        if not p:
            return''
        return p[-1].lower() #minuscula para comparação case-insensitive
    
class Tamanho(Comparator):
    def extract_value(self, p):
        return len(p)