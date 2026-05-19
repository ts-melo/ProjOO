class ArvoreNoMapa:
    __slots__ = [ 'x', 'y', 'altura', 'diametro', 'galhos', 'especie']

    def __init__(self, x, y, altura, diametro, galhos, especie):
        self.x = x
        self.y = y
        self.altura = altura
        self.diametro = diametro
        self.galhos = galhos
        self._especie = especie

    def desenhar(self):
        return self._especie.renderizar(self.x, self.y, self.altura, self.diametro, self.galhos)
    
