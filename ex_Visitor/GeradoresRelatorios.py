from Visitor import CompanyVisitor

class Pdf(CompanyVisitor):
    def visit_department(self, department):
        print(f"Relatório em formato PDF: processando departamento {department.nome}")

    def visit_employee(self, employee):
        print(f"Relatório em formato PDF: convertendo dados de {employee.nome}")

class Json(CompanyVisitor):
    def visit_department(self, department):
        print(f"Relatório em formato JSON: processando departamento {department.nome}")

    def visit_employee(self, employee):
        print(f"Relatório em formato JSON: convertendo dados de {employee.nome}")

class Xsls(CompanyVisitor):
    def visit_department(self, department):
        print(f"Relatório em formato Xsls: processando departamento {department.nome}")

    def visit_employee(self, employee):
        print(f"Relatório em formato Xsls: convertendo dados de {employee.nome}")