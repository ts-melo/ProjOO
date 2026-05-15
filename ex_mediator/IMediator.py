from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def enviar_mensagem(self, mensagem, usuario, sala):
        pass

    @abstractmethod
    def adicionar_usuario(self, usuario, sala):
        pass