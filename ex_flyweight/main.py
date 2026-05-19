import random

class Algarismo:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def __str__(self):
        return str(self._valor)

class FabricaAlgarismos:
    _instancias = {}
    @classmethod
    def get_algarismo(cls, valor):
        if valor not in cls._instancias:
            cls._instancias[valor] = Algarismo(valor)
        return cls._instancias[valor]
    @classmethod
    def total_instancias(cls):
        return len(cls._instancias)

class NumeroDezAlgarismos:
    def __init__(self):
        self._algarismos = []
        for _ in range(10):
            rand_dig = random.randint(0,9)
            self._algarismos.append(FabricaAlgarismos.get_algarismo(rand_dig))

    def __str__(self):
        return "".join(str(alg) for alg in self._algarismos)

if __name__ == "__main__":
    lista_numeros = []

    for i in range(1,11):
        num = NumeroDezAlgarismos()
        lista_numeros.append(num)
        print(f"Número {i}: {num}")

    print(f"\nTotal de instâncias de Algarismo criadas: {FabricaAlgarismos.total_instancias()}")    

    dig = random.randint(0,9)
    occ = []
    for num in lista_numeros:
        for alg in num._algarismos:
            if alg.valor == dig:
                occ.append(alg)
    
    if len(occ) > 0:
        primeira_instancia = occ[0]
        ref = id(primeira_instancia)

        for i, inst in enumerate(occ):
            print(f" ocorrencia {i+1} -> {id(inst)}")
        msm_obj = all(inst is primeira_instancia for inst in occ)
        if msm_obj:
            print(f"-> SUCESSO! Apesar de aparecer {len(occ)} vezes nos textos, existe apenas UMA única instância do '{dig}' ocupando a memória. Todas as ocorrências apontam para o ID: {ref}.")