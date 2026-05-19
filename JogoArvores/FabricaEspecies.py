from Arvore import EspecieArvore

class FabricaEspecies:
    _especies = {}

    @classmethod
    def get_especie(cls, nome_especie):
        if nome_especie not in cls._especies:
            textura = f"Textura_{nome_especie}.png"
            cls._especies[nome_especie] + EspecieArvore(nome_especie, textura)

        return cls._especies[nome_especie]
    
    