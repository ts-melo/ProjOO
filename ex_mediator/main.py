
def main():
    from IMediator import ChatMediator
    from Mediador import ChatRoom, Usuario

    room = ChatRoom()
    alice = Usuario(room, "Alice")
    bob = Usuario(room, "Bob")

    room.adicionar_usuario(alice)
    room.adicionar_usuario(bob)

    alice.enviar_mensagem("Olá, Bob!")
    bob.enviar_mensagem("Oi, Alice! Como vai?")