"""Employee"""
from datetime import date

class Employee:
    """Employee"""
    def __init__(self,name,birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        """Name Getter"""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value.upper()

    @property
    def birth_date(self):
        """Birth Date Getter"""
        return self.__birth_date

    @birth_date.setter
    def birth_date(self,value):
        self.__birth_date = date.fromisoformat(value)


john = Employee("John", "2001-02-07")

john.name = "Billy"

print(john.birth_date)
print(john.name)
