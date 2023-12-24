class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print(f"{self.brand} is moving")

    def stop(self):
        print(f"{self.brand} has stopped")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! {self.brand} is now {self.age} years old")


car1 = Auto(brand="Toyota", age=3, mark="Camry", color="blue", weight=1500)
car2 = Auto(brand="Honda", age=2, mark="Civic", color="red", weight=1300)

car1.move()
car1.stop()
car1.birthday()

car2.move()
car2.stop()
car2.birthday()
