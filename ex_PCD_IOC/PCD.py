from IObservadorPCD import IObservadorPCD
class PCD:
    def __init__(self, nome):
        self.nome = nome
        # IoC: A lista começa vazia. As dependências serão "injetadas" depois, externamente.
        self._observadores = []

    def registrar_interesse(self, observador: IObservadorPCD):
        """
        INJEÇÃO DE DEPENDÊNCIA:
        Em vez da PCD criar a universidade, nós 'injetamos' a universidade pronta aqui dentro.
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    #assim que os dados mudam, o modelo dispara o evento para notificar
    def set_medicoes(self, temp, ph, umidade):
        print(f"\n[Sinal de Sensor] {self.nome} captou novos dados.")
        self._notificar(temp, ph, umidade)

    def _notificar(self, temp, ph, umidade):
        """
        HOLLYWOOD PRINCIPLE: 'Don't call us, we'll call you'.
        Os observadores não perguntam os dados. A PCD 'liga de volta' 
        para eles quando algo muda. O modelo percorre os observadoes e chala o callback 'atualizar'
        """
        for obs in self._observadores:
            obs.atualizar(self.nome, temp, ph, umidade)