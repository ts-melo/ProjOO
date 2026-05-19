import sys
import random
import tracemalloc
from Arvore import EspecieArvore
from FabricaEspecies import FabricaEspecies
from DesenhaArvore import ArvoreNoMapa

def main():
    especies = ["Carvalho", "Pinheiro", "Bétula", "Salgueiro", "Álamo"]
    floresta = []
    total_arvores = 1000

    print(f"Criando a floresta com {total_arvores} árvores...")
    tracemalloc.start()
    for i in range(total_arvores):
        nome = random.choice(especies)
        especie_fly = FabricaEspecies.get_especie(nome)

        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        altura = round(random.uniform(5.0, 30.0), 2)
        diametro = round(random.uniform(0.5, 3.0), 2)
        galhos = random.randint(5, 20)

        nova_arvore = ArvoreNoMapa(x, y, altura, diametro, galhos, especie_fly)
        floresta.append(nova_arvore)
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nAmostra das árvores plantadas (Características únicas, mesma espécie base):")
    print(floresta[0].desenhar())
    print(floresta[500].desenhar())
    print(floresta[9999].desenhar())

    print(f"\nTotal de objetos 'Árvore no Mapa' (Leves): {len(floresta)}")
    print(f"Total de objetos 'Especie/Textura' (Pesados) em RAM: {len(FabricaEspecies._especies)}")
    print(f"memoria pico alocada : {memoria_pico/(1024 * 1024):.4f} MB")

if __name__ == "__main__":
    main()
