from IMediator import ChatMediator

class ChatRoom(ChatMediator):
    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def enviar_mensagem(self, remetente, mensagem):
        for user in self._usuarios:
            if user != remetente:
                user.receber_mensagem(mensagem)

class Usuario:
    def __init__(self, mediator, nome):
        self.mediator = mediator
        self.nome = nome
    
    def enviar_mensagem(self, mensagem):
        print(f"{self.nome} envia : {mensagem}")
        self.mediator.enviar_mensagem(self, mensagem)

    def receber_mensagem(self, mensagem):
        print(f"{self.nome} recebe : {mensagem}")

