from PCD import PCD
from Uni import Universidade
def main():
 #a criação de objetos independentes - baixo acoplamanento
    pcd_rio_negro = PCD("PCD-RIO-NEGRO")
    pcd_solimoes = PCD("PCD-SOLIMOES")

    uni_sjc = Universidade("ICT-SJC")
    uni_manaus = Universidade("UFAM")

# com a inversão de controle, nós decidimos quem observa a quem fora das classes pcd e universidade. Como se "ligamos" os objetos externamente

    pcd_rio_negro.registrar_interesse(uni_sjc)
    pcd_rio_negro.registrar_interesse(uni_manaus)

    pcd_solimoes.registrar_interesse(uni_manaus)

#na execução o fluxo agora é guiado por eventos - o sujeito pcd assume o controlle e avisa as universidades
    pcd_solimoes.set_medicoes(29, 6.5, 88)
    pcd_rio_negro.set_medicoes(24.3, 8, 70)
