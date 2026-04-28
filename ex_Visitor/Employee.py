from Visitor import Element, CompanyVisitor
class Empregado(Element):
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def accept(self, visitor :CompanyVisitor):
        visitor.ver_employee(self)

class Departamento(Element):
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []

    def add_empregado(self, empregado):
        self.empregados.append(empregado)

    def accept(self, visitor: CompanyVisitor):
        visitor.ver_department(self)
        for e in self.empregados:
            e.accept(visitor)