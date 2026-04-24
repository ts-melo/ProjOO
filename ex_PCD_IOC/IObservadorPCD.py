from abc import ABC, abstractmethod

class IObservadorPCD(ABC):
    ##define que qqr interessao tem q ter o metodo atualizar
    #a interface que define o metodo de callback. A IOC acontece porque o observador não chama o dado, ele só espera ser chamado de volta
    @abstractmethod
    def atualizar(self, nome_pcd, temp, ph, umidade):
        pass
