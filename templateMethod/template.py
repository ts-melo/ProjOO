from abc import ABC, abstractmethod
from functools import cmp_to_key

#classe abstrata, o template
class Comparator(ABC):
    #o template method, define o esqueleto da comparação
    def compare(self, p1, p2):
        val1 = self.extract_value(p1)
        val2 = self.extract_value(p2)
        #base operation
        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:
            return 0
    
    #esse é a parte que varia, cada subclasse implementa de forma diferente
    #required_operations
    @abstractmethod
    def extract_value(self, p):
        if not p:
            return''
        else:
            return p.lower() #minuscula para comparação case-insensitive
        pass


class UltimaLetra(Comparator):
    #sobrescreve comportamento padrão para ordenar pela ultima letra
    def extract_value(self, p):
        if not p:
            return''
        return p[-1].lower() #minuscula para comparação case-insensitive
    
class Tamanho(Comparator):
    #sobreescreve comportamento padrão para ordenar pelo tamanho da string
    def extract_value(self, p):
        return len(p)

#se quisesse implementar outro jeito de comparação, por exemplo, ordenação por numero de vogais
# basta criar uma nova classe que herda de Comparator e implementar o método extract_value para contar as vogais e retornat o total de vogais
# o "esqueleto" la na classe comparator que vai pegar esse numero retornado e usar para fazer a ordenação
 

if __name__ == "__main__":
    palavras = ["banana", "abacaxi", "uva", "laranja", "melancia"]
    print("Original:", palavras)
    print("-" * 30)
    a = palavras.copy()
    a.sort()

    #ordenar pela ultima letra
    palavras_ultima_letra = sorted(palavras, key=cmp_to_key(UltimaLetra().compare))
    print("Ordenado pela última letra:", palavras_ultima_letra)
    
    print("-" * 30)

    #ordenar pelo tamanho
    palavras_tamanho = sorted(palavras, key=cmp_to_key(Tamanho().compare))
    print("Ordenado pelo tamanho:", palavras_tamanho)