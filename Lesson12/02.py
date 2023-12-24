import time
from task1 import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("Attention")

    @staticmethod
    def load():
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")


# Приклад використання:
truck1 = Truck(brand="Volvo", age=5, mark="VNL", max_load=10000, color="blue", weight=8000)
truck2 = Truck(brand="Scania", age=3, mark="R-series", max_load=12000, color="red", weight=8500)

car1 = Car(brand="Toyota", age=2, mark="Camry", max_speed=200, color="silver", weight=1500)
car2 = Car(brand="Honda", age=1, mark="Civic", max_speed=180, color="white", weight=1300)

# Перевірка методів і атрибутів
print("Truck 1:")
truck1.move()
truck1.load()
truck1.birthday()

print("\nTruck 2:")
truck2.move()
truck2.load()
truck2.birthday()

print("\nCar 1:")
car1.move()
car1.stop()
car1.birthday()

print("\nCar 2:")
car2.move()
car2.stop()
car2.birthday()
