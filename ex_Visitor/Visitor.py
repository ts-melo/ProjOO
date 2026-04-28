from abc import ABC, abstractmethod

class CompanyVisitor(ABC):
    @abstractmethod
    def ver_department(self, department):
        pass

    @abstractmethod
    def ver_employee(self, employee):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: CompanyVisitor):
        pass