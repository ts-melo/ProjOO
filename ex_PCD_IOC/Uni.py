from IObservadorPCD import IObservadorPCD

class Universidade(IObservadorPCD):
    def __init__(self, nome):
        self.nome = nome
# esse é o CALLBACK. A IOC acontece porque a universidade "espera a PCD a chamá-la"
    def atualizar(self, nome_pcd, temp, ph, umidade):
        print(f"--- Notificação para {self.nome} ---")
        print(f"Fonte: {nome_pcd} | Temp: {temp}°C | pH: {ph} | UR: {umidade}%")