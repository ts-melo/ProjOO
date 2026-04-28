from GeradoresRelatorios import Pdf, Json
from Employee import Empregado, Departamento

def main():
    # Criando os dados
    e1 = Empregado("João", "Analista")
    e2 = Empregado("Maria", "Desenvolvedora")
    ti = Departamento("Tecnologia")
    ti.add_empregado(e1)
    ti.add_empregado(e2)

    # Criando os visitantes (formatos)
    rel_pdf = Pdf()
    rel_json = Json()

    print("--- SOLICITANDO PDF ---")
    ti.accept(rel_pdf)

    print("\n--- SOLICITANDO JSON ---")
    ti.accept(rel_json)

if __name__ == "__main__":
    main()