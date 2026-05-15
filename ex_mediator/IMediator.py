from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, mensagem, usuario):
        pass

    @abstractmethod
    def add_colleague(self, usuario):
        pass