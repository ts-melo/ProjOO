import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass

#metodo pra execução de comando (interface)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#entidade/modelo de dominio, facilita a tipagem e visualização dos dados e adição de campos no futuro
@dataclass
class Pessoa:
    id : int
    nome : str
    def __str__(self):
        return f"[{self.id}] = '{self.nome}'"

#receiver contains the business logic, does the actual work when a command is executed
class BancoDados:
    def __init__(self):
        self._pessoas: dict[int, Pessoa] = {}

    def adicionar(self, id_pessoa, nome):
        self._pessoas[id_pessoa] = Pessoa(id_pessoa, nome)
        print(f"pessoa {self._pessoas[id_pessoa]} , id {id_pessoa} adicionada")

    def remover(self, id_pessoa):
        if self._pessoas.pop(id_pessoa,None):
            print("removido")
        else:
            print("não encontrado")
    
    def buscar(self, id_pessoa):
        pessoa = self._pessoas.get(id_pessoa)
        if pessoa:
            print(pessoa)
        else:
            print("não encontrado")
        
    def listar_todos(self):
        if not self._pessoas:
            print("banco vazio")
        else:
            for pessoa in self._pessoas.values():
                print(f" -> {pessoa}")

#concrete commands, implement various kinds of requests, isn't supposed to perform the work on its own, but rather pass the call to the receiver
class Cnew(Command):
    def __init__(self, receiver, id_pessoa, nome):
        self._receiver = receiver
        self._id_pessoa = id_pessoa
        self._nome = nome
    def execute(self):
        self._receiver.adicionar(self._id_pessoa, self._nome)

class Cdelete(Command):
    def __init__(self, receiver, id_pessoa):
        self._reveiver = receiver
        self._id = id_pessoa
    def execute(self):
        self._reveiver.remover(self._id)

class Cget(Command):
    def __init__(self, receiver, id_pessoa):
        self._receiver = receiver
        self._id = id_pessoa
    def execute(self):
        self._receiver.buscar(self._id)

class Call(Command):
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.listar_todos()

#sender class, resposible for initiating requests. stores a ref to a command object
class Invoker:
    def __init__(self):
        self._comando = None
    def set_comando(self, comando):
        self._comando = comando
    def executar_comando(self):
        if isinstance(self._comando, Command):
            self._comando. execute()
    

if __name__ == "__main__":
    db = BancoDados()
    invoker = Invoker()

    print("=== Banco de Dados ===")
    print("Comandos: new <id> <nome>, delete <id>, get <id>, all, exit")
    print("-" * 44)

    while True:
        try:
            entrada = input("banco> ").strip()
            
            if not entrada:
                continue
                
            args = entrada.split()
            nome_comando = args[0].lower()
            comando_obj = None

            if nome_comando == "exit":
                print("Encerrando o banco de dados...")
                break

            #criação do comando
            if nome_comando == "new" and len(args) >= 3:
                nome_completo = " ".join(args[2:])
                comando_obj = Cnew(db, int(args[1]), nome_completo)
                
            elif nome_comando == "delete" and len(args) >= 2:
                comando_obj = Cdelete(db, int(args[1]))
                
            elif nome_comando == "get" and len(args) >= 2:
                comando_obj = Cget(db, int(args[1]))
                
            elif nome_comando == "all":
                comando_obj = Call(db)
                
            else:
                print(f"  -> Erro: Comando inválido ou argumentos faltando.")
                continue

            #passa o comando p invoker executar
            invoker.set_comando(comando_obj)
            invoker.executar_comando()

        except ValueError:
            print(" O <id> deve ser um número inteiro válido.")
        except KeyboardInterrupt:
            print("\nEncerrando o banco de dados...")
            break
