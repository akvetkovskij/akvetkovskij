# Classwork 7
# Вводится химическая формула: H2O -> {'H': 2, 'O': 1}
# C2H5OH -> {'C': 2, 'H': 6, 'O': 1}
# formula = {}
# input_formula = 'C2H5OH'
class Person:

    def __init__(self, name: str, age: int):
        self.name = name.title()
        self.age = age


vasya = Person('Vasya', 27)
print(vasya.age)
