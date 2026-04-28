from Visitor import CompanyVisitor, Element
class Pdf(CompanyVisitor):
    def ver_department(self, department):
        print("gerando relatorio em formato PDF do departamento: " + department.nome)
    def ver_employee(self, employee):
        print("gerando relatorio em formato PDF do empregado: " + employee.nome)

class Json(CompanyVisitor):
    def ver_department(self, department):
        print("gerando relatorio em formato JSON do departamento: " + department.nome)
    def ver_employee(self, employee):
        print("gerando relatorio em formato JSON do empregado: " + employee.nome)



class Xsls(CompanyVisitor):
    def ver_department(self, department):
        print("gerando relatorio em formato Xsls do departamento: " + department.nome)
    def ver_employee(self, employee):
        print("gerando relatorio em formato Xsls do empregado: " + employee.nome)

