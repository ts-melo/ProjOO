
import random
import tracemalloc
from FabricaEspecies import FabricaEspecies
from DesenhaArvore import ArvoreNoMapa
from ArvoreSemFlyweight import ArvoreSemFlyweight
def main():
    especies = [f"Especie_{i}" for i in range(50)]
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
    print(floresta[999].desenhar())



    print(f"\nTotal de objetos 'Árvore no Mapa' (Leves): {len(floresta)}")
    print(f"Total de objetos 'Especie/Textura' (Pesados) em RAM: {len(FabricaEspecies._especies)}")
    print("\nVerificando compartilhamento de objetos Flyweight:")

    a1 = floresta[0]
    a2 = floresta[1]

    print(f"Espécie árvore 1: {a1.especie.nome}")
    print(f"ID objeto espécie 1: {id(a1.especie)}")

    print(f"Espécie árvore 2: {a2.especie.nome}")
    print(f"ID objeto espécie 2: {id(a2.especie)}")

    print(f"memoria pico alocada com flyweight : {memoria_pico/(1024 * 1024):.4f} MB")

    tracemalloc.start()
    floresta_sem = []
    print("construindo floresta sem flyweight:\n")
    for i in range(total_arvores):
        nome = random.choice(especies)
        textura = bytearray(100000)

        arvore = ArvoreSemFlyweight(
            nome,
            textura,
            random.randint(0,1000),
            random.randint(0, 1000),
            round(random.uniform(5.0, 30.0), 2),
            round(random.uniform(0.5, 3.0), 2),
            random.randint(5,20)
        )
        floresta_sem.append(arvore)
    _, pico_sem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"memoria pico sem flyweight : {pico_sem / (1024 * 1024):.4} MB")

if __name__ == "__main__":
    main()
