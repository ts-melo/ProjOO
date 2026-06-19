from abc import ABC

class OrdenadorTemplate(ABC):
    def ordenar(self, lista: list) -> list:
        n = len(lista)
        lista_copia = lista.copy()
        
        for i in range(n):
            for j in range(0, n - i - 1):
                
                val1 = self.extract_value(lista_copia[j])
                val2 = self.extract_value(lista_copia[j+1])
                
                if val1 > val2:
                    lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]
                    
        return lista_copia

    def extract_value(self, p: str):
        
        if not p: 
            return ''
        return p.lower()


class OrdenadorAlfabetico(OrdenadorTemplate):
    
    pass


class OrdenadorUltimaLetra(OrdenadorTemplate):
    
    def extract_value(self, p: str):
        if not p: 
            return ''
        return p[-1].lower()
    

class OrdenadorTamanho(OrdenadorTemplate):
    
    def extract_value(self, p: str):
        return len(p)

def client_code(ordenador: OrdenadorTemplate, lista: list) -> None:

    # Executa o Template Method
    resultado = ordenador.ordenar(lista)
    print(resultado)


if __name__ == "__main__":
    palavras = ["kiwi", "abacaxi", "uva", "morango", "banana", "laranja"]
    
    print("--- LISTA ORIGINAL ---")
    print(palavras)
    print("\n" + "="*40 + "\n")

    #Ordem Alfabética
    client_code(OrdenadorAlfabetico(), palavras)
    print("-" * 50)

    #Última Letra
    client_code(OrdenadorUltimaLetra(), palavras)
    print("-" * 50)

    # Tamanho

    client_code(OrdenadorTamanho(), palavras)
    print("-" * 50)