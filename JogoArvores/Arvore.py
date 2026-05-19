
class EspecieArvore:
    def __init__(self, nome_especie, textura_2d):
        self._nome_especie = nome_especie
        self._textura_2d = textura_2d

        @property
        def nome(self):
            return self._nome_especie
        
        @property
        def textura(self):
            return self._textura_2d
        
        #info extrinseca
        def renderizar(self, x, y, altura, diametro, galhos):
            print(f"Renderizando {self._nome_especie} na posição ({x}, {y}) com altura {altura}, diâmetro {diametro} e {galhos} galhos usando a textura '{self._textura_2d}'.")
