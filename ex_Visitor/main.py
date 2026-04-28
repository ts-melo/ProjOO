from Visitor import CompanyVisitor
from GeradoresRelatorios import Pdf, Json, Xsls
from Employee import Empregado, Departamento
def main():
    empregado1 = Empregado("João", "Analista")
    empregado2 = Empregado("Maria", "Desenvolvedora")
    departamento_ti = Departamento("TI")
    departamento_ti.add_empregado(empregado1)
    departamento_ti.add_empregado(empregado2)

    rel_pdf = Pdf()
    rel_json = Json()

    print("Gerando relatório PDF:")
    departamento_ti.accept(rel_pdf)
    print("\nGerando relatório JSON:")
    departamento_ti.accept(rel_json)





if __name__ == "__main__":
    main()