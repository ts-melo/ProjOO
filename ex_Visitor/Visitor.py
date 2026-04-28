from abc import ABC, abstractmethod

class CompanyVisitor(ABC):
    @abstractmethod
    def visit_department(self, department):
        pass

    @abstractmethod
    def visit_employee(self, employee):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: CompanyVisitor):
        pass