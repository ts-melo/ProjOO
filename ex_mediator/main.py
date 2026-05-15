
def main():
    from IMediator import ChatMediator
    from Mediador import ChatRoom, Usuario

    room = ChatRoom()
    alice = Usuario(room, "Alice")
    bob = Usuario(room, "Bob")
    charlie = Usuario(room, "Charlie")

    room.adicionar_usuario(alice, "Geral")
    room.adicionar_usuario(bob, "Geral")
    room.adicionar_usuario(charlie, "estudos")
    room.adicionar_usuario(alice, "estudos")

    alice.enviar_mensagem("Olá", "Geral")
    bob.enviar_mensagem("Oi, Alice! Como vai?", "Geral")
    charlie.enviar_mensagem("Alguém para estudar?", "estudos")

if __name__ == "__main__":
    main()