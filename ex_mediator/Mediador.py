from IMediator import ChatMediator
from datetime import datetime

class ChatRoom(ChatMediator):
    def __init__(self):
        self._usuarios = []
        self._historico = []

    def adicionar_usuario(self, usuario):
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)
            print(f"{usuario.nome} entrou na sala de chat.")


    def enviar_mensagem(self, mensagem : str, remetente: 'Usuario'):
        registro = f"[ {datetime.now().strftime('%H : %M')} ] {remetente.nome}: {mensagem}"
        self._historico.append(registro)

        for user in self._usuarios:
            if user != remetente:
                user.receber_mensagem(mensagem, remetente.nome)

class Usuario:
    def __init__(self, mediator, nome):
        self.mediator = mediator
        self.nome = nome
    
    def enviar_mensagem(self, mensagem: str):
        print(f"{self.nome} envia : {mensagem}")
        self.mediator.enviar_mensagem(mensagem, self)

    def receber_mensagem(self, mensagem: str, de_quem: str):
        print(f"{self.nome} recebeu de {de_quem}: {mensagem}")

