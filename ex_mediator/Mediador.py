from IMediator import ChatMediator
from datetime import datetime

class ChatRoom(ChatMediator):
    def __init__(self):
        self._salas = {}

    def adicionar_usuario(self, usuario, sala):
        if sala not in self._salas:
            self._salas[sala] = { "usuarios": [] , "historico": [] }
        self._salas[sala]["usuarios"].append(usuario)
        print(f"{usuario.nome} entrou na sala de chat {sala}.")

    def enviar_mensagem(self, mensagem: str, remetente: 'Usuario', sala):
        if sala in self._salas:
            # Registro do histórico
            registro = f"[{datetime.now().strftime('%H:%M')}] {remetente.nome}: {mensagem}"
            self._salas[sala]["historico"].append(registro)
            
            # Loop correto acessando a chave 'usuarios'
            for user in self._salas[sala]["usuarios"]:
                if user != remetente:
                    # Ordem: mensagem, nome do autor, nome da sala
                    user.receber_mensagem(mensagem, remetente.nome, sala)
                    
    def mostrar_historico(self, sala):
        if sala in self._salas:
            print(f"\n--- HISTÓRICO DA SALA: {sala} ---")
            for entrada in self._salas[sala]["historico"]:
                print(f"[{entrada['hora']}] {entrada['autor']}: {entrada['msg']}")
            print("-------------------------------\n")

class Usuario:
    def __init__(self, mediator, nome):
        self.mediator = mediator
        self.nome = nome
    
    def enviar_mensagem(self, mensagem: str, sala):
        print(f"{self.nome} envia para [{sala}]: {mensagem}")
        self.mediator.enviar_mensagem(mensagem, self, sala)

    def receber_mensagem(self, mensagem: str, de_quem: str, sala):
        print(f"{self.nome} recebeu de {de_quem} (na sala {sala}): {mensagem}")

