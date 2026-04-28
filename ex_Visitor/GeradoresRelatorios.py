from Visitor import CompanyVisitor, Element
# Em GeradoresRelatorios.py
class Pdf(CompanyVisitor):
    def visit_department(self, department):
        print(f"=== RELATÓRIO PDF: DEPARTAMENTO {department.nome} ===")
        print("Lista de Colaboradores:")

    def visit_employee(self, employee):
        print(f"  - Nome: {employee.nome} | Cargo: {employee.cargo}")

class Json(CompanyVisitor):
    def visit_department(self, department):
        print(f"{{ 'departamento': '{department.nome}', 'funcionarios': [")

    def visit_employee(self, employee):
        print(f"    {{ 'nome': '{employee.nome}', 'cargo': '{employee.cargo}' }},")

class Xsls(CompanyVisitor):
    def ver_department(self, department):
        print("gerando relatorio em formato Xsls do departamento: " + department.nome)
    def ver_employee(self, employee):
        print("gerando relatorio em formato Xsls do empregado: " + employee.nome)

