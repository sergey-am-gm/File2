
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self): # Нам пишут предупреждение, что мы переопределили метод __str__  для объекта?
        return (f'Название: {self.name}, кол-во этажей: {str(self.number_of_floors)}')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1.__str__())
print(h2.__str__())

# __len__
print(len(h1))
print(len(h2))